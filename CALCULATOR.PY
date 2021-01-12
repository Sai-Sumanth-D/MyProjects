
# Simple Calculator using Python


def add(x, y):

    return(x+y)


def subtraction(x, y):

    return(x-y)


def multiplication(x, y):

    return(x*y)


def division(x, y):

    return(x/y)


def power(x, y):

    return pow(x ^ y)


print('Select your desired Operation:')
print('1.Add')
print('2.Subtract')
print('3.Multiplication')
print('4.Division')
print('5.Power')

Operation_type = input('Enter your choice of operation 1/2/3/4/5 : ')

value1 = int(input('Enter your first number : '))
value2 = int(input('Enter your second number : '))

if Operation_type == "1":
    print(value1, '+', value2, "=", add(value1+value2))

elif Operation_type == "2":
    print(value1, "-", value2, "=", subtraction(value1-value2))

elif Operation_type == "3":
    print(value1, "*", value2, "=", multiplication(value1*value2))


elif Operation_type == "4":
    print(value1, "/", value2, "=", division(value1 / value2))


elif Operation_type == "5":
    print(value1, "^", value2, "=", pow(value1, value2))


else:
    print('Enter only from the available options from 1-5')
