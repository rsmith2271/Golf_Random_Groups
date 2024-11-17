import tkinter as tk
from tkinter import ttk, messagebox
import random
from name_random_generator import generate_name_pairs, generate_name_trios, generate_name_quads

class GolfRandomizerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Golf Buddies Random Group Generator")
        self.geometry("600x700")
        
        # List to store names
        self.name_list = []
        
        # Create and pack widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Name Entry Section
        name_frame = ttk.LabelFrame(self, text="Add Players", padding="10")
        name_frame.pack(fill="x", padx=10, pady=5)
        
        self.name_entry = ttk.Entry(name_frame)
        self.name_entry.pack(side="left", padx=5)
        
        add_button = ttk.Button(name_frame, text="Add Player", command=self.add_name)
        add_button.pack(side="left", padx=5)
        
        # Names List Section
        list_frame = ttk.LabelFrame(self, text="Current Players", padding="10")
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.names_listbox = tk.Listbox(list_frame)
        self.names_listbox.pack(fill="both", expand=True)
        
        remove_button = ttk.Button(list_frame, text="Remove Selected", command=self.remove_name)
        remove_button.pack(pady=5)
        
        # Group Type Selection
        group_frame = ttk.LabelFrame(self, text="Select Group Type", padding="10")
        group_frame.pack(fill="x", padx=10, pady=5)
        
        self.group_type = tk.StringVar(value="pairs")
        ttk.Radiobutton(group_frame, text="Pairs", value="pairs", variable=self.group_type).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="Trios", value="trios", variable=self.group_type).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="Quads", value="quads", variable=self.group_type).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="7 Players (3-2-2)", value="seven", variable=self.group_type).pack(side="left", padx=10)
        
        # Generate Button
        generate_button = ttk.Button(self, text="Generate Groups", command=self.generate_groups)
        generate_button.pack(pady=10)
        
        # Results Section
        results_frame = ttk.LabelFrame(self, text="Generated Groups", padding="10")
        results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.results_text = tk.Text(results_frame, height=8)
        self.results_text.pack(fill="both", expand=True)
        
    def add_name(self):
        name = self.name_entry.get().strip()
        if name:
            self.name_list.append(name)
            self.names_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
        
    def remove_name(self):
        selection = self.names_listbox.curselection()
        if selection:
            index = selection[0]
            name = self.names_listbox.get(index)
            self.name_list.remove(name)
            self.names_listbox.delete(index)
            
    def generate_groups(self):
        if not self.name_list:
            messagebox.showwarning("Warning", "Please add some players first!")
            return
            
        group_type = self.group_type.get()
        self.results_text.delete(1.0, tk.END)
        
        if group_type == "pairs":
            if len(self.name_list) < 2:
                messagebox.showwarning("Warning", "Need at least 2 players for pairs!")
                return
            pairs = generate_name_pairs(self.name_list.copy())
            self.display_groups(pairs, 2)
            
        elif group_type == "trios":
            if len(self.name_list) < 3:
                messagebox.showwarning("Warning", "Need at least 3 players for trios!")
                return
            trios = generate_name_trios(self.name_list.copy())
            self.display_groups(trios, 3)
            
        elif group_type == "quads":
            if len(self.name_list) < 4:
                messagebox.showwarning("Warning", "Need at least 4 players for quads!")
                return
            quads = generate_name_quads(self.name_list.copy())
            self.display_groups(quads, 4)
            
        elif group_type == "seven":
            if len(self.name_list) != 7:
                messagebox.showwarning("Warning", "Need exactly 7 players for this option!")
                return
            names = self.name_list.copy()
            random.shuffle(names)
            self.results_text.insert(tk.END, f"Group 1 (3): {' - '.join(names[:3])}\n")
            self.results_text.insert(tk.END, f"Group 2 (2): {' - '.join(names[3:5])}\n")
            self.results_text.insert(tk.END, f"Group 3 (2): {' - '.join(names[5:])}\n")
    
    def display_groups(self, groups, group_size):
        names = self.name_list.copy()
        for i, group in enumerate(groups, 1):
            self.results_text.insert(tk.END, f"Group {i}: {' - '.join(group)}\n")
            for name in group:
                if name in names:
                    names.remove(name)
        
        # Handle leftover players
        if names:
            self.results_text.insert(tk.END, f"\nLeftover players: {' - '.join(names)}\n")

if __name__ == "__main__":
    app = GolfRandomizerGUI()
    app.mainloop()
