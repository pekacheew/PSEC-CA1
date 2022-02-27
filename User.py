from rwaFiles import *
from cipher import *
from verifiers import *
from datetime import datetime
import time
import threading
from colors import *
userID = ''
modelAns = []
ansList = []
noOfQns = qzSettings(2)
timer = 0
############################################ Start of Countdown ############################################
def countdown():
    global timer
    timer *=  60                                                                    # TIMER in minutes * 60 seconds
    for i in range(timer):
        timer-=1
        time.sleep(1)

############################################ Start of Quiz Results ############################################
def quizResult():                   
    global modelAns
    global ansList
    global timer
    totalMarks = 0

    for f in range(len(modelAns)):
        if ansList[f] == modelAns[f]:                                               # check if answer is correct
            totalMarks += 2                                                         # for every answer that is correct, add 2 marks
        else:
            pass
    
    print(f'\nTotal Marks: {totalMarks}')                                           # print total marks attained
    
    fullMarks = len(ansList)*2
    if totalMarks == 0:
        percentage = 0.0
    else:
        percentage = totalMarks / fullMarks * 100                                   # calculate percentage
    print(f"\nYou've scored {percentage}%.")                                        # print out percentage of marks attained
    
    if percentage >= 50 and percentage < 60:                                        # print out grade
        print(styleStr(("That's a D grade. You can do better!"),rgb=(255,48,48)))
    elif percentage >= 60 and percentage < 70:
        print(styleStr(("That's a C grade. Keep it up!"),rgb=(48,249,255)))
    elif percentage >= 70 and percentage < 80:
        print(styleStr(("That's a B grade. Almost there!"),rgb=(235,255,48)))
    elif percentage >= 80 and percentage <= 100:
        print(styleStr(("That's an A grade. Good job!"),rgb=(55,255,48)))
    else:
        print("You have failed the test. Study harder!")
    
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                # date & time

    #write results into quiz_results.csv
    resultToWrite = (f"{userID},{str(totalMarks)},{str(percentage)},{current_date_time}")
    wResults(resultToWrite)
    rmvSpaceR()
    
    tOrF = True
    if tOrF == True:
        tOrF = adminORuser(userID)                                                  # check if user is admin or user
        if tOrF == True:                                                            # if user:
            attemptCount(userID)                                                    # take away 1 attempt count from user

    def newAttempt():
        tOrF = True
        while tOrF:
            userInput = input("Do you want to try again (y|n)? ")
            tOrF = yOrN(userInput)
        if userInput == 'y':
            beginQuiz()
        else:
            # cdthread.join()
            exit()

    newAttempt()                                                                    # end of program

############################################ Start of Begin Quiz ############################################
def beginQuiz():

    global ansList
    global modelAns
    global userID
    global cdthread
    ansList = [0] * noOfQns # e.g. ansList = [0,0,0,0,0] [b,c,b,0,d] [a,b,c,d]
    
    attemptsLeft = usrAttempts(userID)                                              # check attempts left
    if attemptsLeft == True:                                                        # if 0 attempts left, return to menu
        startUser()
    
    print(styleStr((f"Hi {userID}, please choose the best answer for the questions."),rgb=(255,200,100)))
    print(styleStr((f"Time allowed: {qzSettings(1)} minute(s)."),rgb=(255,200,100)))# get timer from quiz setting

    with open('./csv/question_pool.csv', 'r') as csvFile:
        csvFileR = csvFile.readlines()
        random.shuffle(csvFileR)                                                    # shuffle questions
    
    def qnNP():
        global timer
        timer = qzSettings(1)                                                       # get TIMER in minutes from qzSettings
        global modelAns      
        modelAns = ["0\n"] * noOfQns                                                # Print and Answer Questions
        qnNum = 0

        cdthread = threading.Thread(target = countdown)                             # threading target countdown TIMER function
        cdthread.start()                                                            # initiate threading function

        while qnNum < noOfQns:
            qnPool = csvFileR[qnNum].split(sep=',')
            print(f'\n\tQuestion {qnNum+1}: '+qnPool[0]+'\n')
            print(f'\ta) {qnPool[1]}\n\tb) {qnPool[2]}\n\tc) {qnPool[3]}\n\td) {qnPool[4]}\n')

            modelAns[qnNum] = qnPool[5]
            
            for i in range(len(modelAns)):
                modelAns[i] = modelAns[i].strip('\n')   # for e.g. modelAns = [a\n,b\n,c\n,a\n,a\n] -> [a,b,c,a,a]
            usrAns = quizOption(qnNum)                                              # ask for user input a,b,c,d,P,N & verify input

            if qnNum < noOfQns:
                if usrAns == 'N':                                                   # move on to next question
                    qnNum += 0
                elif usrAns == 'P':                                                 # move back to previous question
                    qnNum -= 2
                else:
                    ansList[qnNum] = usrAns                                         # insert user's answer into his answer list
            
            elif qnNum >= noOfQns:
                print()

            if timer == 0:                                                          # if TIMER reaches 0, auto submit quiz
                print("You have ran out of time. Submitting quiz automatically...")
                time.sleep(3)
                quizResult()
            
            qnNum += 1                                                              # increment question Number
        
        # print summary screen of all questions n answers provided
        qnNumber = 0
        while qnNumber < noOfQns:
            qnPool = csvFileR[qnNumber].split(sep=',')
            print(f'\n\tQuestion {qnNumber+1}: '+qnPool[0]+'\n')
            print(f'\ta) {qnPool[1]}\n\tb) {qnPool[2]}\n\tc) {qnPool[3]}\n\td) {qnPool[4]}\n\t(Your Answer) >>> {ansList[qnNumber]}')
            qnNumber += 1
        

    qnNP()

    tOrF = True
    while tOrF == True:
        submission = input(styleStr(("\nEnter 0 to submit or 1 to make changes: "),rgb=(255,200,100)))            # ask user to confirm submission or to change answer
        if submission == "0":
            tOrF = False
            quizResult()
        elif submission == "1":
            tOrF = True
            qnNP()
        else:
            print("Please enter a valid input.")
            tOrF = True

