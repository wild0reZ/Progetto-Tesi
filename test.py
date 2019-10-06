import xmltodict
import json

with open('./testingFiles/esempio_nuovo_formato_bis.xml') as fd:
    doc = xmltodict.parse(fd.read())

#print(json.dumps(doc, indent=4))
#print(json.dumps(doc['root']['job']['multiple_routings_list_elem'], indent=4))
def myPrint(doc):
    for k,v in doc.items():
        if isinstance(v, dict):
            myPrint(v)
        else:
            print("{0} : {1}".format(k, v))

myPrint(doc)

