import random
import tkinter as tk
from tkinter import ttk, messagebox

def generate_name_pairs(names):
    pairs = []
    random.shuffle(names)
    for i in range(0, len(names), 2):
        if i + 1 < len(names):
            pairs.append((names[i], names[i + 1]))
    return pairs

def generate_name_trios(names):
    trios = []
    random.shuffle(names)
    for i in range(0, len(names), 3):
        if i + 2 < len(names):
            trios.append((names[i], names[i + 1], names[i + 2]))
    return trios

def generate_name_quads(names):
    quads = []
    random.shuffle(names)
    for i in range(0, len(names), 4):
        if i + 3 < len(names):
            quads.append((names[i], names[i + 1], names[i + 2], names[i + 3]))
    return quads

class GolfRandomizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Golf Random Group Generator")
        self.geometry("600x500")
        self.configure(padx=20, pady=20)

        self.name_list = []
        
        # Create and set up the GUI elements
        self.setup_gui()

    def setup_gui(self):
        # Title
        title_label = ttk.Label(self, text="Golf Random Group Generator", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 20))

        # Name input frame
        input_frame = ttk.Frame(self)
        input_frame.pack(fill="x", pady=(0, 10))

        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.pack(side="left", padx=(0, 10), expand=True, fill="x")
        self.name_entry.bind("<Return>", lambda e: self.add_name())

        add_button = ttk.Button(input_frame, text="Add Name", command=self.add_name)
        add_button.pack(side="right")

        # Names list
        list_frame = ttk.LabelFrame(self, text="Added Names")
        list_frame.pack(fill="both", expand=True, pady=(0, 20))

        self.names_listbox = tk.Listbox(list_frame)
        self.names_listbox.pack(fill="both", expand=True, padx=5, pady=5)

        # Remove name button
        remove_button = ttk.Button(self, text="Remove Selected Name", command=self.remove_name)
        remove_button.pack(pady=(0, 20))

        # Group selection
        group_frame = ttk.LabelFrame(self, text="Select Group Type")
        group_frame.pack(fill="x", pady=(0, 20))

        self.group_var = tk.StringVar(value="pairs")
        
        ttk.Radiobutton(group_frame, text="Pairs", value="pairs", variable=self.group_var).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="Trios", value="trios", variable=self.group_var).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="Quads", value="quads", variable=self.group_var).pack(side="left", padx=10)
        ttk.Radiobutton(group_frame, text="7 Players", value="seven", variable=self.group_var).pack(side="left", padx=10)

        # Generate button
        generate_button = ttk.Button(self, text="Generate Groups", command=self.generate_groups)
        generate_button.pack(pady=(0, 20))

        # Results
        self.result_text = tk.Text(self, height=6, wrap="word")
        self.result_text.pack(fill="x")

    def add_name(self):
        name = self.name_entry.get().strip()
        if name:
            self.name_list.append(name)
            self.names_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
        self.name_entry.focus()

    def remove_name(self):
        selection = self.names_listbox.curselection()
        if selection:
            index = selection[0]
            self.names_listbox.delete(index)
            self.name_list.pop(index)

    def generate_groups(self):
        if not self.name_list:
            messagebox.showwarning("Warning", "Please add some names first!")
            return

        group_type = self.group_var.get()
        min_required = {"pairs": 2, "trios": 3, "quads": 4, "seven": 7}
        
        if group_type == "seven" and len(self.name_list) != 7:
            messagebox.showwarning("Warning", "Exactly 7 players are required for this option!")
            return
        elif len(self.name_list) < min_required[group_type]:
            messagebox.showwarning("Warning", f"At least {min_required[group_type]} players are required!")
            return

        self.result_text.delete(1.0, tk.END)
        if group_type == "pairs":
            self.show_pairs()
        elif group_type == "trios":
            self.show_trios()
        elif group_type == "quads":
            self.show_quads()
        elif group_type == "seven":
            self.show_seven_players()

    def show_pairs(self):
        pairs_result = generate_name_pairs(self.name_list.copy())
        self.result_text.insert(tk.END, "The groups are:\n\n")
        for i, pair in enumerate(pairs_result, 1):
            self.result_text.insert(tk.END, f"{i}. {pair[0]} - {pair[1]}\n")
        
        if len(self.name_list) % 2 == 1:
            leftover = [name for name in self.name_list if not any(name in pair for pair in pairs_result)]
            if leftover:
                self.result_text.insert(tk.END, f"{len(pairs_result) + 1}. {leftover[0]} is on their own\n")

    def show_trios(self):
        trios_result = generate_name_trios(self.name_list.copy())
        self.result_text.insert(tk.END, "The groups are:\n\n")
        for i, trio in enumerate(trios_result, 1):
            self.result_text.insert(tk.END, f"{i}. {trio[0]} - {trio[1]} - {trio[2]}\n")
        
        leftover = [name for name in self.name_list if not any(name in trio for trio in trios_result)]
        if len(leftover) == 1:
            self.result_text.insert(tk.END, f"{len(trios_result) + 1}. {leftover[0]} is on their own\n")
        elif len(leftover) == 2:
            self.result_text.insert(tk.END, f"{len(trios_result) + 1}. {leftover[0]} - {leftover[1]}\n")

    def show_quads(self):
        quads_result = generate_name_quads(self.name_list.copy())
        self.result_text.insert(tk.END, "The groups are:\n\n")
        for i, quad in enumerate(quads_result, 1):
            self.result_text.insert(tk.END, f"{i}. {quad[0]} - {quad[1]} - {quad[2]} - {quad[3]}\n")
        
        leftover = [name for name in self.name_list if not any(name in quad for quad in quads_result)]
        if len(leftover) == 1:
            self.result_text.insert(tk.END, f"{len(quads_result) + 1}. {leftover[0]} is on their own\n")
        elif len(leftover) == 2:
            self.result_text.insert(tk.END, f"{len(quads_result) + 1}. {leftover[0]} - {leftover[1]}\n")
        elif len(leftover) == 3:
            self.result_text.insert(tk.END, f"{len(quads_result) + 1}. {leftover[0]} - {leftover[1]} - {leftover[2]}\n")

    def show_seven_players(self):
        names = self.name_list.copy()
        random.shuffle(names)
        self.result_text.insert(tk.END, "The groups are:\n\n")
        self.result_text.insert(tk.END, f"1. {names[0]} - {names[1]} - {names[2]}\n")
        self.result_text.insert(tk.END, f"2. {names[3]} - {names[4]}\n")
        self.result_text.insert(tk.END, f"3. {names[5]} - {names[6]}\n")

if __name__ == "__main__":
    app = GolfRandomizer()
    app.mainloop()
