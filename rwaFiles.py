import random
########################## userid_pswd.csv #######################
# Remove spacing in list function
def rmvSpaceID():
    with open('./csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# Check if User already Exist 
def regUsrIDone(userID):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                if userID == exUserID[0]:
                    print("User already exists.")
                    csvFile.close()
                    return True

            else:
                csvFile.close()
                return False

# Check if User Exist 
def regUsrIDtwo(userID,aOrU):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                stripUserID = exUserID[2].strip('\n')
                if userID == exUserID[0]:
                    #check if user is admin or user account
                    if aOrU == stripUserID:
                        
                        csvFile.close()
                        return False
            else:
                csvFile.close()
                return True
                
# check if user is admin or user account
def adminORuser(userID):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                exUserID = i.split(sep=',')
                stripExUserID = exUserID[2].strip('\n')
                if userID == exUserID[0]:
                    #check if user is admin or user account
                    if stripExUserID == 'a':
                        csvFile.close()
                        return False
                    elif stripExUserID == 'u':
                        csvFile.close()
                        return True
            else:
                csvFile.close()
                return True

# write New User into userid_pswd.csv
def newUsr(writeIntoFile):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{writeIntoFile}')
    with open('./csv/userid_pswd.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# check if password is correct
def usrPswd(userID,userPswd):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            
            for i in csvFileR:
                attempts = i.split(sep=',')
                stripAttempts = attempts[1].strip('\n')
                
                if userID == attempts[0] and userPswd == stripAttempts:
                    print("Correct Password")
                    csvFile.close()
                    return False
                elif userID == attempts[0] and userPswd != stripAttempts:
                    print("Wrong password")
                    csvFile.close()
                    return True
            else:
                pass

# update new password of existing user
def editPswd(userID,newuserPswd):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            attempts = csvFileR[i].split(sep=',')

            if userID == attempts[0]:
                toAppend = userID + ',' + newuserPswd + ',' + attempts[2] +',' + attempts[3] +',' +attempts[4] +',' + attempts[5]+'\n'
                csvFileR[i] = toAppend
                
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()
    

# remove User
def removeUsr(userID):
    with open('./csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            userIDsplit = i.split(sep=',')
            if userID == userIDsplit[0]:
                csvFileR.remove(i)
        csvFile.close()
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# retrieve user list
def usrList():
    with open('./csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            userIDsplit = i.split(sep=',')
            print(str(r)+'. '+userIDsplit[0])

        csvFile.close()

# check attempts
def usrAttempts(userID):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        
        for i in csvFileR:
            attempts = i.split(sep=',')
            stripAttempts = attempts[3].strip('\n')
            
            if userID == attempts[0] and stripAttempts == '999':
                print("\nUnlimited attempts.\n")
                csvFile.close()
                return False
            elif userID == attempts[0] and stripAttempts == '0':
                print("\n0 Attempts Remaining, returning to main menu.\n")
                csvFile.close()
                return True
            elif userID == attempts[0]:
                print(f"\n{stripAttempts} Attempts Remaining")
                csvFile.close()
                return False

        else:
            pass

# update attempt count
def attemptCount(userID):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        

        for i in range(len(csvFileR)):
            attempts = csvFileR[i].split(sep=',')
            if userID == attempts[0] and attempts[3] == '999':
                pass
            else:
                newAttempt = int(attempts[3]) - 1 
                if userID == attempts[0]:
                    toAppend = attempts[0] + ',' + attempts[1] + ',' + attempts[2] +',' + str(newAttempt)+',' + attempts[4] + ',' + attempts[5] 
                    csvFileR[i] = toAppend
                
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()

# Reset all Attempts
def resetAttempt():
    with open('./csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')

            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(qzSettings(3)) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend

    with open('./csv/userid_pswd.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()


# Plus 1 Attempt to all users
def plusAttempt():
    with open('./csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(int(userIdSplit[3])+int(1)) + ',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Minus 1 Attempt to all user
def minusAttempt():
    with open('./csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(int(userIdSplit[3])-int(1)) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Set to unlimited attempts
def unlimitedAttempt():
    with open('./csv/userid_pswd.csv', 'r+') as csvFile:
        csvFileR = csvFile.readlines()

        for i in range(len(csvFileR)):
            userIdSplit = csvFileR[i].split(sep=',')
            if adminORuser(userIdSplit[0]) == True:
                toAppend = userIdSplit[0] + ',' + userIdSplit[1] + ',' + userIdSplit[2] +',' + str(999) +',' +userIdSplit[4] +',' +userIdSplit[5]
                csvFileR[i] = toAppend
    with open('./csv/userid_pswd.csv', 'w') as csvFile:
            for n in csvFileR:
                csvFile.write(n)
            csvFile.close()

# Check User Input against Secret Answer
def secretA(userID,secretAns):
    with open('./csv/userid_pswd.csv','r+') as csvFile:
                csvFileR = csvFile.readlines()
                for i in csvFileR:
                    attempts = i.split(sep=',')
                    stripAttempts = attempts[5].strip('\n')
                    
                    if userID == attempts[0] and secretAns == stripAttempts:
                        print("Correct")
                        csvFile.close()
                        return False
                    elif userID == attempts[0] and secretAns != stripAttempts:
                        print("Wrong")
                        csvFile.close()
                        return True
                else:
                    pass

# print user's secret question
def secretQ(userID):
    print()
    with open('./csv/userid_pswd.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()

        for i in csvFileR:
            userIDsplit = i.split(sep=',')
            if userID == userIDsplit[0]:
                return userIDsplit[4]

        csvFile.close()
########################## quiz_settings.csv #######################
# quiz timer
def quizTimer(newTime,selection):
    with open('./csv/quiz_settings.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()

            for i in range(len(csvFileR)):
                qzSet = csvFileR[i].split(sep=',')
                if qzSet[0] == selection:
                    toAppend = str(selection) + ', ' + str(newTime) + '\n'
                    csvFileR[i] = toAppend
                
    with open('./csv/quiz_settings.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()

# get quiz settings data
def qzSettings(input):
    with open('./csv/quiz_settings.csv','r+') as csvFile:
        qzSettingsVessel = []                      
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            
            qzSettingsVessel.append(i.split(',')[1])

        if input == 1:                              #timer
            variable = int(qzSettingsVessel[0]) 
            return variable
        elif input == 2:                           #num of questions
            variable = int(qzSettingsVessel[1]) 
            return variable
        elif input == 3:                          #attempts
            variable = int(qzSettingsVessel[2]) 
            return variable

########################## question_pool.csv #######################
# remove space in question_pool
def rmvSpaceQn():
    with open('./csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# check if question already exists
def regQnone(qn):
    with open('./csv/question_pool.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                qnPool = i.split(sep=',')
                if qn == qnPool[0]:
                    print("Question already exists.")
                    csvFile.close()
                    return True

            else:
                csvFile.close()
                return False

# check if question exists to be edited.
def regQntwo(qnToDel):
    with open('./csv/question_pool.csv','r+') as csvFile:
            csvFileR = csvFile.readlines()
            for i in csvFileR:
                qnPool = i.split(sep=',')
                if qnToDel == qnPool[0]:
                    print("Question exists.")
                    csvFile.close()
                    return False

            else:
                print("Question does not exist.")
                csvFile.close()
                return True

# add new line of question in
def addQuestion(newQuestion):
    with open('./csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{newQuestion}')
    with open('./csv/question_pool.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()
    rmvSpaceQn()
            
# remove question
def removeQn(qnDel):
    with open('./csv/question_pool.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
    
        for i in csvFileR:
            qnSplit = i.split(sep=',')
            if qnDel == qnSplit[0]:
                csvFileR.remove(i)
        csvFile.close()
    with open('./csv/question_pool.csv', 'w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# retrieve Question list
def qnList():
    with open('./csv/question_pool.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            qnSplit = i.split(sep=',')
            print('\n\t'+str(r)+'. '+qnSplit[0])
            print(f"\ta) {qnSplit[1]}")
            print(f"\tb) {qnSplit[2]}")
            print(f"\tc) {qnSplit[3]}")
            print(f"\td) {qnSplit[4]}")
            print(f"\t(ANS): {qnSplit[5]}")

        csvFile.close()

# edit question into question_pool.csv
def editQn(qn,newChg,index):
    with open('./csv/question_pool.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        rmvSpaceQn()
        for i in range(len(csvFileR)):
            qnPool = csvFileR[i].split(sep=',')

            if qn == qnPool[0]:
                if index == 0:
                    toAppend = f'{newChg},{qnPool[1]},{qnPool[2]},{qnPool[3]},{qnPool[4]},{qnPool[5]}\n'
                    csvFileR[i] = toAppend
                elif index == 1:
                    toAppend = f'{qnPool[0]},{newChg},{qnPool[2]},{qnPool[3]},{qnPool[4]},{qnPool[5]}\n'
                    csvFileR[i] = toAppend
                elif index == 2:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{newChg},{qnPool[3]},{qnPool[4]},{qnPool[5]}\n'
                    csvFileR[i] = toAppend
                elif index == 3:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{newChg},{qnPool[4]},{qnPool[5]}\n'
                    csvFileR[i] = toAppend
                elif index == 4:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{qnPool[3]},{newChg},{qnPool[5]}\n'
                    csvFileR[i] = toAppend
                elif index == 5:
                    toAppend = f'{qnPool[0]},{qnPool[1]},{qnPool[2]},{qnPool[3]},{qnPool[4]},{newChg}\n'
                    csvFileR[i] = toAppend

        rmvSpaceQn()

    with open('./csv/question_pool.csv', 'w') as csvFile:
        for n in csvFileR:
            
            csvFile.write(n)

        csvFile.close()


########################## quiz_results.csv #######################
# write into quiz results
def wResults(resultToWrite):
    with open('./csv/quiz_results.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()

        csvFileR.append(f'\n{resultToWrite}')
    with open('./csv/quiz_results.csv','w') as csvFile:
        for n in csvFileR:
            csvFile.write(n)

        csvFile.close()

# remove space for quiz_results.csv
def rmvSpaceR():
    with open('./csv/quiz_results.csv','r+') as csvFile:
        csvFileR = csvFile.readlines()
        for i in csvFileR:
            if i == '\n':
                csvFileR.remove(i)
        csvFile.seek(0)
        csvFile.truncate()
        for n in csvFileR:
            csvFile.write(n)
        csvFile.close()

# retrieve entire quiz results
def resultList():
    with open('./csv/quiz_results.csv','r+') as csvFile:    
        csvFileR = csvFile.readlines()
        r = 0

        for i in csvFileR:
            r += 1
            resultPool = i.split(sep=',')
            stripResultPool = resultPool[3].strip('\n')
            print(f"{str(r)}. {resultPool[0]} scored {resultPool[1]} marks. {resultPool[2]}%. Timestamp: {stripResultPool}")

        csvFile.close()
