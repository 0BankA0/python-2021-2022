#!/usr/bin/python3

import sys
import random
import re
import sqlite3

while True:

    class RockPaperScissors:
        def __init__(self): #Define __init__ method
            print("\n\nThis is a Rock, Paper, Scissors game where you can play against a computer. \nThe one who first gets three wins is the champion.\n")

        def menu(self): #Define menu method which displays the menu of the program
            user_input = input("--- MENU --- \nLogin & Play (1) \nCreate a New User (2) \nStatistics (3)\nExit game (4)\n\n")
            #The player is given an option to choose from four different options
            if user_input == "1":
                pass
            elif user_input == "2":
                self.new_user() #If the answer is '2', go to new_user method
            elif user_input == "3":
                self.statistics() #If the answer is '3', go to statistics method
            elif user_input == "4":
                print ("\nThanks for playing!")
                sys.exit() #If the answer is '4', end the running program
            else:
                print ("Please give a valid answer (1),(2),(3) or (4).\n")
                self.menu() #If the answer is invalid, return to menu method

        def player1_username(self): #Define player1_username method where player input a new username for their user
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            player1_username_input = input("Player 1, please give me your username: \n\n")
            self.player1_username_input = player1_username_input
            if not re.match("^[a-zA-Z0-9 _]*$", self.player1_username_input): #Checks that only letters, numbers or spaces are given
                print("Please enter a valid username using only letters, numbers and spaces.")
                database_connection.close() #Closes the connection to database
                self.player1_username() #Goes back to player1_username method if the username is invalid
            cursor = database_connection.execute("select exists(SELECT * from USERS where USERNAME = '{0}')".format(player1_username_input)) 
            for username in cursor: #Checks if the username exists in database 
                pass
            if username[0] == 1:
                pass
            elif username[0] == 0:
                print ("\nThe username was not found in the database. You must create a user if you haven't got one.\n")
                database_connection.close() #Closes the connection to database
                self.menu() #Returns to the menu if the username was not found in the database
            else:
                print("Something unexpected happened. Please try again")
                sys.exit()   

        def player1_password(self): #Define player1_password method where players input a password for their existing user
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            player1_password_input = input("Please give me your password: \n\n")
            if not re.match("^[a-zA-Z0-9 _]*$", player1_password_input): #Checks that only letters, numbers or spaces are given
                print("You can only enter a password with letters, numbers and spaces.")
                database_connection.close() #Closes the connection to database
                self.player1_password() #Goes back to player1_password method if the password is invalid
            cursor = database_connection.execute("select exists(SELECT * from USERS where PASSWORD = '{0}' AND USERNAME = '{1}')".format(player1_password_input,self.player1_username_input))
            for password in cursor: #Checks if the password matches to the given username in database
                pass
            if password[0] == 1:
                print ("Login successful ")
                database_connection.close() #Closes the connection to database if the login was successfull
            elif password[0] == 0:
                print ("The password doesn't match with the given username. Please try again.")
                self.player1_password() #If the password desn't match, the password is being asked again from the player
            else:
                print("Something unexpected happened. Please try again")
                sys.exit()

        def new_user(self): #Define new_user method where players can create a new user
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            new_user_username_input = input("Hi, please give me your new username. \n\n")
            if not re.match("^[a-zA-Z0-9 _]*$", new_user_username_input): #Checks that only letters, numbers or spaces are given
                print("Please enter a valid username. (Only letters and numbers allowed)")
                self.new_user() #Goes back to new_user method if the username is invalid
            cursor = database_connection.execute("select exists(SELECT * from USERS where USERNAME = '{0}')".format(new_user_username_input))
            for username in cursor:
                pass
            if username[0] == 1:
                print("This username is already taken. Please provide a different one.")
                self.new_user() #If the username is already taken, it goes back to new_user method
            elif username[0] == 0:
                pass
            else:
                print("Something unexpected happened. Please try again")
                sys.exit()    
            new_user_password_input = input("Please give me your new password. \n\n")
            if not re.match("^[a-zA-Z0-9 _]*$", new_user_password_input): #Checks that only letters, numbers or spaces are given
                print("Please enter a valid username and password combination. (Only letters and numbers allowed)")
                self.new_user() #Goes back to new_user method if the password is invalid
            print ("Creating new user... \n")
            database_connection.execute("INSERT INTO USERS (USERNAME,PASSWORD,WINS,LOSES,GAMESPLAYED,WINPERCENT) \
            VALUES ('{0}', '{1}',0,0,0,0)".format(new_user_username_input, new_user_password_input)); #Inserts the new user to the database
            database_connection.commit() #Performs a commit to the database
            database_connection.close() #Closes the connection to database
            print ("New user created successfully!\n")
            self.menu() #Returns to the menu method

        def statistics(self): #Define statistics method where statistics about the users are shown
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            print("Here are the top 10 players in the order, who has the highest winning percentage\n")
            order = database_connection.execute("SELECT USERNAME, WINS, LOSES, GAMESPLAYED, WINPERCENT FROM USERS ORDER BY WINPERCENT DESC LIMIT 10")
        #The query selects the top 10 users from database in the order that who has the highest winning percentage
            database_connection.commit() #Performs a commit to the database
            for row in order:
                print ("Username = ", row[0])
                print ("Wins = ", int(row[1]))
                print ("Loses = ", int(row[2]))
                print ("Games played = ", int(row[3]))
                print ("Winning percent = ", row[4], "\n");
            database_connection.close() #Closes the connection to database
            self.menu() #Returns to the menu method

        def win_messages(self): #Define win_messages method where the winning messages are shown after a win from one round of the game
            self.player1_win_message = ("Congrats {0}, you won computer in the game!".format(self.player1_username_input))
            self.computer_win_message = ("Too bad {0}, computer won you in the game!".format(self.player1_username_input))
            self.player1_games_won = 0 #Initializes the player1_games_won variable
            self.computer_games_won = 0 #Initializes the computer_games_won variable

        def player1_congrats(self): #Define player1_congrats method where the winning message for player1 is shown after winning three rounds against computer
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            print ("Gongrats {0}, you are the champion!\n".format(self.player1_username_input)) #Displays a winning message for player1
            database_connection.execute("UPDATE USERS set WINS = WINS + 1 where USERNAME = '{0}'".format(self.player1_username_input));
            database_connection.execute("UPDATE USERS set GAMESPLAYED = WINS + LOSES where USERNAME = '{0}'".format(self.player1_username_input));
            database_connection.execute("UPDATE USERS set WINPERCENT = WINS/GAMESPLAYED*100 where USERNAME = '{0}'".format(self.player1_username_input));
        #The querys above update the WINS, LOSES, GAMESPLAYED and WINPERCENT tables in the database
            database_connection.commit() #Performs a commit to the database
            database_connection.close() #Closes the connection to database

        def computer_congrats(self): #Define computer_congrats method
            database_connection = sqlite3.connect('test.db') #Connects to a 'test.db' database
            print ("Too bad {0}, computer is the champion!\n".format(self.player1_username_input)) #Displays a winning message for computer
            database_connection.execute("UPDATE USERS set LOSES = LOSES + 1 where USERNAME = '{0}'".format(self.player1_username_input));
            database_connection.execute("UPDATE USERS set GAMESPLAYED = WINS + LOSES where USERNAME = '{0}'".format(self.player1_username_input));
            database_connection.execute("UPDATE USERS set WINPERCENT = WINS/GAMESPLAYED*100 where USERNAME = '{0}'".format(self.player1_username_input));
        #The querys above update the WINS, LOSES, GAMESPLAYED and WINPERCENT tables in the database
            database_connection.commit() #Performs a commit to the database
            database_connection.close() #Closes the connection to database

        def new_game(self): #Define new_game method where player1 is being asked to play another round
            self.new_game_choice = str.lower(str.strip(input("Do you want to play another round? (yes/no)\n\n")))
            if self.new_game_choice == "yes":                
                print("Great!\n\n") #If the player chooses 'yes', the program is started again
            elif self.new_game_choice == "no":
                print("Thanks for playing!")
                sys.exit() #Exit the running program
            else:
                print("Please enter a yes or no as an answer")
                self.new_game() #Call the new_game method again if the answer is invalid

        def player1_choice(self): #Define player1_choice method asks the player1's input in the choice between rock, paper and scissors
            self.player1_guess = str.lower(str.strip(input("So {0} rock, paper or scissors?\n\n".format(self.player1_username_input))))   
            if self.player1_guess == "rock":
                self.player1_num = 1
            elif self.player1_guess == "paper":
                self.player1_num = 2
            elif self.player1_guess == "scissors":
                self.player1_num = 3
            else:
                print ("Please only insert rock, paper or scissors as an answer!")
                self.player1_choice() #Call the p1_choice method again if the answer is invalid

        def computer_choice(self): #Define computer_choice method defined what option the computer chooses based on a random number
            self.computer_num = random.randrange(1,4)
            if self.computer_num == 1:
                print("The computer chose rock")
            elif self.computer_num == 2:
                print("The computer chose paper")
            elif self.computer_num == 3:
                print("The computer chose scissors")

        def results(self): #Define results method the displays what the current results are for the game
            difference = self.computer_num - self.player1_num
            if difference == 0:
                print ("It's a tie!")
            elif difference % 3 == 1: #If the computer won the round, the difference is 1
                self.computer_games_won+=1
                print (self.computer_win_message)
            elif difference % 3 == 2: #If the user won the round, the difference is 2
                self.player1_games_won+=1
                print (self.player1_win_message)
            print ("So far {0} has won {1} times, and computer has won {2} times".format(self.player1_username_input,self.player1_games_won,self.computer_games_won))              


    user = RockPaperScissors()
    user.menu()
    user.player1_username()
    user.player1_password()
    user.win_messages()
    user.player1_choice()
    user.computer_choice()
    user.results() 
    while True:
        if user.player1_games_won == 3: #If the player 1 won three rounds against computer, call the player1_congrats method
            user.player1_congrats()
            user.new_game()
            break
        elif user.computer_games_won == 3: #If the computer won three rounds against user, call the ccomputer_congrats method
            user.computer_congrats()
            user.new_game()
            break
        else: #If either has yet won three rounds go back to player1_choice, computer_choice and results methods
            user.player1_choice() 
            user.computer_choice()
            user.results()