import argparse
import xml.etree.ElementTree as ET

# Create an argparser that will help the user with some instruction
def createArgumentParser():
    parser = argparse.ArgumentParser(description='This script take as input an XML AGLibrary compatible file and will produce all the possible permutation of the multiple routing.')
    parser.add_argument('-f', '--file', required=True, nargs=1, help='Insert the name or path of the file.')
    args = parser.parse_args()
    return args.file[0]

# Open a file passed as parameter and will return the root of the XML
def readFileAndCreateRoot(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
        return root
    except:
        print("No file named: " + file_name + " has been found.")
        return None

# Testing ArgumentParse and XML Parse
def printRoot():
    openedFile = createArgumentParser()
    if(readFileAndCreateRoot(openedFile) is not None):
        root = readFileAndCreateRoot(openedFile)
        for child in root:
            print(child.tag)

printRoot()