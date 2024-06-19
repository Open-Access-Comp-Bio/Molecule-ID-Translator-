import argparse
import re
import time
import requests
from Bio.Seq import Seq
from Bio import SeqIO
import json  # Add this import at the top of your script

def getMoleculeInfo(ensembl_gene_id: str) -> dict:
    """
    Given an Ensembl gene ID, fetch and return information about the molecule.

    Params
    ------
    ensembl_gene_id
        The Ensembl gene ID to lookup.

    Returns
    -------
    A dictionary containing information about the molecule.
    """

    ensembl_server = 'http://rest.ensembl.org'
    endpoint = f'/lookup/id/{ensembl_gene_id}?expand=1'
    headers = {'Content-Type': 'application/json'}
    
    print("Sending request to:", ensembl_server + endpoint)
    response = requests.get(ensembl_server + endpoint, headers=headers)
    
    print("Response status code:", response.status_code)  # Debugging
    if response.status_code == 200:
        molecule_info = response.json()
        
        # Extract keywords
        keywords = []
        if 'display_name' in molecule_info:
            keywords.append(molecule_info['display_name'])
        if 'description' in molecule_info:
            keywords.append(molecule_info['description'])
        if 'synonyms' in molecule_info:
            keywords.extend(molecule_info['synonyms'])  # Assuming synonyms is a list
        if 'gene_family' in molecule_info:
            keywords.append(molecule_info['gene_family']['name'])
        
        # Save keywords to a file
        with open('keywords.txt', 'w') as file:
            for keyword in keywords:
                file.write(keyword + '\n')
        
        print("Molecule info retrieved:", molecule_info)  # Debugging
        
        try:
            with open('molecule_info.txt', 'w') as file:
                json.dump(molecule_info, file)  # Saves the dictionary as JSON
            print("File written successfully.")
        except IOError as e:
            print("File writing error:", e)
        
        return molecule_info
    else:
        print("Failed to retrieve data - Code:", response.status_code, "Response:", response.text)
        return None

def searchMyGene(keywords: list) -> None:
    """
    Search for genes on the myGene API using a list of keywords and write the myGene IDs to a text file.

    Params
    ------
    keywords : list
        A list of keywords to search for.
    """
    server = "http://mygene.info/v3"
    endpoint = "/query"
    results = []

    for keyword in keywords:
        params = {
            'q': keyword,
            'species': 'human'
        }
        response = requests.get(server + endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'hits' in data:
                # Extract only the myGene IDs from the hits
                gene_ids = [hit['_id'] for hit in data['hits'] if '_id' in hit]
                results.extend(gene_ids)
        else:
            print(f"Failed to retrieve data for keyword '{keyword}' - Code:", response.status_code)
            print("Error response:", response.text)

    # Write the results to a text file
    with open('gene_ids.txt', 'w') as file:
        for gene_id in results:
            file.write(gene_id + '\n')

    print("Gene IDs written to gene_ids.txt")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python getMoleInfo_Ensembl.py <Ensembl_Gene_ID>")
        sys.exit(1)
    
    ensembl_gene_id = sys.argv[1]
    result = getMoleculeInfo(ensembl_gene_id)
    if result:
        print("Molecule Information Retrieved Successfully.")
    else:
        print("Failed to retrieve molecule information.")

    # Example usage:
    keywords = ['MC1R', 'melanocortin 1 receptor']  # Example keywords
    searchMyGene(keywords)
