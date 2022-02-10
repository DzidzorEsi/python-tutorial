
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
#*Set a restriction for input that is not a list and return#*Set a rstriction for the number 0 in the list
#*create a variable, called count and assign to 0
#*write a loop for the list
#*run each iteration through the is_armstrong_number function
#*write if condition to add count 1 for when armstrong function returns True
#write else condition for nothing to be done when function returns false
#*return value of count variable
#*print statement showing the total number of armstrong numbers


def is_armstrong_number(num):
    if type(num) != int:
        return False
    
    if num == 0 or num == 1:
        return False
    
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
    if type(_list) == int:
        return('List expected, but found integer')
    elif type(_list) == str:
        return('List expected, but found string')
        
    count = 0
    for i in (_list):
        ans = is_armstrong_number(i)
        if ans == True:
            count = count + 1

    return count

my_list = [123, 1153, 153, 'top']    
number_count = count_armstrong_numbers(my_list)
print(number_count)


#Steps to count the number of armstrong numbers:
#*define function count_armstrong_numbers(list):
#*create a variable, called count and assign to 0
#*write a loop for the list
#*run each iteration through the is_armstrong_number function
#*write if condition to add count 1 for when armstrong function returns True
#write else condition for nothing to be done when function returns false
#*return value of count variable
#*print statement showing the total number of armstrong numbers                
                
    






        
        
