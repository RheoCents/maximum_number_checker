def rheo_number_checker():

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
        if user_input_number_1 == user_input_number_2 > user_input_number_3:
            print("Input 1 and 2 have the same value")
            print(user_input_number_1, " is the highest value")
        elif user_input_number_2 == user_input_number_3 > user_input_number_1:
            print("Input 2 and 3 have the same value")
            print(user_input_number_2, " is the highest value")
        elif user_input_number_3 == user_input_number_1 > user_input_number_2:
            print("Input 1 and 3 have the same value")
            print(user_input_number_1, " has the highest value")
        elif user_input_number_3 > user_input_number_2 and user_input_number_1:
            print (user_input_number_3, " has the highest value")
        elif user_input_number_2 > user_input_number_3 and user_input_number_1:
            print (user_input_number_2, " has the highest value")
        elif user_input_number_1 > user_input_number_3 and user_input_number_2:
            print(user_input_number_1, " has the highest value")
    else:

    # Checking if user input 1, 2, or 3 is a number
        if not user_input_number_1.isdigit() and not user_input_number_2.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 1, 2, and 3 is not a number")
            
            #Cheking is 2 at the same time is a number
        elif not user_input_number_1.isdigit() and not user_input_number_2.isdigit():
                print("Input number 1 and 2 are not numbers")
        elif not user_input_number_2.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 2 and 3 are not numbers")
        elif not user_input_number_1.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 1 and 3 are not numbers")
            
            # Checking if one of them is a number
        elif not user_input_number_1.isdigit():
                print("Input number 1 is not a number")
        elif not user_input_number_2.isdigit():
                print("Input number 2 is not a number")
        elif not user_input_number_3.isdigit():
                print("Input number 3 is not a number")

    print("Would you like to try again? Yes/No")
    repeat_rheo_number_checker = str(input())
    if  repeat_rheo_number_checker == str("Yes" or "yes"):
          rheo_number_checker()

rheo_number_checker()
            