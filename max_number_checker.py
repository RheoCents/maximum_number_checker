# pseudo code test upload"
# testing git commit

# Ask user for 3 numbers

print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")
user_inputed_number_1 = int(input("give me a number "))
user_inputed_number_2 = input("give me another ")
user_inputed_number_3 = input("give me the last one ")

# Check the 3 numbers
if user_inputed_number_3 > user_inputed_number_2 and user_inputed_number_1:
    print (user_inputed_number_3 + str(" is the highest number"))
if user_inputed_number_2 > user_inputed_number_3 and user_inputed_number_1:
    print (user_inputed_number_2 + str(" is the highest number"))
else:
    print (user_inputed_number_1 + str(" is the highest number"))
