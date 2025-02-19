# main.py
import tkinter as tk
from tkinter import messagebox
from data_manager import save_person, read_people, delete_person, save_to_json
from stats_calculator import calculate_average_age, analyze_names

class PeopleTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("People Tracker")
        self.root.geometry("400x300")

        # Labels and Entries
        tk.Label(root, text="People Tracker").pack(pady=10)

        # Name Entry
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # Age Entry
        tk.Label(root, text="Age:").pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        # Buttons
        tk.Button(root, text="Add Person", command=self.add_person).pack(pady=5)
        tk.Button(root, text="View People", command=self.view_people).pack(pady=5)
        tk.Button(root, text="View Average Age", command=self.view_average_age).pack(pady=5)
        tk.Button(root, text="Analyze Names", command=self.analyze_names).pack(pady=5)
        tk.Button(root, text="Delete Person", command=self.delete_person).pack(pady=5)
        tk.Button(root, text="Save to JSON", command=self.save_to_json).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def add_person(self):
        name = self.name_entry.get()
        if name.lower() == 'quit':
            messagebox.showinfo("Goodbye", "Goodbye!")
            self.root.quit()
            return
        try:
            age = int(self.age_entry.get())
            save_person(name, age)
            messagebox.showinfo("Success", "Person saved successfully!")
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for age.")

    def view_people(self):
        people = read_people()
        if not people:
            messagebox.showinfo("Info", "No people recorded yet.")
        else:
            people_str = "\n".join([f"Name: {p['name']}, Age: {p['age']}" for p in people])
            messagebox.showinfo("People List", people_str)

    def view_average_age(self):
        people = read_people()
        avg_age = calculate_average_age(people)
        if avg_age == 0:
            messagebox.showinfo("Info", "No people recorded yet to calculate an average.")
        else:
            messagebox.showinfo("Average Age", f"Average age: {avg_age:.2f} years")

    def analyze_names(self):  # Ensure this method exists
        people = read_people()
        analysis = analyze_names(people)
        if "Error" in analysis:
            messagebox.showerror("API Error", analysis)
        else:
            messagebox.showinfo("Name Analysis", analysis)

    def delete_person(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter a name to delete.")
            return
        delete_person(name)
        messagebox.showinfo("Success", f"Person '{name}' deleted successfully!")
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

    def save_to_json(self):
        people = read_people()
        save_to_json(people)
        messagebox.showinfo("Success", "Data saved to people.json!")

def main():
    root = tk.Tk()
    app = PeopleTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()