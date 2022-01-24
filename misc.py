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

    
#Converting from degrees Fahrenheit to degrees Kelvin
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


#print ('100 degrees Fahrenheit is ' + str(converted) + ' in degrees Kelvin')

#Checking for a prime number
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

#Using (number)**0.5
def is_perfect_square(number):
    sqr_rt = (number)**0.5

    if sqr_rt == type(int):
         return True

    return False

#perfect_square = is_perfect_square(9)   




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
_reversed = reverse_string_return('characters')
print(_reversed)
    
