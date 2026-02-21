#!/bin/bash

###############################################################################
# RFC-001: Legacy Document Organization Standard - Migration Script
# 
# Purpose: Safely migrate 99-Legacy/ content to 10-Archive/{NN}-Legacy/
# Status: PRODUCTION VALIDATED (BFlow Platform, 3 live customers)
# Usage: ./migrate-legacy-to-archive.sh <source_dir> [--dry-run]
#
# Example:
#   cd /path/to/project/docs
#   ../../scripts/migrate-legacy-to-archive.sh . --dry-run
#   ../../scripts/migrate-legacy-to-archive.sh .
#
###############################################################################

set -eu

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SOURCE_DIR="${1:-.}"
DRY_RUN="${2:---dry-run}"  # Default to dry-run for safety
BATCH_SIZE=50  # Files per progress checkpoint
TOTAL_MIGRATED=0
TOTAL_ERRORS=0

###############################################################################
# Functions
###############################################################################

log_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
    TOTAL_ERRORS=$((TOTAL_ERRORS + 1))
}

log_section() {
    echo
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}${1}${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

extract_stage_id() {
    local dir="$1"
    local basename=$(basename "$dir")
    
    # Extract stage number from dirname like "00-foundation", "02-design", etc
    if [[ $basename =~ ^([0-9][0-9])-[a-z-]+$ ]]; then
        echo "${BASH_REMATCH[1]}"
    else
        echo ""
    fi
}

validate_migration_plan() {
    local source="$1"
    local stage_id="$2"
    
    if [[ ! -f "$source/README.md" ]] && [[ -z "$(find "$source" -type f 2>/dev/null | head -1)" ]]; then
        log_warn "Source is empty: $source"
        return 1
    fi
    
    if [[ -z "$stage_id" ]] || [[ ! "$stage_id" =~ ^[0-9][0-9]$ ]]; then
        log_error "Invalid stage ID detected: '$stage_id'"
        return 1
    fi
    
    return 0
}

migrate_stage_legacy() {
    local stage_dir="$1"
    local dry_run="$2"
    
    local stage_id=$(extract_stage_id "$stage_dir")
    
    if [[ -z "$stage_id" ]]; then
        # Skip - not a stage folder
        return 0
    fi
    
    local legacy_source="$stage_dir/99-Legacy"
    
    if [[ ! -d "$legacy_source" ]]; then
        # No legacy content in this stage
        return 0
    fi
    
    if ! validate_migration_plan "$legacy_source" "$stage_id"; then
        return 1
    fi
    
    # Determine archive root (10-archive or 10-Archive depending on project)
    local archive_root="$(dirname "$stage_dir")/10-archive"
    if [[ ! -d "$archive_root" ]]; then
        archive_root="$(dirname "$stage_dir")/10-Archive"
    fi
    
    local archive_stage_dir="$archive_root/${stage_id}-Legacy"
    
    log_info "Migrating: $legacy_source → $archive_stage_dir"
    
    # Count files
    local file_count=$(find "$legacy_source" -type f 2>/dev/null | wc -l)
    log_info "  Files to migrate: $file_count"
    
    if [[ "$dry_run" == "--dry-run" ]]; then
        log_warn "  [DRY-RUN] Would create: $archive_stage_dir"
        log_warn "  [DRY-RUN] Would copy: cp -r \"$legacy_source\"/* \"$archive_stage_dir\""
        return 0
    fi
    
    # Execute migration
    mkdir -p "$archive_stage_dir" || {
        log_error "Failed to create: $archive_stage_dir"
        return 1
    }
    
    cp -r "$legacy_source"/* "$archive_stage_dir"/ || {
        log_error "Failed to copy content from: $legacy_source"
        return 1
    }
    
    # Verify count matches
    local copied_count=$(find "$archive_stage_dir" -type f 2>/dev/null | wc -l)
    if [[ $copied_count -ne $file_count ]]; then
        log_error "File count mismatch: copied $copied_count but expected $file_count"
        return 1
    fi
    
    # Remove original
    rm -rf "$legacy_source" || {
        log_error "Failed to delete: $legacy_source"
        return 1
    }
    
    log_success "Migrated: $stage_id-Legacy ($file_count files)"
    TOTAL_MIGRATED=$((TOTAL_MIGRATED + file_count))
    
    return 0
}

create_archive_readme() {
    local archive_root="$1"
    local dry_run="$2"
    
    if [[ -f "$archive_root/README.md" ]]; then
        log_info "Archive README already exists"
        return 0
    fi
    
    local readme_path="$archive_root/README.md"
    
    if [[ "$dry_run" == "--dry-run" ]]; then
        log_warn "  [DRY-RUN] Would create: $readme_path"
        return 0
    fi
    
    cat > "$readme_path" << 'EOF'
# 10-Archive: Legacy Documentation

**Purpose**: Centralized storage for archived and deprecated content from active stages (00-09)

**AI Directive**: 🤖 **NEVER READ** - This folder contains outdated, deprecated, and archived content that should not inform current development decisions. AI assistants should ignore this entire directory.

## Structure

- `00-Legacy/` - Foundation stage archives (version evolution, old roadmaps)
- `01-Legacy/` - Planning stage archives (deprecated analysis, old requirements)
- `02-Legacy/` - Design stage archives (old architecture designs, deprecated specs)
- `03-Legacy/` - Integration stage archives (deprecated integrations, old contracts)
- `04-Legacy/` - Build stage archives (POC code, old sprints, legacy implementations)
- `05-Legacy/` - Tools stage archives (deprecated tool guides, old templates)
- `06-Legacy/` - Deploy stage archives (old deployment procedures, legacy infrastructure)
- `07-Legacy/` - Operate stage archives (legacy operational procedures)
- `08-Legacy/` - Collaborate stage archives (old processes, deprecated templates)
- `09-Legacy/` - Govern stage archives (deprecated policies, old RFCs)

## Guidelines

1. **No new content**: Do not add files directly here. Archive them to the appropriate `{NN}-Legacy/` subfolder.
2. **Dated organization**: Subfolders within each stage should include the deprecation date (e.g., `2026-02-13-old-design/`)
3. **Maintenance**: Content older than 12 months can be evaluated for permanent deletion
4. **AI context**: Always add `AI-NEVER-READ` directive to README files

See [SDLC-Legacy-Document-Organization.md](../../02-Core-Methodology/Documentation-Standards/SDLC-Legacy-Document-Organization.md) for RFC-001 standard.

**Created**: $(date +'%Y-%m-%d')
**RFC**: RFC-001 Legacy Document Organization Standard
**Framework**: SDLC 6.1.1+
EOF
    
    log_success "Created: $readme_path"
}

validate_migration() {
    local source_dir="$1"
    
    log_section "VALIDATION: Checking for remaining 99-Legacy/"
    
    local found_legacy=$(find "$source_dir" -maxdepth 3 \
        -type d -name "99-Legacy" \
        -path "*/0[0-9]-*/99-Legacy" 2>/dev/null | wc -l)
    
    if [[ $found_legacy -eq 0 ]]; then
        log_success "✓ No 99-Legacy/ folders found in stages 00-09"
        return 0
    else
        log_error "Found $found_legacy remaining 99-Legacy/ folders in stages"
        find "$source_dir" -maxdepth 3 -type d -name "99-Legacy" \
            -path "*/0[0-9]-*/99-Legacy" 2>/dev/null | while read legacy_dir; do
            log_error "  - $legacy_dir"
        done
        return 1
    fi
}

###############################################################################
# Main Execution
###############################################################################

log_section "RFC-001 LEGACY MIGRATION SCRIPT"
log_info "Source directory: $SOURCE_DIR"
log_info "Dry-run mode: ${DRY_RUN:---live}"
log_info "Start time: $(date +'%Y-%m-%d %H:%M:%S')"

# Find all stage directories
if [[ ! -d "$SOURCE_DIR" ]]; then
    log_error "Source directory not found: $SOURCE_DIR"
    exit 1
fi

log_section "PHASE 1: DISCOVER STAGE DIRECTORIES"

declare -a STAGE_DIRS=()
while IFS= read -r -d '' dir; do
    if [[ -d "$dir/99-Legacy" ]]; then
        STAGE_DIRS+=("$dir")
        log_info "Found: $(basename "$dir")"
    fi
done < <(find "$SOURCE_DIR" -maxdepth 1 -type d -name "0[0-9]-*" -print0 2>/dev/null)

if [[ ${#STAGE_DIRS[@]} -eq 0 ]]; then
    log_warn "No stage folders with 99-Legacy/ found"
    log_info "Migration complete - nothing to do"
    exit 0
fi

log_success "Found ${#STAGE_DIRS[@]} stages with 99-Legacy content"

log_section "PHASE 2: ENSURE ARCHIVE ROOT EXISTS"

local archive_root="$SOURCE_DIR/10-archive"
if [[ ! -d "$archive_root" ]]; then
    archive_root="$SOURCE_DIR/10-Archive"
fi

if [[ ! -d "$archive_root" ]]; then
    log_warn "Archive root does not exist: $archive_root"
    if [[ "$DRY_RUN" != "--dry-run" ]]; then
        mkdir -p "$archive_root"
        log_success "Created: $archive_root"
    fi
fi

log_section "PHASE 3: MIGRATE LEGACY CONTENT"

for stage_dir in "${STAGE_DIRS[@]}"; do
    if ! migrate_stage_legacy "$stage_dir" "$DRY_RUN"; then
        log_error "Migration failed for: $stage_dir"
    fi
done

log_section "PHASE 4: CREATE ARCHIVE README"

if [[ "$DRY_RUN" != "--dry-run" ]]; then
    create_archive_readme "$archive_root" "$DRY_RUN"
fi

log_section "PHASE 5: VALIDATION"

if validate_migration "$SOURCE_DIR"; then
    log_success "✓ Migration validation successful"
else
    log_warn "⚠ Migration validation found issues (see above)"
fi

log_section "MIGRATION SUMMARY"

log_info "Total files migrated: $TOTAL_MIGRATED"
log_info "Total errors: $TOTAL_ERRORS"
log_info "End time: $(date +'%Y-%m-%d %H:%M:%S')"

if [[ $TOTAL_ERRORS -gt 0 ]]; then
    log_error "Migration completed with $TOTAL_ERRORS errors"
    exit 1
else
    if [[ "$DRY_RUN" == "--dry-run" ]]; then
        log_warn "Dry-run mode - no changes were made"
        log_info "To execute migration, run: ./migrate-legacy-to-archive.sh $SOURCE_DIR"
    else
        log_success "Migration completed successfully!"
    fi
    exit 0
fi
