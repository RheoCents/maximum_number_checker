
def rheo_maximum_number_checker():
    # Welcome
    print("Hello and welcome to Rheo's number checker\nFor this, we will ask you 3 numbers and it we will show the highest!")
    # Input
    user_input_number_1 = float(input("give me a number "))
    user_input_number_2 = float(input("give me another "))
    user_input_number_3 = float(input("give me the last one "))

        #same value interpreter
    if user_input_number_1 == user_input_number_2 == user_input_number_3:
          print("Input 1, 2, and 3 have the same value")
          print(user_input_number_1, " is the highest value")
        
        #maximum checker if all are numbers
    if user_input_number_1 > user_input_number_2 and user_input_number_3:
          print(user_input_number_1, " is the highest value")
    if user_input_number_2 > user_input_number_1 and user_input_number_3:
          print(user_input_number_2, " is the highest value")
    if user_input_number_3 > user_input_number_1 and user_input_number_2:
          print(user_input_number_3, " is the highest value")
    
    else:
         print("That is not a number you silly")


        #repeat prompt
    print("Would you like to try again? Y/N")
    repeat_rheo_number_checker = input().lower()
    if repeat_rheo_number_checker == "Y" or "y":
        print()
        rheo_maximum_number_checker()
    else:
        print("Thank you for using Rheo's maximum number checker for threes!")          

rheo_maximum_number_checker()
