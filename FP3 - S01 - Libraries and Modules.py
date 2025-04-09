#--------------
#FP3-S01-Libraries and Modules
#Hailey-lynn Aldred
#07 April 2025
#Main Code File
#--------------
from modules import mymusic #importing my .py file mymusic from the folder modules
from modules import usermusic #importing my .py file usermusic from the folder modules
import time #importing one of pythons built in modules

#----Functions----#
def intro():
    print("Music: Noun")
    print("""Vocal or instrumental sounds (or both) combined to produce
beauty of form, harmony, and the expression of emotion.""") #triple quotes for multiple lines of code in one string
    time.sleep(2) #opens the .py module time and calls the function sleep. waits two seconds

def music_me():
    print(mymusic.my_favs) #takes the variable from the module and prints it
    time.sleep(1) #waits one second
    mymusic.my_choice() #calls the function from the module
    print("I have a tattoo for the song", mymusic.tattoo + '.') #prints a string along with another variable from the same module
    time.sleep(2)
    print("Music impacts people in many ways, more than we can imagine.")
    time.sleep(2)

def music_user():
    usermusic.top_songs() #calls function from another module and runs it
    time.sleep(2)
    ghost_ehe = usermusic.top_artist('Ghost') #attaches the returned value from the function that's called from the module
    print(ghost_ehe) #prints the returned value
    
def main(): #just my main code as a function
    intro()
    music_me()
    music_user()
    
#----Main Code----#
main() #calls my main code
