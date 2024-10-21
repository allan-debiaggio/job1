L=[8,24,27,48,2,16,9,7,84,91]
value = 0

for i in range(0,10) :
    if L[i] % 2 == 0 :
        value += L[i]

print(L)
print("The sum of even numbers in this list is : ", value)