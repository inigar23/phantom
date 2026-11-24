# PHANTOM — Learning Log

A persistent record of cybersecurity concepts, software engineering principles, challenges, and mastery checkpoints throughout the PHANTOM journey.

---

## Entry 01 — 2026-11-24: Virtual Environments & Dependency Isolation

### 1. Concepts Learned
* **Dependency Hell & Diamond Dependency Problem:**
  * When two libraries require conflicting versions of a shared sub-dependency (e.g., Library A needs `urllib3 >= 2.0`, while Library B needs `urllib3 == 1.26`).
  * Python can only load one version of any package into memory per process. Installing packages globally across projects causes collisions and silent runtime failures.
* **Virtual Environment (`venv`) Architecture:**
  * A lightweight, isolated environment directory containing its own Python binary/symlink and separate `site-packages` directory.
  * Allows project-specific library management without modifying system-wide Python.
* **Git Hygiene in Security Projects:**
  * Why `.venv/` is excluded in `.gitignore`: It contains platform-specific compiled binaries and thousands of third-party files. Sharing it causes cross-platform breakage and bloat.
  * We commit `requirements.txt` instead, ensuring deterministic, reproducible builds.

### 2. Practical Exercises Completed
* Initialized an isolated environment with `python -m venv .venv`.
* Validated the isolated binary path (`.venv\Scripts\python.exe`).
* Configured `.gitignore` with standard Python, OS, test, and environment patterns.
* Initialized the local Git repository and audited untracked files via `git status`.

### 3. What I Can Now Explain Independently
* Why installing Python packages globally is dangerous for production systems and college projects.
* What a virtual environment physically consists of on disk.
* Why `.gitignore` is crucial for repository hygiene and security (preventing accidental secret leaks like `.env`).
