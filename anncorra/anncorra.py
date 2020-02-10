#!/usr/bin/python
'''
This is the module file to access the function 'explain'
in order to understand the POS tags just by their name
and prints its content in understandable format.
'''
import json
import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))  #path to the directory of current file
JSONFILEPATH = os.path.join(DIR_PATH, 'pos_tags_data.json')   #json file in same folder to access.
DATA = json.loads(open(JSONFILEPATH).read())

def structured_print(dict_tag):
    '''
    structured_print(dict_tag)

        Print the data attributes of a json object format shown below
        dict_tag : a single json object, Passed from the explain() function
        {
            format
                key1 : key1_value
                key2 : key2_value
        }
    '''
    print("POS Tags : ", dict_tag["POS Tags"])
    print("Full form : ", dict_tag["Full Form"])
    print("Desription : ", dict_tag["Description"])
    print("Example : ")
    print(dict_tag["Example"])


def explain(tag):
    '''
    explain(tag)

        Fetch the details of the POS_TAG(tag) from the json file stored in the same folder
        tag: string,  Name of the tag you want to know about
    '''
    for dict_tag in DATA:
        if dict_tag['POS Tags'] == tag:
            structured_print(dict_tag)
