import tkinter as tk

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def check_maximum_number():
    user_input_number_1 = user_entry_number_1.get
    user_input_number_2 = user_entry_number_2.get
    user_input_number_3 = user_entry_number_3.get
    
    maximum_number = None
    
    if user_input_number_1 == user_input_number_2 == user_input_number_3:
        maximum_number = user_input_number_1
        rheo_answer_to_max_number.config(text="They all have the same value")
    else:
        if is_number(user_input_number_1):
            maximum_number = float(user_input_number_1)

        if is_number(user_input_number_2):
            if maximum_number is None or float(user_input_number_2) > maximum_number:
                maximum_number = float(user_input_number_2)

        if is_number(user_input_number_3):
            if maximum_number is None or float(user_input_number_3) > maximum_number:
                maximum_number = float(user_input_number_3)

        if maximum_number is not None:
            rheo_answer_to_max_number.config(text=f"{maximum_number} is the highest value")
        else:
            rheo_answer_to_max_number.config(text="That's no number you silly")


root = tk.Tk()
root.title("Rheo's Number Checker")

label = tk.Label(root, text="Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")
label.pack()

user_entry_number_1 = tk.Entry(root)
user_entry_number_1.pack()

user_entry_number_2 = tk.Entry(root)
user_entry_number_2.pack()

user_entry_number_3 = tk.Entry(root)
user_entry_number_3.pack()

check_button = tk.Button(root, text="Check", command=check_maximum_number)
check_button.pack()

rheo_answer_to_max_number = tk.Label(root, text="")
rheo_answer_to_max_number.pack()

root.mainloop()