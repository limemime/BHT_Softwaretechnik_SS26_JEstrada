import tkinter as tk
import logging
from engine_starter import EngineStarter
from gui import DashboardGUI

# We configure standard logging output for user visibility in console.
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    """Initializes config, instantiates the engine, boots the GUI, and runs the application."""
    logging.info("Initializing Semantic Entropy Application...")
    
    # 1. Create the root Tkinter application window
    root = tk.Tk()
    
    # 2. Instantiate our background engine coordinator.
    # It automatically handles config loading and word selector setup.
    engine = EngineStarter()
    
    # 3. Instantiate the GUI Dashboard, wiring it with the controller.
    # This separates the layout/rendering completely from application startup.
    app = DashboardGUI(root, engine)
    
    # 4. Run the Tkinter main event loop.
    logging.info("Launching GUI main event loop...")
    root.mainloop()

if __name__ == "__main__":
    main()
