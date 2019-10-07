import argparse
import os
import shutil
import itertools
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

def createDirectory():
    path = './output'
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def extractDataFromXML():
    openedFile = createArgumentParser()
    shutil.copyfile(openedFile, './output/{0}'.format(os.path.basename('template.xml')))
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

def allThePerms(data):
    count  = 0
    tmp = []
    # Dato che, come parametro gli sto passando una lista di liste, mi calcolo tutte le possibili permutazioni
    # attraverso map che prende due parametri, list che consente appunto di creare una lista e l'altro
    # permutations(sublist) che, attraverso la funzione permutations calcola tutte le possibili permutazioni
    # di una sublist estratta dalla lista di liste.
    # In fine calcoliamo il prodotto cartesiano tra le liste attraverso la funzione product.  
    perms = [list(map(list,itertools.permutations(sublist))) for sublist in data]
    for data in itertools.product(*perms):
        count += 1 
        tmp.append(data)
    return tmp

def rotate(l, n):
    return l[n:] + l[:n]

def allThePermsRotation(data):
    listOfAllRotations = []
    allRotationsCartesianProduct = []
    for sublist in data:
        allThePerms = []
        for i in range(len(sublist)):
            allThePerms.append(rotate(sublist, i))
        listOfAllRotations.append(allThePerms)
    for data in itertools.product(*listOfAllRotations):
        allRotationsCartesianProduct.append(data)
    return allRotationsCartesianProduct 

# Cambiare il nome del file cone nome file originale + contatore
def exportModifiedXML():
    createDirectory()
    path = str(createArgumentParser())
    rest, fileName = os.path.split(path)
    export = fileName.split('.')[0]
    allThePermsTuples = allThePermsRotation(extractDataFromXML())
    count = 0
    for subl in allThePermsTuples:
        tree = readFileAndCreateTree('./output/template.xml')
        out = list(itertools.chain(*subl)) 
        for (a, e) in zip(tree.findall('.//job//multiple_routings_list_elem//id_time_profile'), out):
            a.text = e
        tree.write('./output/'+export+ '_' +str(count)+'.xml')
        print("Saving file number: ", count+1)
        count += 1
    os.remove('./output/template.xml')

def main():
    exportModifiedXML()


if __name__ == "__main__":
    main()