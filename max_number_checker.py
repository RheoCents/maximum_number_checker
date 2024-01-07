def rheo_number_checker():

    # Welcoming message
    print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")

    # Input Variable labeling
    user_input_number_1 = input("give me a number ")
    user_input_number_2 = input("give me another ")
    user_input_number_3 = input("give me the last one ")

    #defining float values
    def is_float_number(value):
         try:
              float(value)
              return True
         except ValueError:
              return False
    def is_int(value):
         try:
              int(value)
              return True
         except ValueError:
              return False

    # Checking if it is a number
    if user_input_number_1.isdigit() and user_input_number_2.isdigit() and user_input_number_3.isdigit():
        user_input_number_1 = float(user_input_number_1)
        user_input_number_2 = float(user_input_number_2)
        user_input_number_3 = float(user_input_number_3)

    # Check if the 3 numbers are the same
        if user_input_number_1 == user_input_number_2 == user_input_number_3:
            print("Input 1, 2, and 3 have the same value")
            print(user_input_number_1, " is the highest value")

        # Check if 2 of the numbers are the same
        elif user_input_number_2 == user_input_number_3 > user_input_number_1:
            print("Input 2 and 3 have the same value")
            print(user_input_number_2, " is the highest value")
        elif user_input_number_3 == user_input_number_1 > user_input_number_2:
            print("Input 1 and 3 have the same value")
            print(user_input_number_1, " is the highest value")
        elif user_input_number_2 == user_input_number_1 > user_input_number_2:
            print("Input 1 and 3 have the same value")
            print(user_input_number_1, " is the highest value")

        # Check which number is the highest
        elif user_input_number_3 > user_input_number_2 and user_input_number_1:
            print (user_input_number_3, " is the highest value")
        elif user_input_number_2 > user_input_number_3 and user_input_number_1:
            print (user_input_number_2, " is the highest value")
        elif user_input_number_1 > user_input_number_3 and user_input_number_2:
            print(user_input_number_1, " is the highest value")
    else:

    # Checking if user input 1, 2, or 3 is a number
        if not user_input_number_1.isdigit() and not user_input_number_2.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 1, 2, and 3 is not a number")
                print("no input have the highest value")
            
            #Cheking is 2 inputs at the same time are not a number
        elif not user_input_number_1.isdigit() and not user_input_number_2.isdigit():
                print("Input number 1 and 2 are not numbers") 
                print(user_input_number_3, " is the highest value")
        elif not user_input_number_2.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 2 and 3 are not numbers")
                print(user_input_number_1, " is the highest value")
        elif not user_input_number_1.isdigit() and not user_input_number_3.isdigit(): 
                print("Input number 1 and 3 are not numbers")
                print(user_input_number_2, " is the highest value")
            
            # Checking if one of them is not a number
        elif not user_input_number_1.isdigit():
                if user_input_number_2 > user_input_number_3:
                    print("Input number 1 is not a number")
                    print(user_input_number_2, "is the highest value")
                elif user_input_number_3 > user_input_number_2:
                    print("Input number 1 is not a number")
                    print(user_input_number_3, "is the highest value")

        elif not user_input_number_2.isdigit():
                if user_input_number_1 > user_input_number_3:
                    print("Input number 1 is not a number")
                    print(user_input_number_1, "is the highest value")  
                elif user_input_number_3 > user_input_number_1:
                    print("Input number 1 is not a number")
                    print(user_input_number_3, "is the highest value")
                
        elif not user_input_number_3.isdigit():
                if user_input_number_1 > user_input_number_2:
                    user_input_number_1 = float(user_input_number_1)
                    print("Input number 1 is not a number")
                    print(user_input_number_1, "is the highest value")  
                elif user_input_number_2 > user_input_number_1:
                    user_input_number_2 = float(user_input_number_2)
                    print("Input number 1 is not a number")
                    print(user_input_number_2, "is the highest value")

    print("Would you like to try again? Yes/No")
    repeat_rheo_number_checker = str(input())
    if  repeat_rheo_number_checker.lower == "Yes" or "yes":
          print()
          rheo_number_checker()
    else:
         print("Thank you for using Rheo's maximum number checker for threes!")
rheo_number_checker()
            