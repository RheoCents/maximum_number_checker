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
    def is_intiger(value):
         try:
              int(value)
              return True
         except ValueError:
              return False

    def is_number(value):
         return is_float_number(value) or is_intiger(value)

    # Checking if it is a number
    if is_number(user_input_number_1) and is_number(user_input_number_2) and is_number(user_input_number_3):
        user_input_number_1 = float(user_input_number_1)
        user_input_number_2 = float(user_input_number_2)
        user_input_number_3 = float(user_input_number_3)

    # Check if the 3 numbers are the same
        if is_number(user_input_number_1) == is_number(user_input_number_2) == is_number(user_input_number_3):
            print("Input 1, 2, and 3 have the same value")
            print(user_input_number_1, " is the highest value")

        # Check if 2 of the numbers are the same
        elif is_number(user_input_number_2) == is_number(user_input_number_3) > is_number(user_input_number_1):
            print("Input 2 and 3 have the same value")
            print(user_input_number_2, " is the highest value")
        elif is_number(user_input_number_3) == is_number(user_input_number_1) > is_number(user_input_number_2):
            print("Input 1 and 3 have the same value")
            print(user_input_number_1, " is the highest value")
        elif is_number(user_input_number_2) == is_number(user_input_number_1) > is_number(user_input_number_3):
            print("Input 1 and 3 have the same value")
            print(user_input_number_1, " is the highest value")

        # Check which number is the highest
        elif is_number(user_input_number_3) > is_number(user_input_number_2) and is_number(user_input_number_1):
            print (user_input_number_3, " is the highest value")
        elif is_number(user_input_number_2) > is_number(user_input_number_3) and is_number(user_input_number_1):
            print (user_input_number_2, " is the highest value")
        elif is_number(user_input_number_1) > is_number(user_input_number_3) and is_number(user_input_number_2):
            print(user_input_number_1, " is the highest value")
    else:
        user_input_number_1 = float(user_input_number_1)
        user_input_number_2 = float(user_input_number_2)
        user_input_number_3 = float(user_input_number_3)
    # Checking if user input 1, 2, or 3 is a number
        if not is_number(user_input_number_1) and not is_number(user_input_number_2) and not is_number(user_input_number_3): 
                print("Input number 1, 2, and 3 is not a number")
                print("no input have the highest value")
            
            #Cheking is 2 inputs at the same time are not a number
        elif not is_number(user_input_number_1) and not is_number(user_input_number_2):
                print("Input number 1 and 2 are not numbers") 
                print(user_input_number_3, " is the highest value")
        elif not is_number(user_input_number_2) and not is_number(user_input_number_3): 
                print("Input number 2 and 3 are not numbers")
                print(user_input_number_1, " is the highest value")
        elif not is_number(user_input_number_1) and not is_number(user_input_number_3): 
                print("Input number 1 and 3 are not numbers")
                print(user_input_number_2, " is the highest value")
            
            # Checking if one of them is not a number
        elif not is_number(user_input_number_1) and not user_input_number_1.isdigit():
                if is_number(user_input_number_2) > is_number(user_input_number_3):
                    print("Input number 1 is not a number")
                    print(user_input_number_2, "is the highest value")
                elif is_number(user_input_number_3) > is_number(user_input_number_2):
                    print("Input number 1 is not a number")
                    print(user_input_number_3, "is the highest value")

        elif not is_number(user_input_number_2):
                if is_number(user_input_number_1) > is_number(user_input_number_3):
                    print("Input number 2 is not a number")
                    print(user_input_number_1, "is the highest value")  
                elif is_number(user_input_number_3) > is_number(user_input_number_1):
                    print("Input number 2 is not a number")
                    print(user_input_number_3, "is the highest value")
                
        elif not is_number(user_input_number_3):
                if is_number(user_input_number_1) > is_number(user_input_number_2):
                    print("Input number 3 is not a number")
                    print(user_input_number_1, "is the highest value")  
                elif is_number(user_input_number_2) > is_number(user_input_number_1):
                    print("Input number 3 is not a number")
                    print(user_input_number_2, "is the highest value")

    print("Would you like to try again? Y/N")
    repeat_rheo_number_checker = input().lower()
    if repeat_rheo_number_checker == "Y":
          print()
          rheo_number_checker()
    else:
         print("Thank you for using Rheo's maximum number checker for threes!")

rheo_number_checker()
            