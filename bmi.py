import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        # Read height and convert if needed
        height = float(entry_height.get())
        if height_unit.get() == "inches":
            height = height * 2.54  # Convert inches to cm
        
        height = height / 100  # Convert cm to meters

        # Read weight and convert if needed
        weight = float(entry_weight.get())
        if weight_unit.get() == "lbs":
            weight = weight * 0.453592  # Convert pounds to kg

        bmi = weight / (height * height)
        bmi = round(bmi, 2)

        # Update progress bar
        bmi_progress['value'] = min(bmi, 40)

        result_text = f"Your BMI: {bmi}\n"

        if bmi < 18.5:
            result_text += "You are Underweight.\nTip: Eat more nutritious food!"
            label_result.config(fg="#3498db")
        elif 18.5 <= bmi < 24.9:
            result_text += "You have Normal weight.\nTip: Great job! Keep maintaining."
            label_result.config(fg="#2ecc71")
        elif 25 <= bmi < 29.9:
            result_text += "You are Overweight.\nTip: Exercise regularly and eat healthy."
            label_result.config(fg="#f1c40f")
        else:
            result_text += "You are Obese.\nTip: Consult a doctor for advice."
            label_result.config(fg="#e74c3c")
        
        label_result.config(text=result_text)
    except ValueError:
        label_result.config(text="Please enter valid numbers!", fg="#e74c3c")

def reset_fields():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    label_result.config(text="Your BMI will appear here.", fg="#bdc3c7")
    bmi_progress['value'] = 0
    height_unit.set("cm")
    weight_unit.set("kg")

# Window setup
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x550")
window.configure(bg="#2c3e50")  # Dark background

# Title label
title_label = tk.Label(window, text="BMI Calculator", font=("Helvetica", 22, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Height input
label_height = tk.Label(window, text="Enter Height:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
label_height.pack(pady=5)
entry_height = tk.Entry(window, font=("Helvetica", 12), bd=2, bg="#34495e", fg="#ecf0f1", insertbackground="white")
entry_height.pack(pady=5)

# Height unit selection
height_unit = tk.StringVar(value="cm")
height_unit_menu = ttk.Combobox(window, textvariable=height_unit, values=["cm", "inches"], state="readonly", font=("Helvetica", 11))
height_unit_menu.pack(pady=5)

# Weight input
label_weight = tk.Label(window, text="Enter Weight:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
label_weight.pack(pady=5)
entry_weight = tk.Entry(window, font=("Helvetica", 12), bd=2, bg="#34495e", fg="#ecf0f1", insertbackground="white")
entry_weight.pack(pady=5)

# Weight unit selection
weight_unit = tk.StringVar(value="kg")
weight_unit_menu = ttk.Combobox(window, textvariable=weight_unit, values=["kg", "lbs"], state="readonly", font=("Helvetica", 11))
weight_unit_menu.pack(pady=5)

# Calculate button
button_calculate = tk.Button(window, text="Calculate BMI", font=("Helvetica", 13, "bold"),
                             bg="#2980b9", fg="white", bd=0, padx=10, pady=5, command=calculate_bmi, activebackground="#3498db")
button_calculate.pack(pady=15)

# Reset button
button_reset = tk.Button(window, text="Reset", font=("Helvetica", 13, "bold"),
                         bg="#c0392b", fg="white", bd=0, padx=10, pady=5, command=reset_fields, activebackground="#e74c3c")
button_reset.pack(pady=5)

# Progress bar style for dark theme
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=20, background="#1abc9c", troughcolor="#34495e", bordercolor="#34495e", lightcolor="#34495e", darkcolor="#34495e")

# Progress bar
bmi_progress = ttk.Progressbar(window, orient="horizontal", length=250, mode="determinate", maximum=40, style="TProgressbar")
bmi_progress.pack(pady=20)

# Result label
label_result = tk.Label(window, text="Your BMI will appear here.", font=("Helvetica", 14), bg="#2c3e50", fg="#bdc3c7", justify="center")
label_result.pack(pady=20)

# Run the app
window.mainloop()
