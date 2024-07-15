import tkinter as tk
from tkinter import ttk
from network_sniff import scan_ip
from mitm import mitm_attack
import threading, subprocess
from ModbusClient import ModbusClientClass, start_blank

class GUI(tk.Tk):
    def __init__(self):
        self.modbusclient = None

        super().__init__()

        self.title("Zenmap-like GUI")
        self.geometry("800x600")

        # Create the main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Top frame for command entry
        top_frame = ttk.Frame(self.main_frame)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        bound_label = ttk.Label(top_frame, text="Bound:")
        bound_label.pack(side=tk.LEFT, padx=(10, 5), pady=10)

        self.start_bound_entry = ttk.Entry(top_frame)
        self.start_bound_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=10)

        to_label = ttk.Label(top_frame, text="~")
        to_label.pack(side=tk.LEFT, padx=(5, 10), pady=10)

        self.end_bound_entry = ttk.Entry(top_frame)
        self.end_bound_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=10)

        read_button = ttk.Button(top_frame, text="Read Coils", command=lambda: self.read(True))
        read_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        read_button = ttk.Button(top_frame, text="Read Regs", command=lambda: self.read(False))
        read_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        write_button = ttk.Button(top_frame, text="Write Coils", command=lambda: self.write(True))
        write_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        write_button = ttk.Button(top_frame, text="Write Regs", command=lambda: self.write(False))
        write_button.pack(side=tk.LEFT, padx=(0, 10), pady=10)

        # Left frame for scan profiles and targets
        left_frame = ttk.Frame(self.main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 5), pady=10)

        interface_label = ttk.Label(left_frame, text="interface")
        interface_label.pack(anchor=tk.W)

        self.interface_combo = ttk.Combobox(left_frame, values=[])
        self.interface_combo.pack(fill=tk.X, pady=(0, 10))

        scanip_button = ttk.Button(left_frame, text="Scan IP", command=lambda: threading.Thread(target=self.scanIP).start())
        scanip_button.pack(pady=(10, 10))

        server_label = ttk.Label(left_frame, text="Server:")
        server_label.pack(anchor=tk.W)

        self.server_combo = ttk.Combobox(left_frame, values=[])
        self.server_combo.pack(fill=tk.X, pady=(0, 10))

        client_label = ttk.Label(left_frame, text="Client:")
        client_label.pack(anchor=tk.W)

        self.client_combo = ttk.Combobox(left_frame, values=[])
        self.client_combo.pack(fill=tk.X, pady=(0, 10))

        self.mitm_thread = threading.Thread(target=self.start_mitm)
        mitm_button = ttk.Button(left_frame, text="Start Mitm", command=self.mitm_thread.start)
        mitm_button.pack(pady=(10, 10))

        self.blank_thread = threading.Thread(target=start_blank)
        blank_button = ttk.Button(left_frame, text="Start Blank", command=self.blank_thread.start)
        blank_button.pack(pady=(10, 10))

        # Right frame for scan output
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 10), pady=10)

        self.id_labels = [] 
        self.value_entry = []

        #output_label = ttk.Label(right_frame, text="Output:")
        #output_label.pack(anchor=tk.W)

        #self.output_text = tk.Text(right_frame, wrap=tk.WORD)
        #self.output_text.pack(fill=tk.BOTH, expand=True)

        # Status bar at the bottom
        status_frame = ttk.Frame(self)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_label = ttk.Label(status_frame, text="Ready")
        self.status_label.pack(side=tk.LEFT, padx=(10, 0), pady=5)

    def read(self, ty):
        if self.modbusclient is None:
            self.server = self.server_combo.get()
            self.modbusclient = ModbusClientClass(self.server)
        for widget in self.right_frame.winfo_children():
            widget.destroy()
    
        self.bound = [int(self.start_bound_entry.get()), int(self.end_bound_entry.get())+1]
        self.id_labels = []
        if ty:
            self.tmp_value_entry = self.modbusclient.read_coils(self.bound)
        else:
            self.tmp_value_entry = self.modbusclient.read_regs(self.bound)
        self.value_entry = []
        rightF = ttk.Frame(self.right_frame)
        rightF.pack(fill=tk.X)
        j = 0
        for i in range(0, self.bound[1]-self.bound[0]):
            self.id_labels.append(ttk.Label(rightF, text=f"{i+self.bound[0]}"))
            self.value_entry.append(ttk.Entry(rightF))
            if self.tmp_value_entry is None:
                self.value_entry[i].insert(0, "0")
            else:
                self.value_entry[i].insert(0, str(bool(self.tmp_value_entry[i])))
            self.id_labels[i].pack(side=tk.LEFT, padx=(10, 5), pady=10)
            self.value_entry[i].pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=10)
            if j == 3:
                j = 0
                rightF = ttk.Frame(self.right_frame)
                rightF.pack(fill=tk.X)
            else:
                j += 1

    def write(self, ty):
        if self.tmp_value_entry is None or self.modbusclient is None:
            return
        for i in range(len(self.value_entry)):
            if ty:
                if self.value_entry[i].get() == "True" or self.value_entry[i].get() == "1":
                    value = bool(1)
                else:
                    value = bool(0)
                if self.tmp_value_entry[i] != value:
                    self.tmp_value_entry[i] = value
                    self.modbusclient.write_coil(i+self.bound[0], value)
            else:
                value = int(self.value_entry[i].get())
                if self.tmp_value_entry[i] != value:
                    self.tmp_value_entry[i] = value
                    self.modbusclient.write_reg(i+self.bound[0], value)

    def scanIP(self):
        interface = self.interface_combo.get()
        self.status_label.config(text="Scanning...")
        ips = scan_ip(interface.split(" ")[1])
        ips = list(ips.values())
        print(ips)
        self.server_combo["values"] = ips
        self.client_combo["values"] = ips
        #self.output_text.insert(tk.END, f"Running {profile} on {target}\n")
        self.status_label.config(text="Ready")

    def start_mitm(self):
        interface = self.interface_combo.get().split(" ")[0]
        self.server = self.server_combo.get()
        self.client = self.client_combo.get()
        self.status_label.config(text="Start Mitm...")
        mitm_attack(self.server,self.client, interface)
        self.status_label.config(text="Ready")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
