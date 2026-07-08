import tkinter as tk
from tkinter import messagebox
import time
import logging

class DashboardGUI:
    """A premium, Dark Mode desktop interface for controlling the Entropy Engine."""
    
    def __init__(self, root, engine_starter):
        self.root = root
        self.engine = engine_starter
        
        # Configure root window properties
        self.root.title("Semantic Entropy Dashboard")
        self.root.geometry("620x520")
        self.root.configure(bg="#121218")
        self.root.resizable(False, False)
        
        # Track statistics
        self.search_count = 0
        self.start_time = None
        self.elapsed_time_str = "00:00:00"
        
        # Custom Color Palette
        self.colors = {
            "bg_main": "#121218",       # Deep black/blue background
            "bg_card": "#1E1E2A",       # Dark gray/blue cards
            "bg_input": "#2A2A3C",      # Lighter slate for inputs
            "fg_primary": "#E2E2EC",    # Soft white for primary text
            "fg_secondary": "#8A8A9E",  # Muted silver for labels
            "accent": "#00ADB5",        # Teal accent color
            "green": "#4E9F3D",         # Status Active
            "red": "#D83A56",           # Status Stopped
            "blue": "#1976D2",          # Secondary action
            "btn_default": "#3E3E56"    # Default button slate
        }
        
        # Setup modern Tkinter GUI layout
        self._create_widgets()
        self._apply_initial_config()
        self._update_timer_loop()
        
        # Register GUI as listener for engine searches
        self.engine.register_on_search_callback(self.safe_on_search_executed)
        
        # Intercept close window protocol to handle thread termination
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _create_widgets(self):
        # 1. Header Canvas / Frame
        header_frame = tk.Frame(self.root, bg=self.colors["bg_main"], height=60)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="SEMANTIC ENTROPY ENGINE", 
            font=("Helvetica", 16, "bold"), 
            fg=self.colors["accent"], 
            bg=self.colors["bg_main"]
        )
        title_label.pack(side=tk.LEFT, pady=10)
        
        # Active Status Indicator
        self.status_var = tk.StringVar(value="● STOPPED")
        self.status_label = tk.Label(
            header_frame, 
            textvariable=self.status_var, 
            font=("Helvetica", 11, "bold"), 
            fg=self.colors["red"], 
            bg=self.colors["bg_main"]
        )
        self.status_label.pack(side=tk.RIGHT, pady=15)

        # 2. Main Dashboard Layout (Split left/right)
        body_frame = tk.Frame(self.root, bg=self.colors["bg_main"])
        body_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        # --- LEFT SIDE: CONFIGURATION ---
        left_frame = tk.Frame(body_frame, bg=self.colors["bg_card"], bd=0)
        left_frame.place(relx=0.0, rely=0.0, relwidth=0.48, relheight=0.98)
        
        # Config Title
        tk.Label(
            left_frame, 
            text="ENGINE SETTINGS", 
            font=("Helvetica", 10, "bold"), 
            fg=self.colors["accent"], 
            bg=self.colors["bg_card"]
        ).pack(anchor=tk.W, padx=15, pady=(15, 10))
        
        # Min Sleep Entry
        tk.Label(
            left_frame, 
            text="Minimum Pace (seconds):", 
            font=("Helvetica", 9), 
            fg=self.colors["fg_secondary"], 
            bg=self.colors["bg_card"]
        ).pack(anchor=tk.W, padx=15)
        self.min_var = tk.StringVar()
        self.min_entry = tk.Entry(
            left_frame, 
            textvariable=self.min_var, 
            bg=self.colors["bg_input"], 
            fg=self.colors["fg_primary"], 
            insertbackground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 10)
        )
        self.min_entry.pack(fill=tk.X, padx=15, pady=(2, 10))
        
        # Max Sleep Entry
        tk.Label(
            left_frame, 
            text="Maximum Pace (seconds):", 
            font=("Helvetica", 9), 
            fg=self.colors["fg_secondary"], 
            bg=self.colors["bg_card"]
        ).pack(anchor=tk.W, padx=15)
        self.max_var = tk.StringVar()
        self.max_entry = tk.Entry(
            left_frame, 
            textvariable=self.max_var, 
            bg=self.colors["bg_input"], 
            fg=self.colors["fg_primary"], 
            insertbackground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 10)
        )
        self.max_entry.pack(fill=tk.X, padx=15, pady=(2, 10))
        
        # Search Engine Dropdown
        tk.Label(
            left_frame, 
            text="Target Search Engine:", 
            font=("Helvetica", 9), 
            fg=self.colors["fg_secondary"], 
            bg=self.colors["bg_card"]
        ).pack(anchor=tk.W, padx=15)
        
        from config import SEARCH_ENGINES
        self.engine_options = list(SEARCH_ENGINES.keys())
        self.selected_engine_var = tk.StringVar()
        
        self.engine_dropdown = tk.OptionMenu(
            left_frame, 
            self.selected_engine_var, 
            *self.engine_options
        )
        self.engine_dropdown.config(
            bg=self.colors["bg_input"], 
            fg=self.colors["fg_primary"], 
            activebackground=self.colors["bg_input"], 
            activeforeground=self.colors["fg_primary"],
            relief=tk.FLAT,
            font=("Helvetica", 9),
            highlightthickness=0,
            bd=0
        )
        self.engine_dropdown["menu"].config(
            bg=self.colors["bg_input"], 
            fg=self.colors["fg_primary"],
            activebackground=self.colors["accent"],
            activeforeground=self.colors["fg_primary"],
            font=("Helvetica", 9)
        )
        self.engine_dropdown.pack(fill=tk.X, padx=15, pady=(2, 15))
        
        # Apply Configuration Button
        self.apply_btn = tk.Button(
            left_frame, 
            text="Apply Settings", 
            command=self.apply_config, 
            bg=self.colors["btn_default"], 
            fg=self.colors["fg_primary"], 
            activebackground=self.colors["accent"], 
            activeforeground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 9, "bold"),
            cursor="hand2"
        )
        self.apply_btn.pack(fill=tk.X, padx=15, pady=5)
        
        # --- RIGHT SIDE: HISTORY & ACTIVITY LOGS ---
        right_frame = tk.Frame(body_frame, bg=self.colors["bg_card"])
        right_frame.place(relx=0.52, rely=0.0, relwidth=0.48, relheight=0.98)
        
        tk.Label(
            right_frame, 
            text="LIVE ACTIVITY LOG", 
            font=("Helvetica", 10, "bold"), 
            fg=self.colors["accent"], 
            bg=self.colors["bg_card"]
        ).pack(anchor=tk.W, padx=15, pady=(15, 10))
        
        # Log Scrollable Text box
        log_container = tk.Frame(right_frame, bg=self.colors["bg_card"])
        log_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_listbox = tk.Listbox(
            log_container, 
            bg="#111116", 
            fg=self.colors["fg_primary"], 
            selectbackground=self.colors["accent"], 
            relief=tk.FLAT, 
            font=("Consolas", 8),
            bd=0,
            yscrollcommand=scrollbar.set
        )
        self.log_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_listbox.yview)

        # 3. Control Actions (Bottom Panel)
        bottom_frame = tk.Frame(self.root, bg=self.colors["bg_main"], height=90)
        bottom_frame.pack(fill=tk.X, padx=20, pady=(5, 10))
        bottom_frame.pack_propagate(False)
        
        # Start Engine Button
        self.start_btn = tk.Button(
            bottom_frame, 
            text="START ENGINE", 
            command=self.start_engine, 
            bg=self.colors["green"], 
            fg=self.colors["fg_primary"], 
            activebackground="#3e8f2d", 
            activeforeground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 10, "bold"),
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=(0, 5), pady=10)
        
        # Stop Engine Button
        self.stop_btn = tk.Button(
            bottom_frame, 
            text="STOP ENGINE", 
            command=self.stop_engine, 
            bg=self.colors["red"], 
            fg=self.colors["fg_primary"], 
            activebackground="#c52e4a", 
            activeforeground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 10, "bold"),
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.stop_btn.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=5, pady=10)
        
        # Force Single Search Button
        self.force_btn = tk.Button(
            bottom_frame, 
            text="SEARCH NOW", 
            command=self.force_search, 
            bg=self.colors["blue"], 
            fg=self.colors["fg_primary"], 
            activebackground="#1565C0", 
            activeforeground=self.colors["fg_primary"],
            relief=tk.FLAT, 
            font=("Helvetica", 10, "bold"),
            cursor="hand2"
        )
        self.force_btn.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=(5, 0), pady=10)
        
        # 4. Status Bar (Footer)
        footer_frame = tk.Frame(self.root, bg="#0E0E12", height=25)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        self.stats_label = tk.Label(
            footer_frame, 
            text="Searches: 0 | Session Duration: 00:00:00", 
            font=("Consolas", 8, "bold"), 
            fg=self.colors["fg_secondary"], 
            bg="#0E0E12"
        )
        self.stats_label.pack(side=tk.LEFT, padx=15)

    def _apply_initial_config(self):
        """Fills the UI entry fields and dropdown with loaded config settings."""
        self.min_var.set(str(self.engine.config.min_sleep))
        self.max_var.set(str(self.engine.config.max_sleep))
        self.selected_engine_var.set(self.engine.config.search_engine)
        self._log_locally("System loaded. Ready to generate entropy.")

    def _log_locally(self, message):
        """Helper to print to local listbox logs with timestamp."""
        timestamp = time.strftime("[%H:%M:%S]")
        self.log_listbox.insert(tk.END, f"{timestamp} {message}")
        self.log_listbox.yview(tk.END) # Auto scroll to bottom

    def apply_config(self):
        """Validates configuration parameters entered in GUI and saves them."""
        try:
            new_min = float(self.min_var.get())
            new_max = float(self.max_var.get())
            selected_engine = self.selected_engine_var.get()
            
            if new_min < 0 or new_max < 0 or new_min > new_max:
                raise ValueError("Values must be positive and Min <= Max.")
            
            # Apply to config
            self.engine.config.update_pace(new_min, new_max)
            self.engine.config.update_engine(selected_engine)
            
            self._log_locally(f"Config updated: {selected_engine} ({new_min}s - {new_max}s)")
            messagebox.showinfo("Success", "Configuration applied successfully!")
        except ValueError:
            messagebox.showerror(
                "Error", 
                "Please enter valid positive numbers, ensuring Minimum <= Maximum."
            )

    def start_engine(self):
        """Starts the background engine process and updates GUI status."""
        if not self.engine.word_selector.words:
            messagebox.showerror("Error", "Dictionary file contains no search words.")
            return
            
        success = self.engine.start()
        if success:
            self.status_var.set("● RUNNING")
            self.status_label.config(fg=self.colors["green"])
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            
            # Start session timer
            self.start_time = time.time()
            self._log_locally("Entropy search thread successfully started.")

    def stop_engine(self):
        """Stops the background engine process and updates GUI status."""
        success = self.engine.stop()
        if success:
            self.status_var.set("● STOPPED")
            self.status_label.config(fg=self.colors["red"])
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self._log_locally("Entropy thread stopped. Waiting for thread termination.")

    def force_search(self):
        """Commands the engine to perform a single manual search immediately."""
        self.engine.force_single_search()

    def safe_on_search_executed(self, word, engine_name):
        """Thread-safe search callback scheduling UI updates in the main loop."""
        self.root.after(0, self._on_search_executed_main_thread, word, engine_name)

    def _on_search_executed_main_thread(self, word, engine_name):
        """Helper executing on main UI thread to log results and update stats."""
        self.search_count += 1
        self._log_locally(f"{engine_name} -> '{word}'")
        self._update_stats_label()

    def _update_stats_label(self):
        """Updates the text of the footer statistics label."""
        self.stats_label.config(
            text=f"Searches: {self.search_count} | Session Duration: {self.elapsed_time_str}"
        )

    def _update_timer_loop(self):
        """Dynamic timer loop updating running duration stats every second."""
        if self.engine.running and self.start_time is not None:
            elapsed = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.elapsed_time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self._update_stats_label()
            
        # Reschedule timer after 1 second (1000 ms)
        self.root.after(1000, self._update_timer_loop)

    def on_closing(self):
        """Shuts down the background search thread safely when dashboard closes."""
        if self.engine.running:
            self.engine.stop()
        self.root.destroy()
