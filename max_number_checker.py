#

# Welcoming message
print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")
# Input Variable labeling
user_input_number_1 = input("give me a number ")
user_input_number_2 = input("give me another ")
user_input_number_3 = input("give me the last one ")

# Checking if it is a number
if user_input_number_1.isdigit() and user_input_number_2.isdigit() and user_input_number_3.isdigit():
    user_input_number_1 = float(user_input_number_1)
    user_input_number_2 = float(user_input_number_2)
    user_input_number_3 = float(user_input_number_3)

# Check the 3 numbers
    if user_input_number_3 > user_input_number_2 and user_input_number_1:
        print (user_input_number_3, " is the highest number")
    if user_input_number_2 > user_input_number_3 and user_input_number_1:
        print (user_input_number_2, " is the highest number")
    if user_input_number_1 > user_input_number_3 and user_input_number_2:
        print(user_input_number_1, " is the highest number")
    else:
        print("They have the same value\n", user_input_number_1, " is the highest value")

else:
    print ("That is not a number you silly")
