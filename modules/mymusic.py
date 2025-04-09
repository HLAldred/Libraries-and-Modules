#--------------
#FP3-S01-Libraries and Modules
#Hailey-lynn Aldred
#07 April 2025
#Modules --> Personal Music!
#--------------
import time #calls py module
song_list = {'Future is a Foreign Land':'Ghost', 'Nobody Escapes':'Mother Mother', 'Through the Ghost':'Shinedown', 'Iris':'The Goo Goo Dolls', 'Cabaret':'Penelope Scott'}
#^ a personal list of songs I like
my_favs = "Here are some of my favourite songs." #variable that main program can call

def my_choice():
    for (key, value) in song_list.items(): #for every key and its corresponding value in my dictionary
        print(key, "by", value) #print the key and its value
        time.sleep(1) #wait one second
        
tattoo = "Just Breathe by Pearl Jam" #another variable that the main program can call