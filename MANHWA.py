import tkinter as tk
from tkinter import messagebox


def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        n = int(entry_compound.get())

        
        simple_interest = (principal * rate * time) / 100
        simple_total = principal + simple_interest

        
        compound_total = principal * (1 + (rate / 100) / n) ** (n * time)
        compound_interest = compound_total - principal

        
        result_text.set(
            f"Simple Interest: {simple_interest:.2f}\n"
            f"Simple Total Amount: {simple_total:.2f}\n\n"
            f"Compound Interest: {compound_interest:.2f}\n"
            f"Compound Total Amount: {compound_total:.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")



window = tk.Tk()
window.title("Interest Calculator")
window.geometry("500x500")
window.resizable(False, False)


title_label = tk.Label(window, text="Interest Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


tk.Label(window, text="Principal Amount:").pack()
entry_principal = tk.Entry(window)
entry_principal.pack(pady=5)


tk.Label(window, text="Annual Interest Rate (%):").pack()
entry_rate = tk.Entry(window)
entry_rate.pack(pady=5)


tk.Label(window, text="Time (Years):").pack()
entry_time = tk.Entry(window)
entry_time.pack(pady=5)

tk.Label(window, text="Compounds Per Year:").pack()
entry_compound = tk.Entry(window)
entry_compound.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate_interest,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold")
)
calculate_button.pack(pady=15)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Arial", 11), justify="left")
result_label.pack(pady=10)

window.mainloop()