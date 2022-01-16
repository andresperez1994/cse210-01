#Tic-tac-toe game
#cse210-01 
#Author: Andres Perez 


def main():
     
    a_1=1
    b_1=2
    c_1=3

    a_2=4
    b_2=5
    c_2=6

    a_3=7
    b_3=8
    c_3=9

    numbers_choosen=[]
    entrance=0
    entrance2=0

    win_game=0
    end_game=0
    input1=0
    input2=10    
    
    while win_game!=1 or end_game!=1: 
        print_chart(a_1,a_2,a_3,b_1,b_2,b_3,c_1,c_2,c_3)
        input1=int(input("x's turn to choose a square (1-9): ")) 
        repeat_input(input1, numbers_choosen)
        
        numbers_choosen.append(input1)     
        sum_total=sum(numbers_choosen) 
        
        if input1==1:
            a_1="x"
        elif input1==2:
            b_1="x"
        elif input1==3:
            c_1="x"
        elif input1==4:
            a_2="x"
        elif input1==5:
            b_2="x"
        elif input1==6:
            c_2="x"
        elif input1==7:
            a_3="x"
        elif input1==8:
            b_3="x"
        elif input1==9:
            c_3="x"   

        if a_1==b_1==c_1 or a_2==b_2==c_2 or a_3==b_3==c_3 or a_1==a_2==a_3 or b_1==b_2==b_3 or c_1==c_2==c_3 or a_1==b_2==c_3 or a_3==b_2==c_1:
            win_game=1
            winner=1
        
        print_chart(a_1,a_2,a_3,b_1,b_2,b_3,c_1,c_2,c_3)   
        if win_game==1: 
            break 
        if sum_total==45:
            end_game=1
            winner=3
            break    
        
        input2=int(input("O's turn to choose a square (1-9): "))
        repeat_input(input2, numbers_choosen)
        
        numbers_choosen.append(input2)     
        sum_total=sum(numbers_choosen)
        
        if input2==1:
            a_1="o"
        elif input2==2:
            b_1="o"
        elif input2==3:
            c_1="o"
        elif input2==4:
            a_2="o"
        elif input2==5:
            b_2="o"
        elif input2==6:
            c_2="o"
        elif input2==7:
            a_3="o"
        elif input2==8:
            b_3="o"
        elif input2==9:
            c_3="o"

        if a_1==b_1==c_1 or a_2==b_2==c_2 or a_3==b_3==c_3 or  a_1==a_2==a_3 or b_1==b_2==b_3 or c_1==c_2==c_3 or a_1==b_2==c_3 or a_3==b_2==c_1:
            win_game=1
            winner=2 
        
        print_chart(a_1,a_2,a_3,b_1,b_2,b_3,c_1,c_2,c_3)
        
        if win_game==1: 
            break  
    
        if  sum_total==45: 
            end_game=1
            winner=3
            break
    if winner==1: 
        print("x's wins the game")
    elif winner==2: 
        print("o's wins the game")
    else:
        print("No one wins the game, try to play again")
    print()
    print("Thank you for play this game!")    
           
                
        

def repeat_input(input1, numbers_choosen):
    while input1 in numbers_choosen:
        print("This number was already chose")   
        print("Choose another number")
        input1=int(input("x's turn to choose a square (1-9): ")) 

        
def print_chart(a_1,a_2,a_3,b_1,b_2,b_3,c_1, c_2,c_3):
    print()
    print(f"{a_1}|{b_1}|{c_1}")
    print("-+-+-")
    print(f"{a_2}|{b_2}|{c_2}")
    print("-+-+-")
    print(f"{a_3}|{b_3}|{c_3}")
    print() 

    

main()