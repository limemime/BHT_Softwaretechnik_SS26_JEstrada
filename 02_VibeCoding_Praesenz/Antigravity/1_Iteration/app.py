# We import the standard tkinter module to create our
# application window. This module provides all the basic graphical
# components needed.
import tkinter as tk

# We import the ttk module for modern themed widgets
# and messagebox for popups. These tools are essential for
# a clean user interface.
from tkinter import ttk, messagebox

# We import our custom EntropyEngine class along with the
# default setup constants. This connects our background logic to
# the frontend dashboard.
from engine import EntropyEngine, DICTIONARY_FILE, MIN_SLEEP_SECONDS, MAX_SLEEP_SECONDS

# We define the DashboardApp class to manage our graphical
# interface efficiently. This object-oriented approach keeps our code organized
# and highly maintainable.
class DashboardApp:

    # The initialization method runs when the application is first
    # launched. It configures the main window and creates the
    # required elements.
    def __init__(self, root):
    
        # We store the main root window as a specific
        # instance variable. This allows us to access it easily
        # from anywhere else.
        self.root = root
        
        # We set the title of the window to something
        # descriptive. This text appears right at the top of
        # the graphical interface.
        self.root.title("Semantic Entropy Dashboard")
        
        # We set the physical dimensions of the window in
        # pixels. This specific size ensures all elements fit perfectly
        # without looking cramped.
        self.root.geometry("350x250")
        
        # We disable resizing for both the width and the
        # height. This locks the window dimensions to preserve our
        # carefully designed layout.
        self.root.resizable(False, False)
        
        # We initialize our custom background engine with the default
        # constants. This prepares the search logic without actually starting
        # the automated loop.
        self.engine = EntropyEngine(DICTIONARY_FILE, MIN_SLEEP_SECONDS, MAX_SLEEP_SECONDS)
        
        # We create a themed frame widget to hold all
        # other elements. This frame adds a nice padding around
        # the entire border.
        self.frame = ttk.Frame(self.root, padding="20")
        
        # We use the grid layout manager to place the
        # frame accurately. This explicitly centers the frame inside the
        # main root window.
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # We create a string variable to track the current
        # engine status. This variable automatically updates any labels connected
        # to it dynamically.
        self.status_var = tk.StringVar(value="Status: Stopped")
        
        # We create a themed label to display the current
        # status text. We style it with bold text and
        # a red color.
        self.status_label = ttk.Label(self.frame, textvariable=self.status_var, font=("Arial", 14, "bold"), foreground="red")
        
        # We place the status label at the very top
        # of the grid. We use column spanning to ensure
        # it stays perfectly centered.
        self.status_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # We create and place a simple text label for
        # the minimum sleep input. This tells the user exactly
        # what the field does.
        ttk.Label(self.frame, text="Min Sleep (sec):").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # We create a string variable to hold the minimum
        # sleep value. It defaults to the initial constant value
        # imported earlier.
        self.min_var = tk.StringVar(value=str(MIN_SLEEP_SECONDS))
        
        # We create an entry widget for typing the minimum
        # sleep time. This input box connects directly to the
        # string variable above.
        self.min_entry = ttk.Entry(self.frame, textvariable=self.min_var, width=10)
        
        # We place the minimum entry widget next to its
        # descriptive label. We align it strictly to the left
        # side for neatness.
        self.min_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # We create and place another label for the maximum
        # sleep input. This ensures the user understands the second
        # input field clearly.
        ttk.Label(self.frame, text="Max Sleep (sec):").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        # We create a string variable for the maximum sleep
        # value. This stores the upper boundary for the random
        # wait calculations.
        self.max_var = tk.StringVar(value=str(MAX_SLEEP_SECONDS))
        
        # We create an entry widget for typing the maximum
        # sleep boundary. The user types numbers into this specific
        # text box directly.
        self.max_entry = ttk.Entry(self.frame, textvariable=self.max_var, width=10)
        
        # We position the maximum entry widget directly under the
        # minimum entry. This maintains a clean and logical vertical
        # alignment column.
        self.max_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # We create a dedicated button to apply the new
        # pacing numbers. Clicking this button triggers the apply_pace function
        # bound to it.
        self.update_btn = ttk.Button(self.frame, text="Apply Pace Changes", command=self.apply_pace)
        
        # We place the update button below the two input
        # fields. It spans both columns to look prominent and
        # easily clickable.
        self.update_btn.grid(row=3, column=0, columnspan=2, pady=(10, 10))
        
        # We create the primary button used to start the
        # background engine. This button executes the start_engine method when
        # pressed by users.
        self.start_btn = ttk.Button(self.frame, text="START ENGINE", command=self.start_engine)
        
        # We place the start button cleanly on the bottom
        # left side. This positioning keeps it separated from the
        # configuration inputs above.
        self.start_btn.grid(row=4, column=0, pady=10, padx=5)
        
        # We create the stop button but disable it initially.
        # It makes no sense to stop an engine that
        # hasn't started yet.
        self.stop_btn = ttk.Button(self.frame, text="STOP ENGINE", command=self.stop_engine, state=tk.DISABLED)
        
        # We place the disabled stop button next to the
        # start button. They sit side by side at the
        # bottom of the window.
        self.stop_btn.grid(row=4, column=1, pady=10, padx=5)

        # We intercept the standard window closing event using the
        # protocol method. This ensures we can safely shut down
        # threads before quitting.
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    # This function handles the logic for applying new pace
    # variables. It reads the inputs and validates them before
    # proceeding.
    def apply_pace(self):
        # We use a try block to handle any unexpected
        # conversion errors safely. The user might type invalid letters
        # instead of numbers.
        try:
            # We attempt to convert the minimum input string into
            # a float. This provides the mathematical value we desperately
            # need later.
            new_min = float(self.min_var.get())
            
            # We also convert the maximum input string into a
            # float number. Both numbers must be valid floats to
            # succeed here.
            new_max = float(self.max_var.get())
            
            # We check if the numbers are negative or logically
            # out of order. The minimum cannot physically be greater
            # than the maximum.
            if new_min < 0 or new_max < 0 or new_min > new_max:
                # If the validation fails, we manually raise a specific
                # value error. This triggers the exception handler down below
                # almost instantly.
                raise ValueError("Invalid range.")
                
            # If everything is valid, we push the new variables
            # to the engine. The background thread will use these
            # boundaries immediately.
            self.engine.update_pace(new_min, new_max)
            
            # We show a friendly popup message confirming the successful
            # change. This gives the user clear feedback that everything
            # worked perfectly.
            messagebox.showinfo("Success", "Pace updated successfully!")
            
        # We catch any value errors that occurred during the
        # conversion process. This prevents the application from crashing due
        # to bad input.
        except ValueError:
            # We display a loud error popup detailing the exact
            # mistake made. This guides the user to fix their
            # specific typing error.
            messagebox.showerror("Error", "Please enter valid positive numbers, and ensure Min <= Max.")

    # This function is responsible for safely starting the background
    # engine thread. It performs final checks before triggering the
    # infinite loop.
    def start_engine(self):
        # We check if the engine has successfully loaded any
        # dictionary words. Starting without words would cause a catastrophic
        # internal failure immediately.
        if not self.engine.words:
            # We show an error popup explaining the missing dictionary
            # file issue. The user must fix this before the
            # application can work.
            messagebox.showerror("Error", "Dictionary file is missing or empty. Cannot start.")
            
            # We immediately exit the function to abort the start
            # process entirely. The engine remains safely stopped in the
            # background.
            return
            
        # We call the start method on the custom engine
        # class instance. This officially launches the background search thread
        # into action.
        self.engine.start()
        
        # We update the dynamic string variable to show it
        # is running. The label on the screen updates automatically
        # and instantly.
        self.status_var.set("Status: Running")
        
        # We dynamically change the status label color to a
        # vibrant green. This gives a strong visual cue that
        # everything is active.
        self.status_label.config(foreground="green")
        
        # We completely disable the start button to prevent multiple
        # simultaneous threads. Clicking it twice could cause serious resource
        # exhaustion issues.
        self.start_btn.config(state=tk.DISABLED)
        
        # We enable the stop button now that it is
        # actually running. The user can safely pause the background
        # tasks anytime.
        self.stop_btn.config(state=tk.NORMAL)

    # This function halts the background engine thread safely and
    # cleanly. It updates the graphical interface to reflect the
    # stopped state.
    def stop_engine(self):
        # We command the custom engine class to stop its
        # background thread. It will finish the current wait cycle
        # and terminate.
        self.engine.stop()
        
        # We update the dynamic string variable back to the
        # stopped text. This informs the user that searches have
        # officially halted.
        self.status_var.set("Status: Stopped")
        
        # We switch the status label color back to a
        # warning red. This visually confirms the system is no
        # longer active.
        self.status_label.config(foreground="red")
        
        # We re-enable the start button so the user can
        # resume later. The system is ready to launch another
        # thread anytime.
        self.start_btn.config(state=tk.NORMAL)
        
        # We disable the stop button since the engine is
        # already paused. You cannot stop a system that is
        # completely stationary.
        self.stop_btn.config(state=tk.DISABLED)

    # This method runs automatically whenever the user clicks the
    # window close button. It ensures the program shuts down
    # gracefully without hanging.
    def on_closing(self):
        # We check if the background engine thread is currently
        # running actively. If it is, we need to shut
        # it down safely.
        if self.engine.running:
            # We send the official stop signal to the background
            # engine thread. This prevents phantom processes from lingering in
            # the background.
            self.engine.stop()
            
        # We permanently destroy the main root window and end
        # the program. The entire application completely exits after this
        # specific command executes.
        self.root.destroy()

# This conditional block ensures the code only runs when
# executed directly. It prevents accidental launches if imported as
# a module elsewhere.
if __name__ == "__main__":

    # We initialize the core graphical interface toolkit using the
    # Tk class. This creates the foundational root window for
    # our desktop application.
    root = tk.Tk()
    
    # We pass the root window into our custom DashboardApp
    # class instance. This wires up all the graphical widgets
    # and internal logic.
    app = DashboardApp(root)
    
    # We trigger the main infinite event loop of the
    # tkinter application. This keeps the window open and responsive
    # to user interactions.
    root.mainloop()
