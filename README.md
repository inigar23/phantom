# PHANTOM — Attack Surface Intelligence and Vulnerability Assessment Platform

> **Tagline:** Discover. Analyze. Investigate. Secure.  
> **Author:** Ragini V S (Computer and Communication Engineering, Amrita School of Engineering)  
> **Mentor:** Antigravity (AI Technical Mentor & Software Architect)

---

## 1. Executive Overview

**PHANTOM** is a modular, defense-oriented cybersecurity platform designed to help security engineers and Security Operations Center (SOC) analysts discover exposed network assets, identify running services, map known vulnerabilities (CVEs), prioritize security risks using contextual scoring, visualize network exposure, and generate actionable technical and executive reports.

Unlike automated black-box scripts, PHANTOM is engineered from first principles:
- **Module 01: RECON** — Asset & port discovery built on pure Python sockets, transitioning to structured Nmap probing.
- **Module 02: FINGERPRINT** — Protocol analysis, banner grabbing, and service identification.
- **Module 03: VULNINTEL** — NIST National Vulnerability Database (NVD) REST API integration with local caching and version matching.
- **Module 04: RISK ENGINE** — Contextual, explainable risk prioritization balancing CVSS metrics, exposure vectors, and asset criticality.
- **Module 05: ATTACK MAP** — Graph-theoretic network topology and vulnerability mapping using Cytoscape.js.
- **Module 06: DOSSIER** — Automated executive and remediation report generation in PDF format.

---

## 2. Architecture & Design Principles

1. **Modular Separation of Concerns:** Each module operates independently with well-defined data models.
2. **Defensive by Design:** Built-in scan scope allowlisting, rate limiting, and input sanitization to ensure testing is strictly authorized.
3. **Reproducibility:** Strict virtual environment dependency pinning and containerized execution.

---

## 3. Technology Stack

- **Core Language:** Python 3.13+
- **Reconnaissance Engine:** Python Sockets, Nmap
- **Backend API:** FastAPI
- **Frontend Dashboard:** React, Tailwind CSS
- **Network Visualization:** Cytoscape.js / NetworkX
- **Testing:** Pytest
- **DevSecOps:** Docker, GitHub Actions CI

---

## 4. Project Structure

```text
phantom/
│
├── docs/                      # Architectural & progress documentation
│   ├── ARCHITECTURE.md        # System design & data flow specifications
│   ├── ISSUE_LOG.md           # Debugging journal and error recovery
│   ├── LEARNING_LOG.md        # Conceptual notes & practical takeaways
│   ├── PROJECT_ROADMAP.md     # Milestone tracking & feature statuses
│   └── SESSION_TRACKER.md     # Daily 60-minute session records
│
├── phantom/                   # Core application package
│   ├── core/                  # Shared utilities, logging, validation
│   └── modules/               # The 6 PHANTOM security engines
│       ├── recon/
│       ├── fingerprint/
│       ├── vulnintel/
│       ├── risk/
│       ├── attackmap/
│       └── dossier/
│
├── tests/                     # Automated test suite
│   └── unit/                  # Unit tests for core functions
│
├── .gitignore                 # Environment and artifact exclusions
├── README.md                  # Project overview
└── requirements.txt           # Production and development dependencies
```

---

## 5. Development Status

* **Completed:** Day 4 — Module 01 (`RECON`) CIDR subnet expansion (`expand_targets`), multithreaded port scanning (`5.16s` ➔ `0.54s` benchmark), target scope guardrails, and `pytest` unit suite (11/11 passing).
* **Next Up:** Day 5 — Structured RECON output models & CLI runner, then Module 02 (`FINGERPRINT`).
* Follows a strict **60-Minute Daily Engineering Sprint** and **Stop/Continue (Green/Yellow/Red)** validation system.
