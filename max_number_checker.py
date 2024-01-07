import tkinter as tk



def rheo_maximum_number_checker():
    user_input_number_1 = entry1.get()
    user_input_number_2 = entry2.get()
    user_input_number_3 = entry3.get()
    
    def is_number(value):
     try:
        float(value)
        return True
     except ValueError:
        return False
    
    maximum_number = None

    if user_input_number_1 == user_input_number_2 == user_input_number_3:
        maximum_number = user_input_number_1

    if is_number(user_input_number_1):
        maximum_number = float(user_input_number_1)

    if is_number(user_input_number_2):
        if maximum_number is None or float(user_input_number_2) > maximum_number:
            maximum_number = float(user_input_number_2)

    if is_number(user_input_number_3):
        if maximum_number is None or float(user_input_number_3) > maximum_number:
            maximum_number = float(user_input_number_3)

    if maximum_number is not None:
        result_label.config(text=f"The highest value is: {maximum_number}")
    else:
        result_label.config(text="That's no number, you silly")

root = tk.Tk()
root.title("Rheo's Maximum Number Checker")

welcome_label = tk.Label(root, text="Hello and welcome to Rheo's number checker! Enter 3 numbers below:")
welcome_label.pack()

input_frame = tk.Frame(root)
input_frame.pack()

label1 = tk.Label(input_frame, text="First number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1)

label2 = tk.Label(input_frame, text="Second number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1)

label3 = tk.Label(input_frame, text="Third number:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(input_frame)
entry3.grid(row=2, column=1)

check_button = tk.Button(root, text="Check", command=rheo_maximum_number_checker)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
