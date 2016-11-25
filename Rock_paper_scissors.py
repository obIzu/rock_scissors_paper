player1 = raw_input("Rock, Scissors or Paper: ")
player2 = raw_input("Rock, Scissors or Paper: ")

def rock_scissors_paper(player1, player2):
 
 if player1 == "Rock" and player2 == "Scissors":
    print "player 1 wins"
 elif player2 == "Rock" and player1 == "Scissors":
    print "player 2 wins"
 elif player1 == "Scissors" and player2 == "Paper":
    print "player 1 wins"
 elif player2 == "Scissors" and player1 == "Paper":
    print "player 2 wins"
 elif player1 == "Paper" and player2 == "Rock":
    print "player 1 wins"
 elif player2 == "Paper" and player1 == "Rock":
    print "player 2 wins"
rock_scissors_paper(player1,player2)

x = 1
while x == 1:    
 Question = raw_input("You want to start a new game. Yes or No?")
 if Question == "Yes":
    player1 = raw_input("Rock, Scissors or Paper: ")
    player2 = raw_input("Rock, Scissors or Paper: ")
    rock_scissors_paper(player1, player2)
 else:
    print "Goodbye and thank you"
    break
