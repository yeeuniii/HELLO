# 빈 리스트 생성
friends = []

my_list = [5, 10, 23.76, "Hello", friends]
letters = ["a", "b", "c", "d", "e"]
print(letters[0])
print(letters[3])
print(letters[:])   # 리스트 복사본 생성

# 항목 추가
letters.append("g")
print(letters)
letters.extend(["h", "i", "j"])
# letters.append(["h", "i", "j"]) ; 둘은 명백히 다른 것.
print(letters)
letters.insert(5, "f")
print(letters)

# 항목 삭제
letters = ["a", "b", "c", "d", "e"]
letters.remove("c")
print(letters)
del letters[3]
print(letters)
letters = ["a", "b", "c", "d", "e"]
last = letters.pop()
print(letters)
print(last)
second = letters.pop(1)
print(letters)
print(second)

# 항목 찾기
if "a" in letters:
    print("found 'a' in letters")
else:
    print("did`nt find 'a' in letters")
print("a" in letters)
print("i" in letters)
var = "a"
if var in letters:
    letters.remove(var)
print(letters)

print(letters.index("a"))
if var in letters:
    print(letters.index(var))

###
letters = ["a", "b", "c", "d", "e"]
for letter in letters:
    print(letter)

# 리스트 정렬
letters = ["d", "a", "e", "b", "c"]
letters.sort()
print(letters)
# print(letters.sort())
letters.reverse()
print(letters)
letters.sort(reverse=True)
print(letters)

friends.extend(["Tom", "James", "Sarah", "Fred"])
list1 = friends
list2 = friends[:]
print(list1, list2)
friends.sort()
print(friends, list1, list2)

letters = ["d", "a", "e", "b", "c"]
new_letter = sorted(letters)
print(new_letter, letters)

# 데이터 테이블 ; 리스트의 리스트
joeMarks = [55, 63, 77, 81]
tomMarks = [65, 61, 67, 72]
bethMarks = [97, 95, 92, 88]
classMarks = [joeMarks, tomMarks, bethMarks]
print(classMarks)
classMarks = [[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]
print(classMarks)
for i in classMarks:
    print(i)

# 도전하기
# 1
print("Enter 5 names:")
names = []
for i in range(5):
    name = input("")
    names.append(name)
# print(names)
print("The names are ", end="")
for i in names:
    print(i, end=" ")
print()
# 2
# (1)
new = names[:]
new.sort()
print("Original", names, "\nSorted", new)
# (2)
print("Original", names, "\nSorted", sorted(names))

# 3
print("The third name you entered is:", names[2])

# 4
num = int(input("Replace one name. Which one? (1-5): "))
new_name = input("New name: ")
# names.pop(num-1)
# names.insert(num-1, new_name)
names[num-1] = new_name
print("The names are ", end="")
for i in names:
    print(i, end=" ")
