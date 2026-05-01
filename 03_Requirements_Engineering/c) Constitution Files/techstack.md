# Technology Stack: Identity Entropy Engine

## Core Language
- **Python 3.x**
  - Chosen for its extensive ecosystem of automation libraries, ease of scripting, and robust JSON handling.

## Data Management
- **Format:** JSON
  - Used for the static keyword dictionary.
  - Allows for structured storage of terms and potential future metadata (e.g., categories, weights).
- **Library:** `json` (Standard Library)
  - Native support for parsing and loading the keyword database.

## Automation & Browser Control
- **Iteration 1:** `subprocess` & `webbrowser` (Standard Library)
  - Used for launching the default system browser and opening new tabs with pre-filled URLs.
- **Iteration 2 & 3:** `Selenium`
  - **Driver:** `ChromeDriver` or `GeckoDriver`.
  - **Purpose:** Programmatic control of the browser, simulating keystrokes, clicks, and navigation.
  - **Benefit:** Higher fidelity in mimicking human behavior compared to simple URL launching.

## User Interface (GUI)
- **Library:** `CustomTkinter`
  - **Reasoning:** Provides a modern, clean look out-of-the-box compared to standard `tkinter`, while remaining lightweight and easy to implement for a dashboard.
  - **Components:** Buttons (Start/Stop), Sliders (Delay adjustment), Labels (Metrics display), Text Box (Logs).

## System Monitoring (Iteration 3)
- **Library:** `psutil`
  - **Purpose:** Retrieve real-time system resource usage (CPU %, Memory %).
  - **Integration:** Displayed on the GUI dashboard for user visibility.

## Dependencies Summary
| Library | Version | Purpose |
| :--- | :--- | :--- |
| `python` | 3.9+ | Core Runtime |
| `customtkinter` | Latest | Graphical User Interface |
| `selenium` | 4.x | Browser Automation (Iter 2+) |
| `psutil` | Latest | System Resource Monitoring (Iter 3) |
| `json` | N/A | Data Parsing (Standard Lib) |

## Development Environment
- **IDE:** VS Code or PyCharm
- **Version Control:** Git
- **Package Management:** `pip` / `requirements.txt`
