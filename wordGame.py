'''This is my word game as our team's "code together" GE103 project. The official members are Praneeth, Revanth, JayaPrakash and Krishna'''
#this is inbuilt library for GUI programming in Python
from tkinter import *
#this dictionary is used to take meaning of a word and display it as a hint
from PyDictionary import PyDictionary
#this is inbuitl library for making something random in programming in Python
import random
#word list is user define library
import word_list

#we make a list of 3000 word from user define library
word_list=word_list.word_list

root=Tk()

root.title('''Word Game By Team "Code Together"''')

#we will use  different type of function for our project as given below

#these are some global variables
w=""
score=0
chance=3
option_e=0

#functions which are used
def selecting_a_word(word_list,i):
    '''This function select a word from a word list of 3000 word in random manner but with specific world length and return it'''
    flag=0
    #lets iterate into word_list using while loop
    while(flag!=1):
        #select a random word
        y=random.randint(1,len(word_list))
        #if word length equal to i then found a required word length
        if(len(word_list[y])==i):
            #to stop while loop
            flag=1
    return word_list[y]

def to_show_player(w):
    '''This functon hide given word and show to player'''
    #let itrate in word using for loop
    for i in range(len(w)-2):
        #make it as new word but with '_' to hide that letter from word
        new_w=''
        #select a ramdon letter from given word
        x=random.randint(0,len(w)-1)
        #now add '_' with some of letter from word
        for j in range(len(w)):
            #if random selected letter found then replace it with '_'
            if(j==x):
                new_w=new_w+'-'
            #otherwise leave it as it is
            else:
                new_w=new_w+w[j]
        w=new_w
    return w



