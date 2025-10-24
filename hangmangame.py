import random
characters="abcde"
c=random.choice(characters)
print("Guess character from among (a,b,c,d,e,f) in 6 attempts:")
count=0
while(count < 6):
    count+=1
    guess=input("Enter your guess:")
    if guess == c:
        print("Guessed correct character in ",count,"attempts!")
        break
    elif guess !=c and count==6:
        print("Better luck next time")
    else:
        print(6-count," Attempts left")
print("Thanks for playing !")
