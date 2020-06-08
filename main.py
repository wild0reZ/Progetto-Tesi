import argparse
import os
import shutil
import itertools
from lxml import etree

# Create an argparser that will help the user with some instruction
def createArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, nargs=1, help='Insert the name or path of the file.')
    args = parser.parse_args()
    return args.f[0]

# Open a file passed as parameter and will return the root of the XML
def readFileAndCreateTree(file_name):
    try:
        tree = etree.parse(file_name)
        return tree 
    except:
        print("No file named: " + file_name + " has been found.")
        return None

def createDirectory():
    path = './output'
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s" % path)
    else:
        print ("Successfully created the directory %s " % path)

def prevision():
    openedFile = createArgumentParser()
    mrlList = []
    ris = 1
    jobNumber = 0
    mrlrNumber = 0
    itpNumber = 0
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'): # Cerco all'interno del file XML tutti i tag job
            for elem in node.iter('multiple_routings_list_elem'): # Cerco tutti i child di job con tag multiple_routings_list_elem
                jobNumber += 1
                #print('Job number ', jobNumber)
                mrlrNumber += 1
                #print('Multi Route number', mrlrNumber)
                itpNumber = 0
                for a in elem.iter(): # Inizio a cercare gli id_time_profile
                    if(a.tag == 'id_time_profile'):
                        itpNumber += 1
                        #print('Id Time Profile number ', itpNumber)
                mrlList.append(itpNumber)
    for x in mrlList:
        ris = ris * x
    print('La previsione del numero di file prodotti è pari a: ', ris)
    for i in range(0, 101):
        perc = (ris*i)/100
        print('Prendendo il ', i, ' %', ' devo salvare: ', perc, ' file')
    #return arl


def extractDataFromXML():
    openedFile = createArgumentParser()
    jobNumber = 0
    mrlrNumber = 0
    itpNumber = 0
    shutil.copyfile(openedFile, './output/{0}'.format(os.path.basename('template.xml')))
    arl = [] # Creo una lista che ospiterà tutte le liste degli id_time_profile
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'): # Cerco all'interno del file XML tutti i tag job
            for elem in node.iter('multiple_routings_list_elem'): # Cerco tutti i child di job con tag multiple_routings_list_elem
                tmp = [] # Inizializzo una lista vuota che conterrà tutti gli id_time_profile del singolo multiple_routings_list_elem
                jobNumber += 1
                mrlrNumber += 1
                print(elem.tag)
                for a in elem.iter(): # Inizio a cercare gli id_time_profile
                    if(a.tag == 'id_time_profile'):
                        itpNumber += 1
                        print(a.tag)
                        tmp.append(a.text) # Li salvo all'interno della lista
                arl.append(tmp) # Salvo la lista all'interno della lista di tutti i multiple_routings_list_elem

    print('[DEBUG] Ci sono %d jobs, %d multiple routings, %d id time profile',  jobNumber,  mrlrNumber,  itpNumber)
    return arl

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
        tree.write('./output/'+export+ '_' +str(count)+'.xml', encoding='utf-8', xml_declaration=True)
        print("Saving file number: ", count+1)
        count += 1
    os.remove('./output/template.xml')

def removeSpaces():
    count = 1
    print('Removing unnecessary spaces. Wait')
    for filename in os.listdir(os.chdir('./output')):
        # first get all lines from file
        with open(filename, 'r+') as f:
            lines = f.readlines()
        # remove spaces
        print('Working on file ', count)
        lines = [line.replace(' , ', ', ') for line in lines]

        # finally, write lines in the file
        with open(filename, 'w+') as f:
            f.writelines(lines)
        count += 1
        

def main():
    exportModifiedXML()
    removeSpaces()
    #prevision()

if __name__ == "__main__":
    main()
