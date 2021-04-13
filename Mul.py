#one ones are one
#one twos are two
import pyttsx3
n = input("Enter a number")
dic = {

    "1" : "ones",
    "2" : "twos",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "sixs",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10" : "tens"

}

txt = "" #Variablefor final text
for i in range(1,11):
    mul = i*int(n)
    txt+= str(i) + " " + dic[n] + " " + "are" + " " + str(mul) + "\n"

engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()