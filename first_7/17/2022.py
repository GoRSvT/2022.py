print("wassup, are you ready to see if you are worthy?:)")

ready = input("Say \"yes\" if you are and \"no\" if you are a pussy \n :")

if ready == "yes":
   print("Okay, let's play")
   score = 0
if ready == "no":
    print("ok, go ahead coward, eat ass like you always do")
    quit()
answer = input("What is your secret kink? \n :")
if answer == "feet":
    print("Congrats, you are worthy!")
    score += 1
else:
    print("You really think " + answer + " is cool enough? Ugh, incorrect")

answer = input("What has to be present before you are allowed to do anything to another person? \n :")
if answer == "consent":
    print("Congrats, you are worthy!")
    score += 1
else:
    print("You really think " + str(answer) + " will grant you unlimited access to another person? Ugh, incorrect")

answer = int(input("What is the proper age to go wild? \n :"))
if answer >= 18:
    print("Congrats, you are worthy and probably boring!")
    score += 1
elif answer < 18:
    print(" Legally, when you are " + str(answer) + " ,you can't do anything. Ugh, incorrect. ")
answer = int(input("Ok, how about the age you should start a chicken farm? \n :"))
if answer >= 0:
    print("Congrats, you are worthy and cool! Age should not restrict you from starting a chicken farm! ")
    score += 1
elif answer < 0:
    print(" You stupid bean, the age you entered does not exist.")
print("You got " + str(score) + " questions correct, go suck on a peach, you little sexy bastard")