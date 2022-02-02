import os

# print(os.path.realpath(__file__))
print(os.getcwd())  # 현재 경로(현재 폴더 위치) 확인
os.chdir("C:\\Users\\박예은\\AppData\\Local\\Programs\\Python\\Python37\\One_Big_Archive\\images")    # 경로 변경
print(os.getcwd())
