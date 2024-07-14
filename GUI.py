import tkinter as tk
from tkinter import ttk
from network_sniff import scan_ip
from mitm import mitm_attack
import threading, subprocess

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Zenmap-like GUI")
        self.geometry("800x600")

        # Create the main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Top frame for command entry
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        command_label = ttk.Label(top_frame, text="Command:")
        command_label.pack(side=tk.LEFT, padx=(10, 5), pady=10)

        self.command_entry = ttk.Entry(top_frame)
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=10)

        run_button = ttk.Button(top_frame, text="Run", command=self.run_command)
        run_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        # Left frame for scan profiles and targets
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 5), pady=10)

        interface_label = ttk.Label(left_frame, text="interface")
        interface_label.pack(anchor=tk.W)

        self.interface_combo = ttk.Combobox(left_frame, values=[])
        self.interface_combo.pack(fill=tk.X, pady=(0, 10))

        scanip_button = ttk.Button(left_frame, text="Scan IP", command=self.scanIP)
        scanip_button.pack(pady=(10, 10))

        server_label = ttk.Label(left_frame, text="Server:")
        server_label.pack(anchor=tk.W)

        self.server_combo = ttk.Combobox(left_frame, values=[])
        self.server_combo.pack(fill=tk.X, pady=(0, 10))

        client_label = ttk.Label(left_frame, text="Client:")
        client_label.pack(anchor=tk.W)

        self.client_combo = ttk.Combobox(left_frame, values=[])
        self.client_combo.pack(fill=tk.X, pady=(0, 10))

        mitm_button = ttk.Button(left_frame, text="Start Mitm", command=self.start_mitm)
        mitm_button.pack(pady=(10, 10))

        # Right frame for scan output
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 10), pady=10)

        output_label = ttk.Label(right_frame, text="Output:")
        output_label.pack(anchor=tk.W)

        self.output_text = tk.Text(right_frame, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Status bar at the bottom
        status_frame = ttk.Frame(self)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_label = ttk.Label(status_frame, text="Ready")
        self.status_label.pack(side=tk.LEFT, padx=(10, 0), pady=5)

    def run_command(self):
        command = self.command_entry.get()
        self.output_text.insert(tk.END, f"Running command: {command}\n")
        self.status_label.config(text="Running...")

    def scanIP(self):
        interface = self.interface_combo.get()
        self.status_label.config(text="Scanning...")
        ips = scan_ip(interface.split(" ")[1])
        ips = list(ips.values())
        print(ips)
        self.server_combo["values"] = ips
        self.client_combo["values"] = ips
        #self.output_text.insert(tk.END, f"Running {profile} on {target}\n")

    def start_mitm(self):
        self.server = self.server_combo.get()
        self.client = self.client_combo.get()
        self.status_label.config(text="Start Mitm...")
        mitm_attack(self.server,self.client)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
