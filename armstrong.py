
#Steps to find armstrong number
#*.define the function: is_armstrong_number(num)
#*.convert num to string & store in variable called num_str
#*.get length of num_str & store in variable called exponent
#*create variable called _sum and assign it to 0
#*.write for loop for range in of (0, exponent)
#*get the i-th digit of num_str
#*convert i-th digit to int
#*get the product of the i-th digit and **exponent and store in variable product
#*add product to variable _sum
#*.write if condition to compare the value of _sum to num
#*.if sum == num, return True
#*.if sum!= num, return False

#Steps to count the number of armstrong numbers:
#*define function count_armstrong_numbers(list):
#*create a variable, called count and assign to 0
#*write a loop for the list
#*run each iteration through the is_armstrong_number function
#*write if condition to add count 1 for when armstrong function returns True
#write else condition for nothing to be done when function returns false
#*return value of count variable
#*print statement showing the total number of armstrong numbers


def is_armstrong_number(num):
    num_str = str(num)
    exponent = len(num_str)
    _sum = (0)

    for i in range (exponent):
        digit = int(num_str[i])
        product = digit **exponent
        _sum += product

    if _sum == num:
        return True
    else:
        return False
    
    
def count_armstrong_numbers(_list):
    count = (0)
    for i in (_list):
        is_armstrong_number(i)

    if is_armstrong_number(i) == True:
        count += 1
    else:
        pass

    return count

my_list = ([153, 834, 1634, 92331, 111, 0])
number_count = count_armstrong_numbers(my_list)
print(number_count)

                
                
    






        
        
