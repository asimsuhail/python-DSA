# is string balanced () {} []


str = "(){}[()](){{()}}"
str = list(str)
li = []

for i in str:
    if i in [ '(', '{', '[' ]:
        li.append(i)
        print(li)
    if (i == ')' and li[len(li) - 1] == '(' ) or (i == '}' and li[len(li) - 1] == '{' ) or (i == ']' and li[len(li) - 1] == '[' ):
        li.pop()
        print(li)
if len(li) == 0:
    print("balanced")
else:
    print("not balanced")
