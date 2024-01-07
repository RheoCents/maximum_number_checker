import tkinter as tk
#float input validation
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
# main prompt
def check_maximum_number():
    user_input_number_1 = user_entry_number_1.get
    user_input_number_2 = user_entry_number_2.get
    user_input_number_3 = user_entry_number_3.get
    
    maximum_number = None
    #if statements
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

#main root
root = tk.Tk()
root.title("Rheo's Number Checker")
root.configure(background="black")
root.geometry("400x230")

#pop-up message
label = tk.Label(root, text="Hello and welcome to Rheo's number checker\n"
                 "For this, we will ask you 3 numbers and it we will show the highest!",background="black", foreground="orange")
label.pack()
label.config(background="black")

#space
for_space = tk.Label(root, text="", background="black")
for_space.pack()

#button 1 input
user_entry_number_1 = tk.Entry(root)
user_entry_number_1.pack()
user_entry_number_1.config(background="white")

#space
for_space = tk.Label(root, text="", background="black")
for_space.pack()

#button 2 input
user_entry_number_2 = tk.Entry(root)
user_entry_number_2.pack()

#space
for_space = tk.Label(root, text="", background="black")
for_space.pack()

#button 3 input
user_entry_number_3 = tk.Entry(root)
user_entry_number_3.pack()

#space
for_space = tk.Label(root, text="", background="black")
for_space.pack()

#check button 1 input
check_button = tk.Button(root, text="Check", command=check_maximum_number, foreground="white", background="black")
check_button.pack()

#answer
rheo_answer_to_max_number = tk.Label(root, text="",foreground="#09ff00", background="black")
rheo_answer_to_max_number.pack()

root.mainloop()