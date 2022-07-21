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
    if my_count == 1:
        print(word_count + " (" + str(my_count) + ")" + ' tree numbered ' + my_string + ' has a ' + '\033[1m' + risk_level[risk] + '\033[0m' + ' risk rating (' + risk + ') as it is ' + '\033[1m' + probability[risk[1]] + '\033[0m' + ' to fail in a ' + '\033[1m' + occupation[risk[0]] + '\033[0m' + ' use area.')
    else:
        print(word_count + " (" + str(my_count) + ")" + ' trees numbered ' + my_string + ' have a ' + '\033[1m' + risk_level[risk] + '\033[0m' + ' risk rating (' + risk + ') as they are ' + '\033[1m' + probability[risk[1]] + '\033[0m' + ' to fail in a ' + '\033[1m' + occupation[risk[0]] + '\033[0m' + ' use area.')

# four_D = []

tree_name_list = []
tree_risk_list = []

for i in range(num_rows):
    tree_name = data_dict['Tree'][i]
    tree_risk = data_dict['Tree Risk Rating'][i]
    if is_tree(tree_name):
        if is_tree(tree_risk):
            tree_name_list.append(tree_name)
            tree_risk_list.append(tree_risk)

            # if '4d' in tree_risk:
            #     four_D.append(tree_name)

df_dict = {'number':tree_name_list, 'risk_rating':tree_risk_list}
df = pd.DataFrame(df_dict)
df_groupby = df.groupby('risk_rating')['number'].apply(list)


for i in range(df_groupby.index.size):
    sentence_maker(df_groupby.iloc[i], df_groupby.index[i][0:2])