def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Welcome
print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")




def rheo_maximum_number_checker():
    # Input
    user_input_number_1 = float(input("give me a number "))
    user_input_number_2 = float(input("give me another "))
    user_input_number_3 = float(input("give me the last one "))
    # Interchangable variable set
    maximum_number = None

    #same value interpreter
    if user_input_number_1 == user_input_number_2 :
        if user_input_number_1 == user_input_number_3:
            maximum_number = user_input_number_1
        
    #maximum checker if all are numbers
    if is_number(user_input_number_1):
            maximum_number = float(user_input_number_1)

    if is_number(user_input_number_2):
            if maximum_number is None or float(user_input_number_2) > maximum_number:
                maximum_number = float(user_input_number_2)

    if is_number(user_input_number_3):
            if maximum_number is None or float(user_input_number_3) > maximum_number:
                maximum_number = float(user_input_number_3)

    #printing the maximum number
    if maximum_number is not None:
        print(maximum_number, "is the highest value")
    
    #print for when no number was inputted
    else:
         print("That is not a number you silly")

        #repeat prompt
while True:
    rheo_maximum_number_checker()
    print()
    repeat_rheo_number_checker = input("Would you like to try again? (Y/N): ").strip().lower()
    if repeat_rheo_number_checker != "Y" and repeat_rheo_number_checker != "y":
        print("Thank you for using Rheo's maximum number checker for threes!")
        break