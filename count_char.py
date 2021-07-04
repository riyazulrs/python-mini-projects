import operator
strg=input('enter the string')


dic={}

for i in strg:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1

sorted_d = dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
for i in sorted_d:
    print(f"the letter {i} occurs for {dic[i]} times")


