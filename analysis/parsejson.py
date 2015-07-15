__author__ = 'charoy'
import json
from pprint import pprint

json_data=open("../taskruns/moretests150715/crowdsourcing4_task_run.json").read()

data = json.loads(json_data)

pprint(data)

f=open("info.csv",'w')
f.write("task_id,info\n")
for d in data:
    print(d['info'])
    f.write(str(d['task_id'])+','+str(d['info'])+'\n')
f.close