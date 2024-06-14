#Ensembl to GenBank + RefSeq for NCBI. 
#This is just my first attempt at this kind of project and am only aiming to print out the ID's for NCBI. 
#Example: ENSG00000012048 
import requests
import re
from Bio import Entrez
import urllib.parse
import json

Entrez.email = input("In compliance with NCBI policy, please input your email:") 
e_id = input("Please type in a valid Ensembl ID:") 
#For future scripts, will try to have this be a list or data frame column to loop through 
# but let's just focus on getting this to work with one for now. - 061324

#search Ensembl API for 'e_id' and obtain the gene name - function
def database_search(gene_id):
    url = f"https://rest.ensembl.org/lookup/id/{gene_id}?content-type=application/json"
    response = requests.get(url)
    genbank_ids=[]
    refseq_ids = []
    if response.status_code==200:
        data = response.json()
        display_name = data.get("display_name", "No display name found.")
        print("The gene's name is " + display_name)
        url = urllib.parse.quote(display_name)
        search_handle = Entrez.esearch(db="gene", term=url,remode="json")
        search_results = Entrez.read(search_handle)
        search_handle.close()
        gene_ids = search_results["IdList"]
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    for i in gene_ids:
        fetch_handle = Entrez.efetch(db="gene", id=i, retmode="json")
        #bug to be fixed here, error = Exception has occurred: JSONDecodeError - 061324
        gene_info = json.load(fetch_handle)
        fetch_handle.close()
        refseq_id = gene_info.get("refseqrna",[])
        genbank_id=gene_info.get("genbank", [])
        refseq_ids.append(refseq_id)
        genbank_ids.append(genbank_id)
    print(refseq_ids)
    print(genbank_ids)
        
    
        
        
    
#use obtained gene name to search the NCBI API and obtain the GeneBank and RefSeq ID's - function

#Save those codes and print them out. 

#Actual Loop
#Check if ID is good. "ENSG" for humans otherwise, 
# there is a three letter code for the species then a 11 number code with a period followed by the version. 
#For now, this script will only look at human sequences. 
e_id_format = r"^ENSG\d{10}\.\d$"
e_id_format2 = r"^ENSG\d{11}$"

if re.match(e_id_format, e_id) or re.match(e_id_format2, e_id):
    print("Valid ID has been entered")
    #continue on inputting e_id into the first function. 
    database_search(e_id)
   
    #Check to see if the gene name is in the NCBI API. 
    #Extract any and all ID's associated with said name. 
    #Do another if statment seeing if there is GeneBank and/or RefSeq ID's, and if not then have an error print out. 
    #If either ID is present then have it print out. 
    #Will probably have the ID's saved in a list in case there are isotopes or other versions of hte gene that need to be printed out. 
else:
    print("Invalid ID")
    