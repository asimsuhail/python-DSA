# is string balanced () {} []



str = list(input("enter string"))
li = []

for i in str:
    li.append(i)
    print(li)
    if (i == ')' and li[len(li) - 2] == '(' ) or (i == '}' and li[len(li) - 2] == '{' ) or (i == ']' and li[len(li) - 2] == '[' ):
        li.pop()
        li.pop()
        print(li)
if len(li) == 0:
    print("balanced")
else:
    print("not balanced")
