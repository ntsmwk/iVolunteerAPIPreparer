import json

file = 'RK_Zivildienst_HorstMayer'

with open(file+'.json') as json_file:
    data = json.load(json_file)

    for p in data.keys():
        personId = p
        for k in data[p]:
            if k != 'Person':
                for i in data[p][k]:
                    i['personID']=p

            with open(file+'_'+k+'.json', 'w') as outfile:
                json.dump(data[p][k], outfile)

