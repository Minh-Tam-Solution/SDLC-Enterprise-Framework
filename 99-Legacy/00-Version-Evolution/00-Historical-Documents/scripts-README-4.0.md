# 🛠️ SDLC 4.0 Compliance Scanner
## Version: 4.0 - MTS SDLC Framework Compliant
## Date: September 3, 2025
## Status: DESIGN PHASE
## Framework: SDLC 4.0 Compliant
## Sponsor: Minh Tam Solution (MTS)
## Brand: BFlow by MTS - The MVV-Driven Business Operating System

---

```bash
# Scan current directory
python3 scripts/compliance/sdlc_scanner.py

# Scan specific project
python3 scripts/compliance/sdlc_scanner.py --project-root /path/to/project

# Save report to file
python3 scripts/compliance/sdlc_scanner.py --output report.json
```

---

## 📋 What It Checks

The scanner validates projects against SDLC 4.0 standards:

1. **Documentation Standards** - Proper structure and formatting
2. **Code Organization** - Correct folder structure
3. **Naming Conventions** - Consistent naming patterns
4. **Required Files** - Essential documentation present
5. **Compliance Threshold** - Minimum 85% compliance required

---

## 📊 Compliance Scoring

- **85-100%**: ✅ PASS - Meets SDLC 4.0 standards
- **70-84%**: ⚠️ WARNING - Improvements needed
- **Below 70%**: ❌ FAIL - Major revisions required

---

## 🔧 Usage Examples

### Basic Scan
```bash
python3 scripts/compliance/sdlc_scanner.py
```

### Detailed Report
```bash
python3 scripts/compliance/sdlc_scanner.py --verbose
```

### CI/CD Integration
```bash
# In your CI/CD pipeline
python3 scripts/compliance/sdlc_scanner.py --project-root . --output compliance.json
if [ $? -ne 0 ]; then
    echo "Compliance check failed"
    exit 1
fi
```

---

## 📝 Report Format

The scanner generates JSON reports with:
- Total files scanned
- Compliance score percentage
- List of violations
- Recommendations for fixes
- Timestamp of scan

---

## 🆘 Support

- **Framework Documentation**: See main README.md
- **Contact**: dev@mtsolution.com.vn
- **License**: MIT (Open Source)

---

**MTS SDLC Framework v4.0**  
*© 2025 Minh Tam Solution (MTS)*