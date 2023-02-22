# write your code here
import random

print('Enter the number of friends joining (including you):')
people_number = int(input())

if people_number <= 0:
    print('')
    print('No one is joining for the party')
else:
    names = {}
    namelist = []
    print('')
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(people_number):
        name = input()
        names[name] = 0
        namelist.append(name)
    print('Enter the total bill value:')
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'No':
        print('')
        print('No one is going to be lucky')
        for key,value in names.items():
            names[key] = round((bill/(people_number)),2)
        print('')
        print(names)
    else:
        luckyname = random.choice(namelist)
        print(f'{luckyname} is the lucky one!')
        for key,value in names.items():
            names[key] = round((bill/(people_number-1)),2)
        names[luckyname] = 0
        print('')
        print(names)