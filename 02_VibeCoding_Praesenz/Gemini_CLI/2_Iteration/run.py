import sys
from app import app
from search_loop import search_loop

if __name__ == '__main__':
    print("==================================================")
    print("      Semantic Entropy Engine Running             ")
    print("  Dashboard available at: http://127.0.0.1:5000   ")
    print("==================================================")
    try:
        app.run(debug=False, port=5000, host="127.0.0.1")
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        print("Stopping search loop background threads...")
        search_loop.stop()
        print("Shutdown complete. Goodbye!")
        sys.exit(0)
