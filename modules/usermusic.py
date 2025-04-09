#--------------
#FP3-S01-Libraries and Modules
#Hailey-lynn Aldred
#07 April 2025
#Modules --> User Music!
#--------------
import time #calls py module

list_five = {} #an empty dictionary for passing information into

def top_songs():
    song_count = 0 #sets the count to 0 so that the program knows when the user has listed five songs
    print("What are your top 5 songs?")
    while song_count < 5: #while the user can still add more songs
        key = input("What is the name of the song? > ")
        value = input("Who is this song by? > ")
        song_count = song_count + 1 #adds one to the count so that when it hits five the loop stops
        #print(song_count)
        list_five[key] = value #puts the key:value into the dictionary
    print("You said that")
    for (key, value) in list_five.items(): #for every key and its corresponding value, list the key and value
        print(key, "by", value) #lists out the key and its corresponding value in the dictionary
        time.sleep(1)
    print("are your top 5 songs! That is a very solid list of music.")
    
def top_artist(x): #new function with a return value and passable argument
    print("My top artist is", x + '.') #takes the argument and ties a period to it
    my_artist = x.lower() #takes the argument and makes it lowercase (still displays uppercase) and attaches the lowercase version to a variable
    musician = input("Who is your top artist? > ").lower() #makes the user input lowercase as well for comparison
    if musician == my_artist: #if the user input is the same as the argument i passed
        return "Oh! We have the same top artist! Awesome!" #return this string
    else: #if its anything else
        return "Cool, I'll have to give them a listen!" #return this string instead
    