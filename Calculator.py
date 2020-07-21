#def future():
   # age = int(input(" Enter the year you were born here: "))
    #print('You will turn 100 years in: ', age+100)
    #name = str(input(" Enter full name here: "))
    #print('Full name is: ', name)
#future()



def calculation():
    a = int(input("Enter first number here: "))
    b =int(input("Enter second number here: "))
    c = str(input("Enter an operation(add'+', sub'-', division'/', multiplication'*', raise to power'^'): "))
    add = a+b
    sub = a-b
    division = a/b
    multiplication = a*b
    power = a**b
    if c == 'add':
        print('The sum of a and b =:',add)
    elif c == 'sub':
        print('The subtraction of a and b =:',sub)
    elif c == 'division':
        print('The division of a and b =:',division)
    elif c == 'multiplication':
        print('The multiplication of a and b =:',multiplication)
    elif c == 'power':
        print('The power of a and b =:',power)
    else:
        print("Wrong input!!!Please check from the selection example 'sub'")
    while True:
        str(input('Enter y to continue or n to end (n/y): ' ))
        if input == 'y':
            calculation()
        elif input == 'n':
            print("Goodbye!!!")
        else:
            print('Wrong input')
            break
            
calculation()
