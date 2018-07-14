def is_valid(code):

    s2 = []
    for i in code:
        # print(i)

        if i == "(" or i == "[" or i == "{":
            # s1.put(i)
            s2.append(i)
        else:
            # print("s1",s1.get())
            if (len(s2) == 0 and i != ''):
                return False
            if (s2[-1] == '{' and i == '}') or (s2[-1] == '[' and i == ']') or (s2[-1] == '(' and i == ')'):
                # print("hello")
                s2.pop();

            else:
                return False

    return True
c=0
li=[  '((()))',  '(()())',  '(())()',  '()(())',  '()()()' ]
li=[ "(())",   "()()" ]

for i in li:
    print(i)
    if is_valid(i):
        c+=1
    else:
        continue
print(c)
