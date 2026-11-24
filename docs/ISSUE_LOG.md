# PHANTOM — Issue & Debugging Log

Every engineering obstacle, failed test, bug, or unexpected behavior is recorded here with root-cause analysis and lessons learned.

---

## Log Template
```markdown
### Issue #XXX: [Short summary of the bug or failure]
- **Date:** YYYY-MM-DD
- **Module Affected:** [RECON / FINGERPRINT / VULNINTEL / RISK / ATTACK MAP / DOSSIER / INFRA]
- **Error Message / Observed Behavior:**
  [Paste error traceback or describe incorrect behavior]
- **Root Cause:**
  [Why did this happen?]
- **Fix Attempted & Solution:**
  [How was it resolved?]
- **Lesson Learned:**
  [What conceptual or practical insight prevents this in the future?]
```

---

## Resolved Issues

### Issue #001: Nmap CLI missing from system PATH
- **Date:** 2026-11-24
- **Module Affected:** INFRA / SETUP
- **Observed Behavior:** Command `nmap --version` failed with `CommandNotFoundException`.
- **Root Cause:** Nmap is not currently installed or not registered in the Windows system environment PATH.
- **Resolution Plan:** For Phase 0 and the initial exercises of Module 01, we will deliberately use Python's built-in `socket` library to build our own scanner from first principles. Nmap installation will be scheduled prior to Phase 2 (Module 02 integration).
- **Lesson Learned:** Building low-level socket tools first ensures deep understanding of Layer 4 networking before relying on external scanning binaries.
