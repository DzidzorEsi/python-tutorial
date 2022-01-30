def invert_2_variables():
    x = 30
    y = 20
    print ('initial values')
    print ('x = 30')
    print ('y = 20'+'\n')

    z = x
    x = y
    y = z


    print ('final values')
    print ('x = ' +str(x))
    print ('y = ' +str(y))



def invert_3_variables():
    a = 10
    b = 20
    c = 30

    print ('initial values')
    print ('a = ' + str(a))
    print ('b = ' + str(b))
    print ('c = ' + str(c) + '\n')

    d = a
    a = b
    b = c
    c = d

    print ('final values')
    print ('a = ' +str(a))
    print ('b = ' +str(b))
    print ('c = ' +str(c))

'''
print ('Converting from degrees Fahrenheit to degrees Kelvin...')

(32°F − 32) × 5/9 + 273.15 = 273.15K
1.define function (convert_to_degrees_kelvin(temp_in_fahrenheit))
2.solve left side of the equation
3.solve right side of the equation
4._return value
5._print value '''


def convert_to_degree_kelvin(temp_in_fahrenheit):
    degree_diff = temp_in_fahrenheit - 32
    degree_in_kelvin = degree_diff * 5/9 + 273.15

    return degree_in_kelvin



def is_number_prime(number):
    for i in range(2, number):
        remainder = number%i

        if remainder == 0:
            return False

    return True
'''          
prime_number = is_number_prime(11)
print(prime_number)'''

'''
print('Testing 100 for  a perfect square...')

1. Define function with parameter(number):
2. Create a loop with range of values (1,number)
3. variable = divide (number) by i
4. Set "if" condition for variable = i to return True

def is_perfect_square(number):
    for i in range(1,number):
        quotient = number/i

        if quotient == i:
            return True
        
    return False

perfect_square = is_perfect_square(100)
print(perfect_square)
'''

def is_perfect_square(number):
    sqr_rt = (number)**0.5

    if sqr_rt == type(int):
         return True

    return False


def reverse_string(string):
    for i in range(len(string), 0, -1):
        print(string[i-1], end='')
        
    print()

def reverse_string_return(string):
    reversed_string = ''
    for i in range(len(string), 0, -1): 

        reversed_string = reversed_string + string[i-1]

    return reversed_string


#reverse_string('motivation')
#_reversed = reverse_string_return('characters')
#print(_reversed)

'''
1.define the function is_palindrome
2.create variable to store characters from iterations
3.write loop using len of argument as start and -1 as step
4.store iterations in variable
5.return true if palindrome
6.return false in not
7.add condition for accepting only string '''


def is_palindrome(string):
    if type(string)!= str:
        print('Invalid input, try something else')

        return
    string = string.replace(' ','')
    reversed_str = string[::-1]

    if reversed_str == (string):
        return True
    else:
        return False

'''
_reversed = is_palindrome('madam')
print(_reversed)
_reversed = is_palindrome('able was i ere i saw elba')
print(_reversed)
_reversed = is_palindrome('nurses run')
print(_reversed)
_reversed = is_palindrome('was it a cat i saw')
print(_reversed)
_reversed = is_palindrome(1881)
print(_reversed)'''

# Hello world comment


#1.define function: is_armstrong_number(num)
#2.get value of exponent & store in variable = expo
# i. convert num to string & find len(num)
#3.get digit in (num)
# i.find(num)%10 & store in variable = remainder
# ii.subtract remainder from (num) & divide by 10
#4.loop step 3 to get all other digits
#5.get sum of each digit raised to the exponent found in step 2 & assign varaible = _sum
#6.return the variable _sum
#7.write if condition to compare the variable sum to intinial parameter

def is_armstrong_number(num):
    expo = len(str(num))
    _sum = 0 
    
    while(True):
        remainder = num %10
        num = (num - remainder)/10
        _sum += (remainder**expo)
        
        return _sum
    if _sum == 153:
        print ("it is an armstrong number")

    else:
        print ("it is not an armstrong number")

armstrong = is_armstrong_number(153)
print(armstrong)
    
    