############################################ Start of User Login ############################################
def usrLogin():
    tOrF = True
    passCount = True
    passCounter = 0
    idCounter = 0
    idCount = True
    global userID
    
    while tOrF == True and idCount == True:
        userID = input("\nPlease enter the user's ID: ")                            # check if userID exists, if not, ask again
        tOrF = regUsrIDtwo(userID,'u') and regUsrIDtwo(userID,'a')
        idCounter += 1
        if idCounter == 3 and tOrF == True:                                         # limit id tries
            print("You have tried too many times, returning you to previous menu.\n")
            startUser()

    tOrF = True
    while tOrF == True and passCount == True:        
        userPswd = input("\nPlease enter the user's Password: ")                    # ask for password
        # encrypt with Caesar cipher and check it against userid_pswd.csv, if it's not a match, ask to re-enter
        encryptedPass = encrypt(userPswd)
        tOrF = usrPswd(userID,encryptedPass)

        passCounter += 1
        if passCounter == 3 and tOrF == True:                                       #limit password tries
            print("You have tried too many times.")
            passCount = False
            startUser()
    
    beginQuiz()

############################################ Start of User Registration ############################################
def regUsr():
    tOrF = True
        
    while tOrF == True:
        userID = input("\nPlease enter the new user's ID: ")                        # ask for new user's userID
        verifyUserID = checkComma(userID)
        if verifyUserID == True:
            print("Please do not enter a comma in your ID.")
            tOrF = True
        else:
            tOrF = regUsrIDone(verifyUserID)

    tOrF = True
    while tOrF == True:
        userPswd = input("\nPlease enter the new user's Password: ")                # ask for new user's passwd
        tOrF = passcheck(userPswd)                                                  # check if the passwd is secure

    encryptedPass = encrypt(userPswd)                                               # encrypt passwd with Caesar Cipher

    tOrF = True
    while tOrF == True:
        scrtQn = input("\nPlease enter a secret recovery question.\n>>> ")              # ask for secret question
        verifyScrtQn = checkComma(scrtQn)
        if verifyScrtQn == True:
            print("Please do not enter a comma in your question.")
            tOrF = True
        else:
            tOrF = False

    tOrF = True
    while tOrF == True:
        scrtAns = input("\nPlease enter your secret question's answer.\n>>> ")          # ask for secret question's answer
        verifyScrtAns = checkComma(scrtAns)
        if verifyScrtAns == True:
            print("Please do not enter a comma in your answer.")
            tOrF = True
        else:
            tOrF = False

    # concatenate userID + userPswd + U + Attempts + secret question + secret question's answer'
    writeIntoFile = (str(userID)+','+str(encryptedPass)+',u'+','+str(qzSettings(3)) + ',' + str(scrtQn) + ',' + str(scrtAns) )
    
    newUsr(writeIntoFile)                                                           # insert userID and passwd into userid_pswd.csv
        
    print("\nRegistration Successful!\n")                                           # print successful
    rmvSpaceID()
    startUser()                                                                     # startUser()
    
############################################ Start of Reset Password ############################################
def resetPassword():
    goOn = False
    idCounter = 0
    passCounter = 0
    idCount = True
    tOrF = True
    passCount = True

    while tOrF == True and idCount == True:
        userID = input("\nPlease enter the user's ID: ")                             # ask for user's ID                          
        tOrF = regUsrIDtwo(userID,'u') and regUsrIDtwo(userID,'a')
        idCounter += 1
        if idCounter == 3 and tOrF == True:
            print("You have tried too many times, returning you to previous menu.\n")
            startUser()

    tOrF = True
    while tOrF == True and passCount == True:        
        secretAns = input(f'Q: {secretQ(userID)}\n>>> ')                             # ask user their secret question

        tOrF = secretA(userID,secretAns)                                             # check if user secret answer is correct
        
        passCounter += 1                                                             # limit answer tries
        if passCounter == 3 and tOrF == True:
            print("\nYou have tried too many times.\n")
            passCount = False
            startUser()
    
    while tOrF == False:                                                                        
        userPswd = input("\nPlease enter the new user's Password: ")                 # ask for new user's passwd
        tOrF = passcheck(userPswd)                                                   # check if the passwd is secure
        
        if tOrF == False:
            tOrF = True
            goOn = True
        else:
            tOrF = False

    while goOn == True:
        encryptedPass = encrypt(userPswd)                                            # encrypt passwd with Caesar Cipher
        editPswd(userID,encryptedPass)                                               # write password into userid_pswd.csv
        rmvSpaceID()
        goOn = False
    startUser()

############################################ Start of User Application ############################################
def startUser():
    tOrF = True
    print("\n***Welcome to Quiz Application***")
    print("a) Start Quiz Application")
    print("b) Register User Account")
    print("c) Reset Password")
    print("d) Exit")

    while tOrF == True:
        userInput = input("Enter (a) to (c) to continue, (d) to exit: ")
        tOrF = abcd(userInput)

    if userInput == "a":                                                             # start quiz application, allow user to login
        usrLogin()
    elif userInput == "b":                                                           # allow user to register new account
        regUsr()
    elif userInput == "c":                                                           # allow user to reset their password
        resetPassword()
    elif userInput == "d":                                                           # allow user to exit program
        exit()

startUser()
