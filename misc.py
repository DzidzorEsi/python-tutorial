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
print ('Converting from degrees Fahrenheit to degrees Kelvin...')
'''
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

def is_number_prime(number):
    for i in range(2, number):
        remainder = number%i

        if remainder == 0:
            return False

    return True
'''           
prime_number = is_number_prime(11)
print(prime_number)'''




    
    
