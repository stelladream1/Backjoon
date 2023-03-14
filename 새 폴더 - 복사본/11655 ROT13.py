import sys
cap = ['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P',
       'Q','R','S','T','U','V','W','X','Y','Z'] * 2
array = list(map(str,input()))
temp = []
for i in array:
    for j in i:
        if j.isalpha():
            if j.isupper():
                result = cap[cap.index(j) + 13]
                temp.append(result[0])
            else:
                j = j.upper()
                result = cap[cap.index(j) + 13].lower()
                temp.append(result[0])
        else:
            temp.append(j)

for i in temp:
    print(i, end="")
