import argparse
import xml.etree.ElementTree as ET

# Create an argparser that will help the user with some instruction
def createArgumentParser():
    parser = argparse.ArgumentParser(description='This script will read an AGLibrary compatible XML file and will create all the possibile permutation of the multiple routes field and than will be saved in differentes files.')
    parser.add_argument('-f', '--file', nargs=1, help='Insert the name or path of the file.')
    args = parser.parse_args()
    return args.file[0]

# Open a file passed as parameter and will return the root of the XML
def readFileAndCreateRoot(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    return root


print (createArgumentParser())