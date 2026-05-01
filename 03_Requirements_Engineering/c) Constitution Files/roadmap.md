# Roadmap: Identity Entropy Engine

## Overview
The development of the Identity Entropy Engine follows a three-phase lifecycle. Each iteration builds upon the previous one, introducing greater complexity in automation, evasion, and user interaction.

---

## Iteration 1: Foundation & Basic Execution
**Objective:** Establish the core logic for random query generation and basic browser interaction.

### Key Deliverables
1.  **Data Layer:**
    - Implementation of a static JSON dictionary containing single keywords and multi-word phrases.
    - Logic for random selection from this dictionary.
2.  **Execution Layer:**
    - Basic script to launch the default system browser.
    - Opening a new tab and navigating to the search engine with the query pre-filled in the URL bar.
3.  **Timing Logic:**
    - Random delay generator (2 minutes to 2 hours).
    - Simple loop to repeat the process.
4.  **Interface:**
    - Minimalist GUI (using `tkinter` or `CustomTkinter`).
    - **Features:** Start/Stop button, basic status log.

### Success Criteria
- Application starts and stops cleanly.
- Generates random queries from the JSON file.
- Opens browser tabs successfully at random intervals.

---

## Iteration 2: Automation & Realism
**Objective:** Enhance evasion capabilities by simulating realistic human browser behavior.

### Key Deliverables
1.  **Automation Upgrade:**
    - Integration of **Selenium WebDriver**.
    - Replacement of simple URL launching with programmatic browser control.
2.  **Behavioral Simulation:**
    - Simulated keystrokes (typing the query character-by-character).
    - Randomized mouse movements or scroll actions (optional).
    - Handling of pop-ups or cookie consent banners to prevent blocking.
3.  **Configuration:**
    - GUI enhancements to allow users to adjust the minimum/maximum delay dynamically.
    - Selection of target search engine (Google, DuckDuckGo, etc.).

### Success Criteria
- Browser interactions appear indistinguishable from manual human use.
- No detection as a basic automation script by simple heuristics.
- User can configure timing parameters via the GUI.

---

## Iteration 3: Optimization & Analytics
**Objective:** Refine the system with resource monitoring, advanced metrics, and resilience.

### Key Deliverables
1.  **Metrics Dashboard:**
    - Real-time display of resource usage (CPU, Memory).
    - Counter for total searches executed.
    - Log of generated queries for audit purposes.
2.  **Resilience:**
    - Error handling for network failures or browser crashes.
    - Auto-recovery mechanisms to resume operation after interruptions.
3.  **Advanced Evasion:**
    - Implementation of "sleep cycles" to mimic user inactivity during night hours.
    - Randomization of User-Agent strings to vary browser fingerprints.

### Success Criteria
- Stable long-term operation without memory leaks.
- Comprehensive visibility into engine performance and activity.
- Robust handling of edge cases and errors.
