a = int(input('Enter a number : '))
mylist = [a]
n = 0
for i in range(a*3):
    n += 1
    if a == 1:
        break

    if a % 2 != 0:
        a = ((a *3) +1)
        mylist.append(int(a))

    if a % 2 == 0:
        a = (a / 2)
        mylist.append(int(a))

print('number of loop = ',n)
print(mylist)