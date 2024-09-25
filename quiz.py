print("""NOTE FOR USER: If the quiz doesn't have a minimum of one question in each section, then the user is requested to create atleast one question in each section.
After creating, the user is asked to restart the window and play the quiz.""")
print()
    
#Modules are imported
import random
import mysql.connector as sql
import csv
import pickle

#Inputs for asking user id and password
print("FETCHING MYSQL ACCOUNT DETAILS...")
us_id = input("Enter user id:")
pd = input("Enter password:")
print()

try:
    #Python is connected to MySQL
    handle = sql.connect(host = "localhost",user = us_id,password = pd)
    cur = handle.cursor(buffered = True)
    cur.execute("create database if not exists PROJECT")
    cur.execute("use PROJECT")
    cur.execute("create table if not exists LEADERBOARD(PLAYER_ID varchar(5) unique, NAME varchar(20), QUIZ varchar(30), POINTS int)")

    #User-defined function for displaying the clues
    def quiz():
        global word
        spaces = ['_']*len(word)
        l1 = random.randint(0,3)
        l2 = random.randint(3,len(word))
        print("The word is of",len(word),"letters")
        index1 = word.find(word[l1-1])
        removed_character='*'
        spaces[index1] = word[l1-1]
        index2 = word.find(word[l2-1])
        spaces[index2] = word[l2-1]
        print(spaces)

    #User-defined functions for adding questions in the quiz
    def add1():
        global list1
        print("\nCREATING QUESTIONS FOR 'COUNTRY' QUIZ...")

        #For adding questions based on the number of questions the user want to add
        num = int(input("Enter the number of questions you want to add:"))
        for i in range(num):
            quest = str.title(input("\nEnter your question relating to countries:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list1:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list1:
                list1.append(dict1)

    def add2():
        global list2
        print("\nCREATING QUESTIONS FOR 'CITY' QUIZ...")

        #For adding questions based on the number of questions the user want to add
        num = int(input("Enter the number of questions you want to add:"))
        for i in range(num):
            quest = str.title(input("\nEnter your question relating to cities of India:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list2:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list2:
                list2.append(dict1)

    def add3():
        global list3
        print("\nCREATING QUESTIONS FOR 'KINGS' QUIZ...")

        #For adding questions based on the number of questions the user want to add
        num = int(input("Enter the number of questions you want to add:"))
        for i in range(num):
            quest = str.title(input("\nEnter your question relating to kings of India:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list3:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list3:
                list3.append(dict1)

    def add4():
        global list4
        print("\nCREATING QUESTIONS FOR 'HANGMAN' QUIZ...")

        #For adding questions based on the number of questions the user want to add
        num = int(input("Enter the number of questions you want to add:"))
        for i in range(num):
            quest = str.title(input("\nEnter your question relating to general knowledge:"))
            ans = str.upper(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list4:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list4:
                list4.append(dict1)

    #User-defined functions for modifying the given set of questions of the quiz
    def modify1():
        global list1
        print("\nMODIFYING THE QUESTIONS OF 'COUNTRY' QUIZ...")
        print("TOTAL NUMBER OF QUESTIONS BEFORE MODIFYING:",len(list1))

        #Menu for giving options to modify the questions in different ways
        choice = int(input("""MENU
1. TO ADD A QUESTION, PRESS 1
2. TO REMOVE A QUESTION, PRESS 2
3. TO UPDATE A QUESTION, PRESS 3
ENTER YOUR CHOICE:"""))

        #For adding a question
        if choice == 1:
            quest = str.title(input("\nEnter your question relating to countries:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list1:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list1:
                list1.append(dict1)

        #For removing a question of a particular index
        elif choice == 2:
            if len(list1) == 0:
                print("NO QUESTIONS ARE AVAILABLE TO REMOVE")
            elif len(list1) != 0:
                ind = int(input("\nEnter the index of the question which you want to remove:"))
                if ind in range(len(list1)):
                    item = list1.pop(ind)
                    print("QUESTION REMOVED:",item,end = "\n")
                elif ind not in range(len(list1)):
                    print("The question is not available for the given index")

        #For updating a question of a particular index
        elif choice == 3:
            ind = int(input("\nEnter the index of the question you want to update:"))
            if ind in range(len(list1)):
                print("Question before updating:")
                print(list1[ind])
                quest = str.title(input("Enter your updated question relating to countries of the world:"))
                ans = str.title(input("Enter the answer for your question:"))
                clue = "CLUE: " + str(quest)
                dict1 = {ans:clue}
                list1[ind] = dict1
                print("Question after updating:")
                print(list1[ind])
            elif ind not in range(len(list1)):
                print("Question is not available for the given index to update")
        else:
            print("INVALID INPUT")
        print("TOTAL NUMBER OF QUESTIONS AFTER MODIFYING:",len(list1))

    def modify2():
        global list2
        print("\nMODIFYING THE QUESTIONS OF 'CITY' QUIZ...")
        print("TOTAL NUMBER OF QUESTIONS BEFORE MODIFYING:",len(list2))

        #Menu for giving options to modify the questions in different ways
        choice = int(input("""MENU
1. TO ADD A QUESTION, PRESS 1
2. TO REMOVE A QUESTION, PRESS 2
3. TO UPDATE A QUESTION, PRESS 3
ENTER YOUR CHOICE:"""))

        #For adding a question
        if choice == 1:
            quest = str.title(input("\nEnter your question relating to cities of India:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list2:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list2:
                list2.append(dict1)

        #For removing a question of a particular index
        elif choice == 2:
            if len(list2) == 0:
                print("NO QUESTIONS ARE AVAILABLE TO REMOVE")
            elif len(list2) != 0:
                ind = int(input("\nEnter the index of the question which you want to remove:"))
                if ind in range(len(list2)):
                    item = list2.pop(ind)
                    print("QUESTION REMOVED:",item,end = "\n")
                elif ind not in range(len(list2)):
                    print("The question is not available for the given index")

        #For updating a question of a particular index
        elif choice == 3:
            ind = int(input("\nEnter the index of the question you want to update:"))
            if ind in range(len(list2)):
                print("Question before updating:")
                print(list2[ind])
                quest = str.title(input("Enter your updated question relating to cities of India:"))
                ans = str.title(input("Enter the answer for your question:"))
                clue = "CLUE: " + str(quest)
                dict1 = {ans:clue}
                list2[ind] = dict1
                print("Question after updating:")
                print(list2[ind])
            elif ind not in range(len(list2)):
                print("Question is not available for the given index to update")
        else:
            print("INVALID INPUT")
        print("TOTAL NUMBER OF QUESTIONS AFTER MODIFYING:",len(list2))

    def modify3():
        global list3
        print("\nMODIFYING THE QUESTIONS OF 'KINGS' QUIZ...")
        print("TOTAL NUMBER OF QUESTIONS BEFORE MODIFYING:",len(list3))

        #Menu for giving options to modify the questions in different ways
        choice = int(input("""MENU
1. TO ADD A QUESTION, PRESS 1
2. TO REMOVE A QUESTION, PRESS 2
3. TO UPDATE A QUESTION, PRESS 3
ENTER YOUR CHOICE:"""))

        #For adding a question
        if choice == 1:
            quest = str.title(input("\nEnter your question relating to kings of India:"))
            ans = str.title(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list3:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list3:
                list3.append(dict1)

        #For removing a question of a particular index
        elif choice == 2:
            if len(list3) == 0:
                print("NO QUESTIONS ARE AVAILABLE TO REMOVE")
            elif len(list3) != 0:
                ind = int(input("\nEnter the index of the question which you want to remove:"))
                if ind in range(len(list3)):
                    item = list3.pop(ind)
                    print("QUESTION REMOVED:")
                    print(item)
                elif ind not in range(len(list3)):
                    print("The question is not available for the given index")

        #For updating a question of a particular index
        elif choice == 3:
            ind = int(input("\nEnter the index of the question you want to update:"))
            if ind in range(len(list3)):
                print("Question before updating:")
                print(list3[ind])
                quest = str.title(input("Enter your updated question relating to kings of India:"))
                ans = str.title(input("Enter the answer for your question:"))
                clue = "CLUE: " + str(quest)
                dict1 = {ans:clue}
                list3[ind] = dict1
                print("Question after updating:")
                print(list3[ind])
            elif ind not in range(len(list3)):
                print("Question is not available for the given index to update")
        else:
            print("INVALID INPUT")
        print("TOTAL NUMBER OF QUESTIONS AFTER MODIFYING:",len(list3))

    def modify4():
        global list4
        print("\nMODIFYING THE QUESTIONS OF 'HANGMAN' QUIZ...")
        print("TOTAL NUMBER OF QUESTIONS BEFORE MODIFYING:",len(list4))

        #Menu for giving options to modify the questions in different ways
        choice = int(input("""MENU
1. TO ADD A QUESTION, PRESS 1
2. TO REMOVE A QUESTION, PRESS 2
3. TO UPDATE A QUESTION, PRESS 3
ENTER YOUR CHOICE:"""))

        #For adding a question
        if choice == 1:
            quest = str.title(input("\nEnter your question relating to general knowledge:"))
            ans = str.upper(input("Enter the answer for your question:"))
            clue = "CLUE: " + str(quest)
            dict1 = {ans:clue}
            if dict1 in list4:
                print("YOUR QUESTION IS ALREADY AVAILABLE IN THE QUIZ")
            elif dict1 not in list4:
                list4.append(dict1)

        #For removing a question of a particular index
        elif choice == 2:
            if len(list4) == 0:
                print("NO QUESTIONS ARE AVAILABLE TO REMOVE")
            elif len(list4) != 0:
                ind = int(input("\nEnter the index of the question which you want to remove:"))
                if ind in range(len(list4)):
                    item = list4.pop(ind)
                    print("QUESTION REMOVED:")
                    print(item)
                elif ind not in range(len(list4)):
                    print("The question is not available for the given index")

        #For updating a question of a particular index
        elif choice == 3:
            ind = int(input("\nEnter the index of the question you want to update:"))
            if ind in range(len(list4)):
                print("Question before updating:")
                print(list4[ind])
                quest = str.title(input("Enter your updated question relating to general knowledge:"))
                ans = str.upper(input("Enter the answer for your question:"))
                clue = "CLUE: " + str(quest)
                dict1 = {ans:clue}
                list4[ind] = dict1
                print("Question after updating:")
                print(list4[ind])
            elif ind not in range(len(list4)):
                print("Question is not available for the given index to update")
        else:
            print("INVALID INPUT")
        print("TOTAL NUMBER OF QUESTIONS AFTER MODIFYING:",len(list4))

    #A text file for displaying the instructions for playing the quiz
    ins1 = open("INSTRUCTIONS.txt","w")
    ins1.write("""INSTRUCTIONS TO PLAY:
1. The game is a quiz where you will be asked to answer the questions with the help of the given clues.
2. There are three different quizzes available and the player can choose any of these three.
3. The player will be asked to enter their name and will be given a particular id.
4. The player needs to enter the correct answer for the given question and points will be awarded based on the number of tries taken by the player to answer correctly.
5. If the player scores 5 points in any of these 3 quizzes, the player will get a bonus opportunity to modify the questions of the quiz in which they won.
6. The bonus chance will be given to the player only once, so the player is requested to play wisely.""")
    ins1.close()

    ins2 = open("INSTRUCTIONS.txt","r")
    rules = ins2.read()
    print(rules)
    ins2.close()

    list1,list2,list3,list4 = [],[],[],[]
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []

    #Multiple binary files for writing and reading the questions of the quiz
    try:
        bin_file1 = open("COUNTRY.dat","rb")
        list1 = pickle.load(bin_file1)
        bin_file1.close()
    except:
        list1 = []

    try:
        bin_file2 = open("CITY.dat","rb")
        list2 = pickle.load(bin_file2)
        bin_file2.close()
    except:
        list2 = []

    try:
        bin_file3 = open("KINGS.dat","rb")
        list3 = pickle.load(bin_file3)
        bin_file3.close()
    except:
        list3 = []

    try:
        bin_file4 = open("HANGMAN.dat","rb")
        list4 = pickle.load(bin_file4)
        bin_file4.close()
    except:
        list4 = []
        
        
    while True:
        #Menu for choosing the game to play
        choice = input("""\nMENU
1. FOR CREATING QUESTIONS, EXCLUSIVE FOR EXAMINERS:
    a. DO YOU WANT TO CREATE QUESTIONS FOR 'COUNTRY' QUIZ, PRESS 1a
    b. DO YOU WANT TO CREATE QUESTIONS FOR 'CITY' QUIZ, PRESS 1b
    c. DO YOU WANT TO CREATE QUESTIONS FOR 'KINGS' QUIZ, PRESS 1c
    d. DO YOU WANT TO CREATE QUESTIONS FOR 'HANGMAN' QUIZ, PRESS 1d
2. FOR PLAYING QUIZ:
    1. DO YOU HAVE GREAT KNOWLEDGE ABOUT COUNTRIES, IF SO 2a
    2. DO YOU HAVE GREAT KNOWLEDGE ABOUT CITIES OF INDIA, IF SO 2b
    3. DO YOU HAVE GREAT KNOWLEDGE ABOUT KINGS OF INDIA, IF SO 2c
    4. DO YOU WANT TO PLAY HANGMAN, IF SO 2d
3. TO EXIT, IF SO 3
ENTER YOUR CHOICE:""")
        #Adding the questions
        if choice == "1a":
            add1()
            
        elif choice == "1b":
            add2()
            
        elif choice == "1c":
            add3()
            
        elif choice == "1d":
            add4()

        #Quiz on various countries
        elif choice == "2a":
            print("\nQUIZ ON COUNTRIES OF THE WORLD")
            game = "COUNTRY"
            name = input("Enter your name:").title()

            #To get a unique player id
            num = random.randint(1,999)
            while num not in lst1:
                lst1.append(num)
            else:
                num = random.randint(1,999)
            player_id = "CY0" + str(num)
            print("Your id:",format(player_id,'03d'))

            #To append and read the questions of "COUNTRY" quiz stored in the corresponding binary file
            dump1 = open("COUNTRY.dat","ab")
            pickle.dump(list1,dump1)
            dump1.close()
            try:
                load1 = open("COUNTRY.dat","rb")
                list1 = pickle.load(load1)
                load1.close()
            except:
                list1 = []
            while list1 == []:
                add1()
                break
            else:
                x = random.randrange(0,len(list1))
                qa = list1[x]
                ky = qa.keys()
                for i in ky:
                    word = i
                    print(qa[i])
                quiz()
                points = 0
                tries = 0
                for i in range(0,5):
                    guess = input("Guess the country:")
                    if guess == word:
                        print("Congratulations!! You Win!!!\nThe word was",word)

                        #Points scale
                        if tries == 0:
                            points += 5
                        elif tries == 1:
                            points += 4
                        elif tries == 2:
                            points += 3
                        elif tries == 3:
                            points += 2
                        elif tries == 4:
                            points += 1
                        break
                    elif 5-i == 1:
                        points = 0
                        print("You lose, the word is",word)
                    else:
                        print("You might be a loser but you can always try again")
                        tries += 1
                print("YOUR SCORE:",points)
                if points == 5:
                    print("Congratulations!! You got a chance to modify the questions of this 'COUNTRY' quiz")
                    modify1()
                else:
                    pass
                cur.execute("insert into LEADERBOARD values('%s','%s','%s',%s)"%(player_id,name,game,points))

                #Binary file for writing the questions
                dump2 = open("COUNTRY.dat","wb")
                pickle.dump(list1,dump2)
                dump2.close()
            print("EXITING THE 'COUNTRY' QUIZ...\n")

        #Quiz on various cities of India
        elif choice == "2b":
            print("\nQUIZ ON CITIES OF INDIA")
            game = "CITY"
            name = input("Enter your name:").title()

            #To get a unique player id
            num = random.randint(1,999)
            while num not in lst2:
                lst2.append(num)
            else:
                num = random.randint(1,999)
            player_id = "CI0" + str(num)
            print("Your id:",format(player_id,'03d'))

            #To append and read the questions of "CITY" quiz stored in the corresponding binary file
            dump1 = open("CITY.dat","ab")
            pickle.dump(list2,dump1)
            dump1.close()
            try:
                load1 = open("CITY.dat","rb")
                list2 = pickle.load(load1)
                load1.close()
            except:
                list2 = []
            while list2 == []:
                add2()
                break
            else:
                x = random.randrange(0,len(list2))
                qa = list2[x]
                ky = qa.keys()
                for i in ky:
                    word = i
                    print(qa[i])
                quiz()
                points = 0
                tries = 0
                for i in range(0,5):
                    guess = input("Guess the city of India:")
                    if guess == word:
                        print("Congratulations!! You Win!!!\nThe word was",word)

                        #Points scale
                        if tries == 0:
                            points += 5
                        elif tries == 1:
                            points += 4
                        elif tries == 2:
                            points += 3
                        elif tries == 3:
                            points += 2
                        elif tries == 4:
                            points += 1
                        break
                    elif 5-i == 1:
                        points = 0
                        print("You lose, the word is",word)
                    else:
                        print("You might be a loser but you can always try again")
                        tries += 1
                print("YOUR SCORE:",points)
                if points == 5:
                    print("Congratulations!! You got a chance to modify the questions of this 'CITY' quiz")
                    modify2()
                else:
                    pass
                cur.execute("insert into LEADERBOARD values('%s','%s','%s',%s)"%(player_id,name,game,points))

                #Binary file for writing the questions
                dump2 = open("CITY.dat","wb")
                pickle.dump(list2,dump2)
                dump2.close()
            print("EXITING THE 'CITY' QUIZ...\n")

        #Quiz on various kings of India
        elif choice == "2c":
            print("\nQUIZ ON KINGS OF INDIA")
            game = "KINGS"
            name = input("Enter your name:").title()

            #To get a unique player id
            num = random.randint(1,99)
            while num not in lst3:
                lst3.append(num)
            else:
                num = random.randint(1,99)
            player_id = "KG0" + str(num)
            print("Your id:",format(player_id,'03d'))

            #To append and read the questions of "KINGS" quiz stored in the corresponding binary file 
            dump1 = open("KINGS.dat","ab")
            pickle.dump(list3,dump1)
            dump1.close()
            try:
                load1 = open("KINGS.dat","rb")
                list3 = pickle.load(load1)
                load1.close()
            except:
                list3 = []
            while list3 == []:
                add3()
                break
            else:
                x = random.randrange(0,len(list3))
                qa = list3[x]
                ky = qa.keys()
                for i in ky:
                    word = i
                    print(qa[i])
                quiz()
                points = 0
                tries = 0
                for i in range(0,5):
                    guess = input("Guess the king of India:")
                    if guess == word:
                        print("Congratulations!! You Win!!!\nThe word was",word)

                        #Points scale
                        if tries == 0:
                            points += 5
                        elif tries == 1:
                            points += 4
                        elif tries == 2:
                            points += 3
                        elif tries == 3:
                            points += 2
                        elif tries == 4:
                            points += 1
                        break
                    elif 5-i == 1:
                        points = 0
                        print("You lose, the word is",word)
                    else:
                        print("You might be a loser but you can always try again")
                        tries += 1
                print("YOUR SCORE:",points)
                if points == 5:
                    print("Congratulations!! You got a chance to modify the questions of this 'KINGS' quiz")
                    modify3()
                else:
                    pass
                cur.execute("insert into LEADERBOARD values('%s','%s','%s',%s)"%(player_id,name,game,points))

                #Binary file for writing questions
                dump2 = open("KINGS.dat","wb")
                pickle.dump(list3,dump2)
                dump2.close()
            print("EXITING THE 'KINGS' QUIZ...\n")

        #Quiz on General Knowledge
        elif choice == "2d":
            print("\nHANGMAN QUIZ")
            game = "HANGMAN"
            spe1 = open("SPECIAL.txt","w")
            spe1.write("""SPECIAL INSTRUCTIONS:
1. This is a hangman quiz where the player will be asked to enter their name.
2. The player will be registered with a particular player id.
3. The player needs to answer correctly for the given question, otherwise points won't be awarded.
4. Points are awarded to based on the number of tries taken by the player to answer the question correctly.
5. If the player repeats their guess, then their chance to find the answer will be deducted.
6. If the player scores 5 points in this hangman quiz, the player will get a bonus reward to modify the questions of the hangman quiz.
7. The bonus chance will be given to the player only once, so the player is requested to play wisely.
""")
            spe1.close()
            spe2 = open("SPECIAL.txt","r")
            spe_rules = spe2.read()
            print(spe_rules)
            spe2.close()
            name = input("Enter your name:").title()

            #To get a unique player id
            num = random.randint(1,999)
            while num not in lst4:
                lst4.append(num)
            else:
                num = random.randint(1,999)
            player_id = "HN0" + str(num)
            print("Your id:",format(player_id,'03d'))

            #To append and read questions of "HANGMAN" quiz stored in the corresponding binary file
            dump1 = open("HANGMAN.dat","ab")
            pickle.dump(list4,dump1)
            dump1.close()
            try:
                load1 = open("HANGMAN.dat","rb")
                list4 = pickle.load(load1)
                load1.close()
            except:
                list4 = []
            if list4 == []:
                add4()
                pass
            else:
                x = random.randrange(0,len(list4))
                qa = list4[x]
                ky = qa.keys()
                for i in ky:
                    print(qa[i])
                    secret = i
                    print("Letters to be filled: ","-"*len(secret))
                points = 0
                normal = """
                __________
                |    |
                |
                |
                |
                |
              -------"""
                a = """
                __________
                |    |
                |    O
                |
                |
                |
              -------"""
                b = """
                __________
                |    |
                |    O
                |    |
                |
                |
              -------"""
                c = """
                __________
                |    |
                |    O
                |  --|--
                |
                |
              -------"""
                d = """
                __________
                |    |
                |    O
                |  --|--
                |   /
                |
              -------"""
                e = """
                __________
                |    |
                |    O
                |  --|--
                |   / \\
                |
              -------"""
                hang = [normal,a,b,c,d,e]
                count = 0
                user = ""
                tries = 5
                words = []
                print(normal,end = "\n")
                while tries > 0:
                    guess = str.upper(input("Enter your alphabet guess:"))
                    if 0 < len(guess) < 2 and (guess.isalpha() or guess == " "):
                        if guess in words:
                            print("You have entered the letter you have already guessed!!\nGuess any other letter!!")
                            tries -= 1
                            count += 1
                            print("Number of tries left:",tries)
                        elif guess in secret:
                            print("Correct!! You found a letter of the secret word")
                            words.append(guess)
                        else:
                            tries -= 1
                            count += 1
                            print("Wrong guess!! Try again!!\nNumber of tries left:",tries)
                        user += guess
                        num = 0
                        print(hang[count],"\n")
                        for guess in secret:
                            if guess in user:
                                print(guess,end = " ")
                            else:
                                print("_",end = " ")
                                num += 1
                        print("\n")

                        #Points scale
                        if num == 0:
                            print("Congratulations!! You win!!\nThe secret word was:",secret)
                            if tries == 5:
                                points += 5
                            elif tries == 4:
                                points += 4
                            elif tries == 3:
                                points += 3
                            elif tries == 2:
                                points += 2
                            elif tries == 1:
                                points += 1
                            break
                        else:
                            pass
                    else:
                        print("INVALID")
                else:
                    print("YOU LOSE")
                    print("The secret word:",secret)
                print("Your points:", points)
                if points == 5:
                    print("Congratulations!! You got a chance to modify the questions of this 'HANGMAN' quiz")
                    modify4()
                else:
                    pass
                cur.execute("insert into LEADERBOARD values('%s','%s','%s',%s)"%(player_id,name,game,points))

                #Binary file for writing questions
                dump2 = open("HANGMAN.dat","wb")
                pickle.dump(list4,dump2)
                dump2.close()
            print("EXITING THE 'HANGMAN' QUIZ...\n")

        #Closing the options for playing the quizzes    
        elif choice == "3":
            print("\nCLOSING THE OPTIONS FOR PLAYING...")
            print("THANK YOU FOR PLAYING")
            print("\nBEFORE SEEING THE LEADERBOARD, HAVE A LOOK AT THE QUESTIONS AND ANSWERS MADE")

            #To display the questions in all the quizzes after playing
            dump1 = open("COUNTRY.dat","wb")
            pickle.dump(list1,dump1)
            dump1.close()
            try:
                load1 = open("COUNTRY.dat","rb")
                print("QUESTIONS OF 'COUNTRY' QUIZ ALONG WITH ANSWERS:")
                list1 = pickle.load(load1)
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                print("|{:25}|{:86}|".format("ANSWER","QUESTION"))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                for i in list1:
                    for j in i.keys():
                        print("|{:25}|{:86}|".format(j,i.get(j)))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                load1.close()
            except:
                print("\nQUESTIONS ARE NOT AVAILABLE IN THE 'COUNTRY' QUIZ")

            dump2 = open("CITY.dat","wb")
            pickle.dump(list2,dump2)
            dump2.close()
            try:
                load2 = open("CITY.dat","rb")
                print("\nQUESTIONS OF 'CITY' QUIZ ALONG WITH ANSWERS:")
                list2 = pickle.load(load2)
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                print("|{:25}|{:86}|".format("ANSWER","QUESTION"))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                for i in list2:
                    for j in i.keys():
                        print("|{:25}|{:86}|".format(j,i.get(j)))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                load2.close()
            except:
                print("\nQUESTIONS ARE NOT AVAILABLE IN THE 'CITY' QUIZ")

            dump3 = open("KINGS.dat","wb")
            pickle.dump(list3,dump3)
            dump3.close()
            try:
                load3 = open("KINGS.dat","rb")
                print("\nQUESTIONS OF 'KINGS' QUIZ ALONG WITH ANSWERS:")
                list3 = pickle.load(load3)
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                print("|{:25}|{:86}|".format("ANSWER","QUESTION"))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                for i in list3:
                    for j in i.keys():
                        print("|{:25}|{:86}|".format(j,i.get(j)))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                load3.close()
            except:
                print("\nQUESTIONS ARE NOT AVAILABLE IN THE 'KINGS' QUIZ")

            dump4 = open("HANGMAN.dat","wb")
            pickle.dump(list4,dump4)
            dump4.close()
            try:
                load4 = open("HANGMAN.dat","rb")
                print("\nQUESTIONS OF 'HANGMAN' QUIZ ALONG WITH ANSWERS:")
                list4 = pickle.load(load4)
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                print("|{:25}|{:86}|".format("ANSWER","QUESTION"))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                for i in list4:
                    for j in i.keys():
                        print("|{:25}|{:86}|".format(j,i.get(j)))
                print("""+-------------------------+--------------------------------------------------------------------------------------+""")
                load4.close()
            except:
                print("\nQUESTIONS ARE NOT AVAILABLE IN THE 'HANGMAN' QUIZ")
            break
        
        else:
            print("\nPLEASE INPUT THE CORRECT CHOICE!!")

    #Selecting all the records from the table "LEADERBOARD"
    data1 = []
    head = ["ID","NAME","QUIZ","POINTS"]
    cur.execute("select * from LEADERBOARD order by POINTS DESC")
    rec1 = cur.fetchall()
    for i in rec1:
        d1 = list(i)
        data1.append(d1)

    #Displaying the total points according to the user name and the number of times they played in total
    data2 = []
    field = ["NAME","TOTAL POINTS","TIMES PLAYED","AVERAGE"]
    cur.execute("select NAME, SUM(POINTS) TOTAL_POINTS, COUNT(QUIZ) TIMES_PLAYED, ROUND(AVG(POINTS),2) AVERAGE from LEADERBOARD group by NAME order by NAME DESC")
    rec2 = cur.fetchall()
    for i in rec2:
        d2 = list(i)
        data2.append(d2)

    #CSV files for writing and reading the data of "LEADERBOARD" table
    if data1 == []:
        with open("GAME.csv","w",newline = "") as game1:
            p = csv.writer(game1)
            p.writerow(head)
            p.writerows(data1)

    elif data1 != []:
        with open("GAME.csv","a",newline = "") as game2:
            q = csv.writer(game2)
            q.writerow(head)
            q.writerows(data1)

    #CSV files for writing and reading data of "TIMES PLAYED" table
    if data2 == []:
        with open("TIMES.csv","w",newline = "") as game3:
            p = csv.writer(game3)
            p.writerow(field)
            p.writerows(data2)

    elif data2 != []:
        with open("TIMES.csv","a",newline = "") as game4:
            p = csv.writer(game4)
            p.writerow(field)
            p.writerows(data2)

    #For displaying the leaderboard
    if data1 == []:
        print("\nNO ONE HAS STARTED PLAYING THE QUIZ...")
    else:
        print("\nLEADERBOARD:")
        with open("GAME.csv","r") as game5:
            q = csv.reader(game5)
            record1 = list(q)
            print("""+------+---------------------+-------------------------------+----------+""")
            print("|{:6}|{:21}|{:31}|{:10}|".format(record1[0][0],record1[0][1],record1[0][2],record1[0][3]))
            print("""+------+---------------------+-------------------------------+----------+""")
            for j in range(1,len(record1)):
                print("|{:6}|{:21}|{:31}|{:10}|".format(record1[j][0],record1[j][1],record1[j][2],record1[j][3]))
            print("""+------+---------------------+-------------------------------+----------+""")
        
        #To display the board for number of times played
        print("\nTIMES PLAYED:")
        with open("TIMES.csv","r") as game6:
            r = csv.reader(game6)
            record2 = list(r)
            print("""+---------------------+---------------+---------------+---------------+""")
            print("|{:21}|{:15}|{:15}|{:15}|".format(record2[0][0],record2[0][1],record2[0][2],record2[0][3]))
            print("""+---------------------+---------------+---------------+---------------+""")
            for j in range(1,len(record2)):
                print("|{:21}|{:15}|{:15}|{:15}|".format(record2[j][0],record2[j][1],record2[j][2],record2[j][3]))
            print("""+---------------------+---------------+---------------+---------------+""")
        
        #To display the player who has dominated the quiz
        try:
            cur.execute("SELECT NAME, AVG(POINTS), COUNT(NAME) FROM LEADERBOARD GROUP BY NAME HAVING COUNT(NAME) >= 3 ORDER BY AVG(POINTS) DESC")
            dom_player = cur.fetchone()
            print("\nTHE PLAYER WHO HAS DOMINATED THE QUIZ SO FAR WITH A HIGH AVERAGE IS", dom_player[0].title())
            print(dom_player[0].title(),"HAS PLAYED", dom_player[2],"TIMES WITH AN AVERAGE OF", round(dom_player[1],2))
        except:
            print("NONE OF THE PLAYERS HAVE PLAYED A MINIMUM OF 3 TIMES")

    #To delete all the records of the table
    d = input("\nDO YOU WANT TO DELETE ALL THE RECORDS?(Y/N):").upper()
    print()
    if d == "Y":
        cur.execute("drop table LEADERBOARD")
        print("ALL RECORDS ARE DELETED SUCCESSFULLY")
    elif d == "N":
        print("NOTHING IS DELETED")
                
    #For making permanent changes in the table
    handle.commit()

    #Closing the interface connection of Python with MySQL
    handle.close()

    #Ratings and Feedback
    print("\nPLEASE ENTER YOUR RATING AND FEEDBACK BEFORE EXITING")
    rating = input("YOUR RATING(OUT OF 5):")
    feedback = input("YOUR FEEDBACK:")
    print("THANK YOU FOR YOUR RATING AND FEEDBACK")

except:
    print("THE GIVEN USER ID AND PASSWORD IS INCORRECT...TRY LOGGING IN AGAIN")
