print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")

user_inputed_number_1 = input("Give me a number: ")
user_inputed_number_2 = input("Give me another number: ")
user_inputed_number_3 = input("Give me the last number: ")

# Check if inputs are numbers
if user_inputed_number_1.isdigit() and user_inputed_number_2.isdigit() and user_inputed_number_3.isdigit():
    user_inputed_number_1 = float(user_inputed_number_1)
    user_inputed_number_2 = float(user_inputed_number_2)
    user_inputed_number_3 = float(user_inputed_number_3)

    # Check the 3 numbers
    if user_inputed_number_3 > user_inputed_number_2 and user_inputed_number_1:
        print(user_inputed_number_3, "is the highest number")
    if user_inputed_number_2 > user_inputed_number_3 and user_inputed_number_1:
        print(user_inputed_number_2, "is the highest number")
    if user_inputed_number_1 > user_inputed_number_3 and user_inputed_number_2:
        print(user_inputed_number_1, "is the highest number")
    if user_inputed_number_1 == user_inputed_number_3 and user_inputed_number_2:
        print(user_inputed_number_1, "is the highest number")
else:
    print("Oops! Please enter valid numbers.")
