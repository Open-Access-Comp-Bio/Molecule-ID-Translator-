#!/usr/bin/env python3

# MyGene ID to OMIM ID converter function

# Modules required for this function:
import requests


def Convert_MyGene_to_OMIM(mygeneid):
    '''This function takes a MyGene ID number as an input, and prints the OMIM ID number as an output.
    If there is not a match in the MyGene database, it prints an error message that the ID is not valid.
    Note: This function is not meant for obtaining the OMIM ID from the common gene code name, only for converting from the MyGene ID number.'''
    r = requests.get(f"https://mygene.info/v3/gene/{mygeneid}?fields=all&dotfield=false&size=10")
    r = r.json()
    try: 
        OMIM_ID = r["MIM"]
        print(OMIM_ID)
    except:
        print("Error: Invalid MyGene ID")


# Testing the function:
Convert_MyGene_to_OMIM(1000)