def next_button_c():
    '''This function add command in 'next word' button and command to replace word/entry from entry word_to_player'''
    global w
    global word_list
    global chance
    global option_e
    if(option_e==1 or option_e==2):
        #as we press next word then it delete previous data and react according to word length
        word_to_player.delete(0, END)
        #If word length is more than 13 then there is no word in word list of length so simple send message to player that you exceed word length
        if(int(word_len.get())>14):
            result_screen.delete(0, END)
            result_screen.insert(0, "Exceed word length")
        #otherwise, word length in required range then give word to player
        elif(chance>0):
            #to select a word of required length from word list
            w=selecting_a_word(word_list,int(word_len.get()))
            #give output to player
            word_to_player.insert(0, to_show_player(w))
            #also provide hint to player in hint region
            result_screen.delete(0, END)
            #taking the module PyDictionary and storing as library
            library=PyDictionary()
            #displaying the meaning of the given word from PyDictionary on result screen
            result_screen.insert(0,library.meaning(w))
            #making the user input blank after he asked to go to next word
            player_response.delete(0,END)
        else:
            word_to_player.insert(0, "You have no more chance,press RESTART!")

        #to chnage length of word automaticaly if player choose type_2 then
        if(option_e==2):
            word_len.delete(0,END)
            word_len.insert(0,3+int(int(score_e.get())//5))
    else:
        word_to_player.delete(0, END)
        word_to_player.insert(0, 'Select a Type')



def result_button_c():
    '''This function add commant to 'result_button' and show result'''
    global w
    global score
    global chance
    global option_e
    if(option_e==1 or option_e==2):
        #collect respone from player as a string k
        k=str(player_response.get())
        #if k and w are equal then updae score and output_2 entry
        if(w==k):
            #to update score variable
            score=int(score_e.get())+1
            score_e.delete(0, END)
            #to update score_e entry
            score_e.insert(0, score)
            result_screen.delete(0, END)
            #to update result_screen entry
            result_screen.insert(0,"You are Correct. The word is: "+w)
        #if k and w are not equal then updae chance and output_2 entry
        else:
            #to update chance variable
            chance=int(chance_e.get())-1
            chance_e.delete(0, END)
            #to update chance_e entry
            chance_e.insert(0, chance)
            result_screen.delete(0, END)
            #to update result_screen entry
            result_screen.insert(0,"You are incorrect. The word is: "+w)
    else:
        result_screen.delete(0, END)
        #to update result_screen entry
        result_screen.insert(0,"You have not choosen any type...")

def option_e1():
    '''This function allow us to choose game type1'''
    global option_e
    option_e=1

def option_e2():
    '''This function allow us to choose game type2'''
    global option_e
    option_e=2

def restart_game():
    '''This function provide initial state of game'''
    global chance
    global score
    #first assign initial value of variable
    chance=3
    score=0
    #now it time to assign initial value to entries
    #first clean old value in entry
    result_screen.delete(0,END)
    chance_e.delete(0, END)
    score_e.delete(0, END)
    word_to_player.delete(0, END)
    word_len.delete(0, END)
    player_response.delete(0, END)
    #now start filling intial value in entry
    chance_e.insert(0, 3)
    result_screen.insert(0, "Hint will shown here.")
    score_e.insert(0, 0)
    word_to_player.insert(0, "New word will appear here")
    word_len.insert(0, 3)




#Row=1
#Label function in root is to show a static output
#this is heading label to provide some initial information
label4=Label(root, text='''       Welcome! To Word Game.
        We have two flavors of game:
        1.In this flavor, you can choose length of word everytime.
        2.In this flavor, you get lengthier/tougher words level by level.
        So, please choose a flavor or you can exit the game.''')
#grid function is to set position of Label in GUI
label4.grid(row=0, column=0, columnspan=5)



#Row=2
#Button function are use to give some command by user
#here, we start putting some button in GUI
option_3=Button(root, text="Type 1", command=option_e1)
option_4=Button(root, text="Type 2", command=option_e2)
#we have to specify grid position of Button also
option_3.grid(row=1, column=0)
option_4.grid(row=1, column=1)

score_l=Label(root, text="Score & Chance left:")
score_l.grid(row=1,column=2)

score_e=Entry(root, text=0, width=5)
score_e.grid(row=1,column=3)
score_e.insert(0,0)

chance_e=Entry(root, text=3, width=5)
chance_e.grid(row=1,column=4)
chance_e.insert(0,3)



#Row=3
label3=Label(root, text='''Word to guess:''')
label3.grid(row=2, column=0)
#word that will user see which will incomplete
word_to_player= Entry(root, fg="red", width=35)
#output
word_to_player.grid(row=2, column=2)



#Row=4
#this label to show player
label1=Label(root, text="Word:")
label2=Label(root, text="  Length of Word:")

label1.grid(row=3,column=0)
label2.grid(row=3,column=3)

player_response= Entry(root, width=30, bg="white", fg="black", borderwidth=5)
word_len= Entry(root, width=10, bg="white", fg="black", borderwidth=5)
word_len.grid(row=3, column=4)
word_len.insert(0,3)
player_response.grid(row=3, column=1, columnspan=2)



#Row=5
#this button provide command to player to cahnge new word and to show result
option_1= Button(root, text="Result", command=result_button_c)
option_2= Button(root, text="Next Word", command=next_button_c)
submit_button= Button(root, text="Restart The Game",command=restart_game)
#to make output of buttons
option_1.grid(row=4, column=0)
submit_button.grid(row=4, column=2)
option_2.grid(row=4, column=4)



#Row=6
output_1=Label(root, text="Correct Word & Hint:")
output_1.grid(row=5, column=0)

result_screen=Entry(root, width=50)
result_screen.grid(row=5, column=1, columnspan=4)
result_screen.insert(0, "Hint and result will shown here")






#just to create extra gap and make gui screen big and name of those who support the project
word_u0= Label(root, text="", fg="blue")
word_u1= Label(root, text="Credit for this goes to Sudarshan Sir.", fg="red")
word_u2= Label(root, text="And their studends:", fg="blue")
word_u3= Label(root, text="Mr Revanth", fg="blue")
word_u4= Label(root, text="Mr JP", fg="blue")
word_u5= Label(root, text="Mr Praneeth", fg="blue")
word_u6= Label(root, text="Mr Krishna", fg="blue")

word_u0.grid(row=8,column=0, columnspan=5)
word_u1.grid(row=9,column=0, columnspan=5)
word_u2.grid(row=10,column=0, columnspan=5)
word_u3.grid(row=11,column=0, columnspan=5)
word_u4.grid(row=12,column=0, columnspan=5)
word_u5.grid(row=13,column=0, columnspan=5)
word_u6.grid(row=14,column=0, columnspan=5)



#to show exit button and exit from game
exit_the_game= Button(root, text="Exit Game", command=root.quit)
exit_the_game.grid(row=15, column=0, columnspan=5)


root.mainloop()
