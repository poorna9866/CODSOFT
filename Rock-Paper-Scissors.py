import random
def a(user,comp):
    us=0
    cs=0
    if user==comp:
        us=us+0
        cs=cs+0
    elif user=='Rock' and comp=='Scissors':
        us=us+1
    elif user=='Rock' and comp=='Paper':
        cs=cs+1
    elif user=='Paper' and comp=='Rock':
        us=us+1
    elif user=='Paper' and comp=='Scissors':
        cs=cs+1
    elif user=='Scissors' and comp=='Rock':
        cs=cs+1
    else:
        us=us+1
    return us,cs

def game():
    print("1.Rock\n2.Paper\n3.Scissors\n")
    print("Enter your choice between 1 to 3: ")
    num=int(input())
    s=['Rock','Paper','Scissors']
    comp=random.choice(s)
    print("User\'s Choice is: "+s[num-1])
    print("Computer\'s choice is: "+comp)
    user_scores,computer_scores=a(s[num-1],comp)
    if user_scores>computer_scores:
        res="USER Won"
    elif user_scores<computer_scores:
        res="COMPUTER Won"
    else:
        res="Tie"
    return res,user_scores,computer_scores

def main():
    y=True
    user_score=0
    computer_score=0
    print("RULES OF THE GAME:")
    print("->Rock beats Scissors")
    print("->Scissors beat Paper")
    print("->Paper beats Rock")
    while y:
        result,use,compu=game()
        print(result)
        user_score=user_score+use
        computer_score=computer_score+compu
        print("User Score: "+str(user_score))
        print("Computer score: "+str(computer_score))
        print("If you want to continue the game(y or n): ")
        cho=input()
        if cho.lower()=='y':
            y=True
        else:
            if user_score>computer_score:
                print("Comparing all the Matches played so far USER won the game with "+str(user_score-computer_score)+" point(s)")
            elif user_score<computer_score:
                print("Comparing all the Matches played so far COMPUTER won the game with "+str(computer_score-user_score)+" point(s)")
            else:
                print("Comparing all the Matches played so far User and computer score equal points.so, the game is TIE.")
            y=False

main()




