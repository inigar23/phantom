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

---

## Entry 02 — 2026-11-25: Ports, TCP 3-Way Handshake & Socket Probing

### 1. Concepts Learned
* **IP Addresses vs. Ports:** An IP identifies the host machine; a port (`0–65535`) identifies a specific service/program inside it. `127.0.0.1` (localhost) loops back to the local machine for safe testing.
* **TCP 3-Way Handshake:** `SYN` ➔ `SYN-ACK` ➔ `ACK`.
  * `connect_ex()` returning `0` means `SYN-ACK` was received (**OPEN**).
  * Non-zero error codes (e.g., `10035` / `10061` on Windows) mean **CLOSED** or **FILTERED**.
* **Timeouts (`settimeout`):** Essential so firewalled/silent ports don't freeze the scanner indefinitely.
* **Context Managers (`with`):** Automatically closes sockets even when exceptions occur, preventing resource leaks.
* **Exception Handling (`try...except`):** Catches `socket.gaierror` on unresolvable hostnames so the scanner degrades gracefully instead of crashing.

### 2. Practical Exercises Completed
* Audited local listening ports with `netstat -an`.
* Ran live Python `socket` probes against `127.0.0.1:445` and `127.0.0.1:59999`.
* Triggered a `socket.gaierror` traceback and resolved it in `phantom/modules/recon/prober.py`.
