from rwaFiles import *
def password_validator(passwd):
      
    SpecialSym =['$', '@', '#', '%', '!']                                           # valid special characters
    val = True
      
    if len(passwd) < 4:                                                             # if password length is lesser than 4, invalid password
        print('Password length should be at least 4.')
        val = False
          
    if len(passwd) > 20:
        print('Passowrd length should be not be greater than 20.')                  # if password length is longer than 20, invalid password
        val = False
          
    if not any(char.isdigit() for char in passwd):                                  # if password do not have numerals, invalid password
        print('Password should have at least one numeral.')
        val = False
          
    if not any(char.isupper() for char in passwd):                                  # if password do not have uppercase, invalid password
        print('Password should have at least one uppercase letter.')
        val = False
          
    if not any(char.islower() for char in passwd):                                  # if password do not have lowercase, invalid password
        print('Password should have at least one lowercase letter.')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols !,$,@,#,%.')
        val = False
        
    if any(',' in char for char in passwd):                                         # if password has commas, invalid password                                   
        print("Password should not have commas.")
        val = False

    if val:
        return val
  
# Main password checker function
def passcheck(passwd):
      
    if (password_validator(passwd)):                                               
        print("Password is valid.")
        return False
    else:
        print("Invalid Password !!")
        return True

# check integer function
def intCheck(intput):                                                               
        if intput <= 60 and intput > 0:                                             # integer only valid if it is between the value of 0 - 60
            return False

        elif intput > 60:                                                           # if integer input is more than 60, invalid input
            print("Please enter an integer of no more than 60.")
            return True

        elif intput <= 0:                                                           # if integer input is less than 0, invalid input
            print("Please enter an integer of no less than or equal to 0.")
            return True

        else:                                                                       # if integer input is not a number, invalid input
            print("Please enter a valid integer.")
            return True
    
# double confirm function
def dblConfirm():
    question = input("\nDouble confirm to delete (y|n)? ")                          # prompt for input (y|n)
    if question == "y":                                                             # if input is 'y', return True
        print()
        return True
    elif question == "n":                                                           # if input is 'n', return False
        print()
        return False
    else:                                                                           # if input is neither 'y' nor 'n', prompt for input again
        print("You have not entered a valid option.")
        dblConfirm()

# (y|n) function
def yOrN(userinput):

    if userinput == "y":                                                            # if input is 'y', return False
        return False    
    elif userinput == "n":                                                          # if input is 'n', return True
        pass
        return False
    else:                                                                           # if input is neither 'y' nor 'n', prompt for input again
        print("You have not entered a valid option.")
        return True

# (a|b|c|d) function
def abcdOption():
    tOrF = True
    
    while tOrF == True:
        abcd = input("What do you want to it change to (a|b|c|d)? ")                # prompt for user input (a|b|c|d)
        if abcd == "a":                                                             # if input = 'a', return 'a'
            print("\nSuccessful")
            return 'a'
            
        elif abcd == "b":                                                           # if input = 'b', return 'b'
            print("\nSuccessful")
            return 'b'
               
        elif abcd == "c":                                                           # if input = 'c', return 'c'
            print("\nSuccessful")
            return 'c'
               
        elif abcd == "d":                                                           # if input = 'd', return 'd'
            print("\nSuccessful")
            return 'd'
                
        else:                                                                       # if input is neither 'a' or 'b' or 'c' or 'd', prompt for input again 
            print("Please enter a valid letter.")
            tOrF = True

# quiz options
def quizOption(i):
    tOrF = True
    while tOrF == True:

        if i == 0:
            # prompts for input (a|b|c|d|N) and returns input value. If not valid input, prompt again.
            qnUserInput = input("\tEnter (a) to (d) for answer, N for next question:\n>>> ")    
            if qnUserInput == "a":
                return 'a'
            elif qnUserInput == "b":
                return 'b'
            elif qnUserInput == "c":
                return 'c'
            elif qnUserInput == "d":
                return 'd'
            elif qnUserInput == "N":
                return 'N'
            else:
                print("Please enter a valid option.")
                tOrF = True

        elif i == qzSettings(2)-1:
            # prompts for input (a|b|c|d|P) and returns input value. If not valid input, prompt again.
            qnUserInput = input("\tEnter (a) to (d) for answer, P for previous question:\n>>> ")
            if qnUserInput == "a":
                return 'a'
            elif qnUserInput == "b":
                return 'b'
            elif qnUserInput == "c":
                return 'c'
            elif qnUserInput == "d":
                return 'd'
            elif qnUserInput == "P":
                return 'P'
            else:
                print("Please enter a valid option.")
                tOrF = True
            

        else:
            # prompts for input (a|b|c|d|N|P) and returns input value. If not valid input, prompt again.
            qnUserInput = input("\tEnter (a) to (d) for answer, P for previous question, N for next question:\n>>> ")
            
            if qnUserInput == "a":
                return 'a'
            elif qnUserInput == "b":
                return 'b'
            elif qnUserInput == "c":
                return 'c'
            elif qnUserInput == "d":
                return 'd'
            elif qnUserInput == "N":
                return 'N'
            elif qnUserInput == "P":
                return 'P'
            else:
                print("Please enter a valid option.")
                tOrF = True

# another (a|b|c|d) function
def qnAnsOption():
    tOrF = True
    
    while tOrF == True:
        # prompt for input (a|b|c|d) and return input value. If not valid input, prompt again.
        abcd = input("What is the correct answer (a|b|c|d)?: ")

        if abcd == "a":
            return 'a'
        elif abcd == "b":
            return 'b'
        elif abcd == "c":
            return 'c'
        elif abcd == "d":
            return 'd'
        else:
            print("Please enter a valid letter.")
            tOrF = True

# admin or user function
def admOrUsr(aOrU):
    # checks if user input is either an 'a' or 'u' , if not, prompt for a valid input again.
    if aOrU == "a":
        return False
    elif aOrU == "u":
        return False
    else:
        print("Please enter a valid input.")
        return True
        
# another (a|b|c|d) function
def abcd(abc):
    # prompt for input (a|b|c|d) and return input value. If not valid input, prompt again.
    if abc == "a":
        return False
    elif abc == "b":
        return False
    elif abc == "c":
        return False
    elif abc == "d":
        exit()
    else:
        print("Please enter a valid input.")
        return True

# check input for commas
def checkComma(userID):
    # check input for commas, if got commas, return True and prompt user to input again
    for i in userID:
        if i == ',':
            return True
        else:
            tOrF = True
    if len(userID) == 0:
        tOrF = False
        
    if tOrF:
        return userID
