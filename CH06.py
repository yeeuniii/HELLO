import easygui
'''
user_response = easygui.msgbox("Hello")
print(user_response)

# 예제 6.1
flavor = easygui.buttonbox("What`s your favorite ice cream flavor?",
                           choices=["vanilla", "chocolate", "strawberry"])
print("I like", flavor)
easygui.msgbox("You like "+flavor)

# 예제 6.2
flavor = easygui.choicebox("Choice your favorite ice cream flavor",
                           choices=["vanilla", "chocolate", "strawberry"])
easygui.msgbox("You choice "+flavor)

# 예제 6.3
flavor = easygui.enterbox("What`s your favorite ice cream flavor?")
easygui.msgbox("You choice "+flavor)

# 예제 6.4
flavor = easygui.enterbox("What`s your favorite ice cream flavor?", default="vanilla")
easygui.msgbox("You choice "+flavor)

##
num = easygui.integerbox("Select integer number among 1~10", lowerbound=1, upperbound=10)
print(num+3)
'''

## 도전하기
# 1
f = float(easygui.enterbox("화씨 온도를 입력하시오."))
c = (f-32)*5/9
easygui.msgbox("현재 섭씨 온도는 "+str(c)+"도 입니다.")

# 2
name = easygui.enterbox("이름을 입력하시오.")
apt = easygui.enterbox("아파트 주소를 입력하시오.")
city = easygui.enterbox("거주시를 입력하시오.")
status = easygui.enterbox("거주구를 입력하시오.")
num = easygui.enterbox("우편번호를 입력하시오.")
whole = name+"\n"+apt+"\n"+status+", "+ city+"\n"+num
easygui.msgbox(whole)
