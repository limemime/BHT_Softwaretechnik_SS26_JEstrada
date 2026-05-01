# Specification & Validation: Iteration 2
## Automation & Realism

---

## Overview
Iteration 2 enhances the engine with Selenium-based browser automation to simulate realistic human behavior. This increases the difficulty of detection by search engines and improves the quality of profile poisoning.

---

## Feature Specifications

### 2.1 Selenium Integration
| ID | Feature | Description |
| :--- | :--- | :--- |
| SEL-01 | WebDriver Initialization | Auto-detect and load Chrome/Firefox driver |
| SEL-02 | Headless Option | Optional headless mode for background operation |
| SEL-03 | Browser Profile | Support for persistent browser profiles (cookies, history) |
| SEL-04 | Driver Management | Automatic driver version matching with installed browser |

### 2.2 Behavioral Simulation
| ID | Feature | Description |
| :--- | :--- | :--- |
| BEH-01 | Keystroke Simulation | Type query character-by-character with random delays |
| BEH-02 | Mouse Movement | Simulate cursor movement to search box and submit button |
| BEH-03 | Scroll Actions | Random scrolling on results page before closing tab |
| BEH-04 | Page Load Wait | Wait for page elements to fully load before interaction |

### 2.3 Enhanced Timing System
| ID | Feature | Description |
| :--- | :--- | :--- |
| TIM-05 | Dynamic Delay Adjustment | User can modify min/max delays via GUI sliders |
| TIM-06 | Typing Speed Variation | Randomize keystroke speed (50-300ms per character) |
| TIM-07 | Session Duration | Optional limit on total session runtime |
| TIM-08 | Break Periods | Simulate user breaks (longer pauses after N searches) |

### 2.4 Anti-Detection Measures
| ID | Feature | Description |
| :--- | :--- | :--- |
| ANT-01 | User-Agent Rotation | Randomize browser User-Agent string per session |
| ANT-02 | Window Size Variation | Randomize browser window dimensions |
| ANT-03 | Cookie Consent Handling | Auto-dismiss common cookie consent pop-ups |
| ANT-04 | CAPTCHA Detection | Detect CAPTCHA pages and pause/notify user |

### 2.5 GUI Enhancements
| ID | Feature | Description |
| :--- | :--- | :--- |
| GUI-05 | Delay Sliders | Visual controls for min/max delay configuration |
| GUI-06 | Search Engine Selector | Dropdown to choose target search engine |
| GUI-07 | Advanced Settings Panel | Toggle for headless mode, User-Agent rotation, etc. |
| GUI-08 | Search Counter | Display total searches executed in current session |

---

## Validation Criteria

### SEL-01: WebDriver Initialization
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Chrome installed | Selenium launches Chrome successfully | ☐ |
| Firefox installed | Selenium launches Firefox successfully | ☐ |
| No browser found | Clear error message with installation guide link | ☐ |

### BEH-01: Keystroke Simulation
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Short query (<10 chars) | All characters typed, visible in search box | ☐ |
| Long query (>50 chars) | All characters typed, no truncation | ☐ |
| Special characters | Characters typed correctly (e.g., `@`, `#`, `$`) | ☐ |

### BEH-02: Mouse Movement
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Track mouse events | Cursor moves visibly to search box | ☐ |
| Click submit | Search executes after click action | ☐ |

### ANT-01: User-Agent Rotation
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Run 10 sessions | At least 3 different User-Agent strings observed | ☐ |
| Consistency within session | Same User-Agent persists for entire session | ☐ |

### ANT-03: Cookie Consent Handling
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Google search page | Cookie banner dismissed automatically | ☐ |
| Bing search page | Cookie banner dismissed automatically | ☐ |
| No banner present | Page proceeds without interference | ☐ |

### TIM-05: Dynamic Delay Adjustment
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Adjust slider during run | New delay values apply to next interval | ☐ |
| Set invalid range (min > max) | GUI rejects input, shows warning | ☐ |

### GUI-08: Search Counter
| Test Case | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Complete 10 searches | Counter increments to exactly 10 | ☐ |
| Restart application | Counter resets to 0 | ☐ |

---

## Technical Requirements
- **Python Version:** 3.9 or higher
- **Dependencies:** `selenium>=4.0`, `webdriver-manager`, `customtkinter`
- **Browser Requirements:** Chrome 90+ or Firefox 88+
- **Memory Footprint:** < 300 MB RAM during operation (with browser)

## Success Metrics
| Metric | Target |
| :--- | :--- |
| Keystroke simulation accuracy | 100% characters typed correctly |
| CAPTCHA detection rate | > 95% of CAPTCHA pages identified |
| Cookie dismissal success | > 90% of common consent banners handled |
| Browser crash rate | < 1% during 100-search stress test |

## Known Limitations (Iter 2)
- Does not fully evade advanced fingerprinting (Canvas, WebGL)
- Limited to Chrome/Firefox browsers
- No IP rotation (single connection per session)
- CAPTCHA handling is detection-only, not solving
