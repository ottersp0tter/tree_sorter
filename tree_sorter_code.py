from pprint import pprint
import pandas as pd
from collections import namedtuple
 
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

#making a word number dictionary, eg 25 is Twenty-five
number_words_dict = {}
with open("numbers.csv", "r") as f:
    lines = f.readlines()


for line in lines:
    split_line = line.split(",")
    number = int(split_line[0])
    word = split_line[1]
    if  "\n" in word:
        size = len(word)
        word = word[:size - 1]
    number_words_dict[number] = word

#_________________________________________________________#



# sentence making function
probability = {'a':'very likely', 'b':'likely', 'c':'somewhat likely', 'd':'unlikely','e':'highly unlikely'}

occupation = {'1':'occasional', '2':'intermittent', '3':'frequent', '4':'constant','5':'continuous'}

risk_level = {
    '5a':'extreme',
    '5b':'extreme', 
    '5c':'very high',
    '5d':'medium',
    '5e':'ALARP',
    '4a':'very high',
    '4b':'very high',
    '4c':'high',
    '4d':'medium',
    '4e':'ALARP',
    '3a':'high',
    '3b':'high',
    '3c':'high',
    '3d':'medium',
    '2a':'high',
    '2b':'medium',
    '2c':'medium',
    '2d':'ALARP',
    '2e':'ALARP',
    '1a':'medium',
    '1b':'medium',
    '1c':'ALARP',
    '1d':'ALARP',
    '1e':'ALARP'
    }

def sentence_maker(my_list, risk):
    my_string = ', '.join(str(x) for x in my_list)
    my_count = len(my_list)
    word_count = number_words_dict[my_count]
    print(word_count + " (" + str(my_count) + ")" + ' trees numbered ' + my_string + ' have a ' + risk_level[risk] + ' risk rating (' + risk + ') as they are ' + probability[risk[1]] + ' to fail in a ' + occupation[risk[0]] + ' use area.')


tree_data = 
for i in range(num_rows):
    tree_name = data_dict['Tree'][i]
    tree_risk = data_dict['Tree Risk Rating'][i]

    # if is_tree(tree_name):
    #     if is_tree(tree_risk):

            # if '4d' in tree_risk:
            #     four_D.append(tree_name)
