#Malik Usman Ahmad PIAIC98144
#Scenario based Assignmen
username=input('Enter your name: ')
fnlist=[] #list for favrioute number store
edlist=[] #list for even odd tuples store.
#appending list and checking even odd
for a in range(1,4):
    num=int(input(f'Enter your {a} favorite number: '))
    fnlist.append(num)
    if num%2==0:
        edlist.append((num,'even'))
    else:
        edlist.append((num,'odd'))

print(f"Hello {username} Let's Explore your favrioute numbers")
#printing even odd
for x,y in edlist:
    print(f'The Number {x} is {y}')
#printing number and it's square
for g in fnlist:
    print(f"The number {g} and its square: ({g},{g**2})")

#printing sum of numbers
tsum=sum(fnlist)
print('The sum of your favrioute number is: ',tsum)

#checking prime
if tsum>1:
    for i in range(2,tsum):
        if(tsum%i==0):
            print(f"{tsum} is not prime number")
            break

        else:
            print(f"Wow!{tsum} is prime number ")
            break
else:
    print(f'{1} is not considered as prime')


print("End of assignment, Output screenshot in comment section of google classroom where we submit Assignment")




