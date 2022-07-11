from pprint import pprint
import pandas as pd
 
file = "tree_sorter.xlsx"
data = pd.read_excel(file) #reading file
 

data_dict = data.to_dict()
num_rows = len(data_dict['Tree'])

number_strings = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']


def is_tree(x):
    if isinstance(x, int):
        return True
    if isinstance(x, str):
        if x[0] in number_strings:
            return True
    return False



four_D = []
four_C = []
four_B = []
four_A = []

for i in range(num_rows):
    tree_name = data_dict['Tree'][i]
    tree_risk = data_dict['Tree Risk Rating'][i]
    if is_tree(tree_name):
        if is_tree(tree_risk):
            if '4a' in tree_risk:
                four_A.append(tree_name)
            if '4b' in tree_risk:
                four_B.append(tree_name)
            if '4c' in tree_risk:
                four_C.append(tree_name)
            if '4d' in tree_risk:
                four_D.append(tree_name)

#4d
four_D_str = ', '.join(str(x) for x in four_D)
four_D_sentence = str(len(four_D)) + ' trees numbered ' + four_D_str + ' have a medium risk rating (4D) as they are unlikely to fail in a constant use area.'

#4c
four_C_str = ', '.join(str(x) for x in four_C)
four_C_sentence = str(len(four_C)) + ' trees numbered ' + four_C_str + ' have a high risk rating (4C) as they are somewhat likely to fail in a constant use area.'

#4b
four_B_str = ', '.join(str(x) for x in four_B)
four_B_sentence = str(len(four_B)) + ' trees numbered ' + four_B_str + ' have a very high risk rating (4B) as they are likely to fail in a constant use area.'

#4a
four_A_str = ', '.join(str(x) for x in four_A)
four_A_sentence = str(len(four_A)) + ' trees numbered ' + four_A_str + ' have a very high risk rating (4A) as they are highly likely to fail in a constant use area.'

print(four_A_sentence + "\n" + four_B_sentence + "\n" + four_C_sentence + "\n" + four_D_sentence)