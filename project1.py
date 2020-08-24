import pyttsx3
print("Welcome to python World\n");
user1=input("Enter A Number For Your Table")
store={
    "1":"ones",
    "2":"Twos",
    "3":"Threes",
    "4":"Fours",
    "5":"Fives",
    "6":"Sixs",
    "7":"Sevens",
    "8":"Eights",
    "9":"Nines",
    "10":"Tens",
}
text=""
for i in range(1,11):
    mult=i*int(user1)
    text+=str(i)+" "+store[user1]+ " are "+ " "+str(mult)+"\n"
print(text)

engine = pyttsx3.init('dummy')
# engine = pyttsx.init('dummy')
engine.say(text)
engine.runAndWait()
