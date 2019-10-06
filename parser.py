import argparse
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

def saverResources():
    openedFile = createArgumentParser()
    arl = []
    rl = []
    if(readFileAndCreateTree(openedFile) is not None):
        tree = readFileAndCreateTree(openedFile)
        for node in tree.iter('job'):
            for elem in node.iter('multiple_routings_list_elem'):
                for a in elem.iter():
    return rl

resource_list = saverResources()
print(resource_list)
