# pseudo code test upload"
# testing git commit

# Ask user for 3 numbers

print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")

user_input_number_1 = int(input("give me a number "))
user_input_number_2 = int(input("give me another "))
user_input_number_3 = int(input("give me the last one "))

# Check the 3 numbers
if user_input_number_3 > user_input_number_2 and user_input_number_1:
    print (int(user_input_number_3) + str(" is the highest number"))
if user_input_number_2 > user_input_number_3 and user_input_number_1:
    print (int(user_input_number_2) + str(" is the highest number"))
if user_input_number_1 > user_input_number_3 and user_input_number_2:
    print(int(user_input_number_1) + str(" is the highest number"))
if user_input_number_1 == user_input_number_3 and user_input_number_2:
    print(int(user_input_number_1) + str(" is the highest number"))

else:
    print ("That is not a number")
