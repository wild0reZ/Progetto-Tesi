import argparse
from itertools import permutations, product
import xml.etree.ElementTree as ET

# Create an argparser that will help the user with some instruction
def createArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, nargs=1, help='Insert the name or path of the file.')
    args = parser.parse_args()
    return args.f[0]

# Open a file passed as parameter and will return the root of the XML
def readFileAndCreateTree(file_name):
    try:
        tree = ET.parse(file_name)
        return tree 
    except:
        print("No file named: " + file_name + " has been found.")
        return None

# Testing ArgumentParse and XML Parse
def printResources():
    openedFile = createArgumentParser()
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'):
            print('\n')
            for elem in node.iter():
                if (elem.tag == 'id_job'):
                    print('job_id:', elem.text)
                if (elem.tag == 'id_resource'):
                    print('id_resource', elem.text)
                if (elem.tag == 'id_time_profile'):
                    print('id_time_profile', elem.text)

def saveResources():
    openedFile = createArgumentParser()
    arl = [] # Creo una lista che ospiterà tutte le liste degli id_time_profile
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'): # Cerco all'interno del file XML tutti i tag job
            for elem in node.iter('multiple_routings_list_elem'): # Cerco tutti i child di job con tag multiple_routings_list_elem
                tmp = [] # Inizializzo una lista vuota che conterrà tutti gli id_time_profile del singolo multiple_routings_list_elem
                for a in elem.iter(): # Inizio a cercare gli id_time_profile
                    if(a.tag == 'id_time_profile'):
                        tmp.append(a.text) # Li salvo all'interno della lista
                arl.append(tmp) # Salvo la lista all'interno della lista di tutti i multiple_routings_list_elem
    return arl

def saveResources2():
    openedFile = createArgumentParser()
    arl = [] # Creo una lista che ospiterà tutte le liste degli id_time_profile
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'): # Cerco all'interno del file XML tutti i tag job
            tmp1 = []
            for elem in node.iter('multiple_routings_list_elem'): # Cerco tutti i child di job con tag multiple_routings_list_elem
                tmp = [] # Inizializzo una lista vuota che conterrà tutti gli id_time_profile del singolo multiple_routings_list_elem
                for a in elem.iter(): # Inizio a cercare gli id_time_profile
                    if(a.tag == 'id_time_profile'):
                        tmp.append(a.text) # Li salvo all'interno della lista
                tmp1.append(tmp) # Salvo la lista all'interno della lista di tutti i multiple_routings_list_elem
            arl.append(tmp1)
    return arl

def product_perms(data):
    count  = 0
    perms = [list(map(list,permutations(subl))) for subl in data]
    for data in product(*perms):
        count += 1 
        print(list(data))
    print(count)

product_perms(saveResources())