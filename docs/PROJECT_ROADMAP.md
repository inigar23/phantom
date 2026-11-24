# PHANTOM — Project Roadmap & Progress Tracker

This document tracks all 6 functional modules and supporting phases, showing dependencies, current statuses, and completion metrics.

---

## Roadmap Overview

| Module / Milestone | Focus Area | Status | Planned Timeline |
|---|---|:---:|---|
| **Phase 0: Environment & Architecture** | Project skeleton, virtual environment, Git, documentation suite | 🟢 In Progress | Days 1–2 |
| **Module 01: RECON** | IP subnet math, TCP handshakes, Python socket scanner, host discovery | ⚪ Pending | Days 3–10 |
| **Module 02: FINGERPRINT** | Banner grabbing, protocol probes (HTTP/SSH), Nmap wrapper & XML parser | ⚪ Pending | Days 11–18 |
| **Module 03: VULNINTEL** | NIST NVD API client, rate limiting, SQLite caching, version matching | ⚪ Pending | Days 19–26 |
| **Module 04: RISK ENGINE** | Quantitative risk algorithm (CVSS + exposure + asset weight), explainability | ⚪ Pending | Days 27–32 |
| **Module 05: ATTACK MAP** | FastAPI backend endpoints, React / Tailwind dashboard, Cytoscape graph | ⚪ Pending | Days 33–40 |
| **Module 06: DOSSIER** | Automated PDF reporting engine with remediation advice | ⚪ Pending | Days 41–45 |
| **Phase 7: Hardening & Testing** | Unit tests (`pytest`), security input sanitization, edge cases | ⚪ Pending | Days 46–50 |
| **Phase 8: DevSecOps & Portfolio** | Docker container, GitHub Actions CI/CD, polished README, demo video | ⚪ Pending | Days 51–55 |

---

## Detailed Milestone Checklist

### Phase 0: Environment & Architecture
- [x] Inspect local Windows environment (Python 3.13.5, Git 2.55.0).
- [x] Create project workspace at `scratch/phantom`.
- [x] Configure `.venv` virtual environment.
- [x] Configure `.gitignore` and initialize Git repository.
- [x] Create documentation & tracking suite (`SESSION_TRACKER`, `LEARNING_LOG`, `PROJECT_ROADMAP`, `ISSUE_LOG`, `ARCHITECTURE`).
- [ ] Make initial commit (`feat: initialize project skeleton and tracking suite`).

### Module 01: RECON (Asset Discovery)
- [ ] Socket basics & TCP 3-way handshake deep dive.
- [ ] Single-port TCP connect scanner on localhost loopback.
- [ ] Range scanning and timeout handling.
- [ ] CIDR subnet parsing and IP validation (`ipaddress` module).
- [ ] Concurrency / multithreaded scanning.
- [ ] Scope allowlisting and security guardrails.
