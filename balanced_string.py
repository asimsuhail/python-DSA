# is string balanced () {} []


str = "(){}[()](){{()}}"
str = list(str)
li = []

for i in str:
    if i == '(' or i == '{' or i == '[':
        li.append(i)
        print(li)
    if i == ')' or i == '}' or i == ']':
        if li[len(li) - 1] == i:
            li.pop()
            print(li)
if len(li) == 0:
    print("balanced")
else:
    print("not balanced")
