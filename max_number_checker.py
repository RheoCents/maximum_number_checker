def rheo_maximum_number_checker():
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
          print(user_input_number_1, " is the highest value")
rheo_maximum_number_checker()
