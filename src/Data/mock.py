#todo
#1,more realistic

###config

#人，地点，时间，(电话，公司，等等)
nodesConfig = {'people':50,'location':10,'time':5,'other':40}
linkRatio = 2

###init
import json
import random
from faker import Faker

fake = Faker(locale='zh_CN')

nodes = []
edges = []
id = 0


###generate node 
for key,num in  nodesConfig.items():
    for i in range(0,num):
        if key == "people":
            nodes.append({'id': str(id), \
                'label': fake.name(),\
                'description': fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),\
                "class":key})
        elif key == "location" :
            nodes.append({'id': str(id), \
                    'label': fake.building_number(),\
                    'description': fake.address(),\
                    "class":key})
        elif key == "time" :
            nodes.append({'id': str(id), \
                    'label': fake.date(pattern="%Y-%m-%d", end_datetime=None),\
                    'description':  fake.date(pattern="%Y-%m-%d", end_datetime=None),\
                    "class":key})
        else :
            nodes.append({'id': str(id), \
                    'label': fake.word(ext_word_list=None),\
                    'description': fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),\
                    "class":key})
        
        id = id + 1

###generate link
for i, value in enumerate(nodes,1):
    source = random.randint(0,i-1)    
    edges.append({'source':str(source),'target':str(i),'label':fake.word(ext_word_list=None),'class':"dddd"})

linkRatio = linkRatio - 1
if linkRatio > 0 :
    num = int(len(nodes) * linkRatio)
    for i in range(0,num):
        source = random.randint(0,len(nodes))    
        target = random.randint(0,len(nodes))    
        edges.append({'source':str(source),'target':str(i),'label':fake.word(ext_word_list=None),'class':"dddd"})

#serialization
data = json.dumps({'edges': edges, 'nodes': nodes}, indent=4, ensure_ascii=False)

with open('./data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
    print("write json file success!")