my_list = [['Esi', 'Ezekiel', 'Other'], ['Esi', 'Ezekiel', 'Other'], ['Esi', 'Ezekiel', 'Other']]

for i in my_list:
    for j in i:
        print(j)


for i in range (len(my_list)):
    for j in range (len(my_list[i])):
        print(my_list[i][j])


