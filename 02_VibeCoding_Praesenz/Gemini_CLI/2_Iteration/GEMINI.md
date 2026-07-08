# Semantic Entropy Engine
A minimalistic local application designed to influence browser cookie profiles and social media tracking by performing randomized, periodic web searches.

## Project Overview
The app consists of a background engine that reads keywords from a dictionary and opens them in the system's default browser at varying intervals (7-30 seconds). This activity creates a "semantic noise" profile in local browser cookies.

- **Dashboard**: A Flask-based web interface (http://127.0.0.1:5000) to control the engine.
- **Engine**: A Python background thread that manages the search loop.

## Building and Running
1. **Install Dependencies**:
   ```bash
   pip install flask
   ```
2. **Run the App**:
   ```bash
   python run.py
   ```
3. **Access Dashboard**: Open `http://127.0.0.1:5000` in your browser.

## Development Conventions
- Use Python 3.x.
- Keep UI minimalistic and modern.
- Ensure randomized pacing (7-30s) to avoid bot detection patterns.
