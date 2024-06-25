from search_functions import name_search
from search_functions import ncbi_search
from search_functions import uniprot_search
from Bio import Entrez

Entrez.email = input("In compliance with NCBI policy, please input your email:")
e_id = input("Please type in a valid Ensembl ID:").strip() #will add script to account for capitalization errors later. 

display_name = name_search(e_id)
ncbi_search(display_name)
uniprot_search(display_name) 

