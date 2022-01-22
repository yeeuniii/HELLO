# Chap6
import random
import easygui

num = random.randint(1,100)
trial = 0

while trial < 6 :
    choice = easygui.integerbox("Guess number among 1~100", lowerbound=1, upperbound=100)
    if choice < num :
        easygui.msgbox("Too small! Try again.")
    elif choice > num :
        easygui.msgbox("Too large! Try again.")
    else :
        easygui.msgbox("CORRECT!!")
        break
    trial = trial+1

if trial > 5 :
    easygui.msgbox("You`re fail. The number is "+str(num))

