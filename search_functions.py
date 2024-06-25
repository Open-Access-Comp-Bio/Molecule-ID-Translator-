#Ensembl to NCBI Accession Codes for homo sapiens. 
#This is just my first attempt at this kind of project and am only aiming to print out the ID's for NCBI. 
#Example: ENSG00000012048 
import requests
import re
from Bio import Entrez
import urllib.parse
import json
import xml.etree.ElementTree as ET
from constants import uniprot_url


#For future scripts, will try to have this be a list or data frame column to loop through 
# but let's just focus on getting this to work with one for now. - 061324

def name_search(gene_id):
    e_id_format = r"^ENSG\d{10}\.\d$"
    e_id_format2 = r"^ENSG\d{11}$"

    if re.match(e_id_format, gene_id) or re.match(e_id_format2, gene_id):

        print("Valid ID has been entered")


        url = f"https://rest.ensembl.org/lookup/id/{gene_id}?content-type=application/json"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
        
        else:
            data = response.json()
            #print(f"Ensembl data: {data}") This is only for current troubleshooting and will be taken out later 
            
            display_name = data.get("display_name", "No display name found.")
            print(f"Gene name is {display_name}") 
            return display_name
    else:
        print("Invalid ID")

def ncbi_search(display_name): #for finding Gene ID from NCBI
    
    search_term = f"{display_name}[Gene] AND Homo sapiens[Organism]"
    
    handle = Entrez.esearch(db="gene", term=search_term)
    record = Entrez.read(handle)
    handle.close()
    
    if not record["IdList"]:
        print("No ID is found.")
    else: 
        found_id = record["IdList"][0]
        print(f"NCBI Gene ID:{found_id}")
            
def uniprot_search(display_name):
    query = f"gene:{display_name} AND organism_id:9606"
    
    params = {
        "query": query,
        "format":"json",
        "size": 10
    }
    
    response = requests.get(uniprot_url, params=params)
    
    if response.status_code != 200:
        print(f"Unable to fulfill request: {response.status_code}")
    else:
        data=response.json()
        for i in data.get("results", []):
            accession_codes = i.get("primaryAccession")
    print(f"Uniprot ID: {accession_codes}")
        
            

    

#Still need to add error handling and figure out what format we want the output to be now that I am able to produce a result. - 061724
 