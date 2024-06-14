#Ensembl to GenBank + RefSeq for NCBI. 
#This is just my first attempt at this kind of project and am only aiming to print out the ID's for NCBI. 
import requests
import re

e_id = input("Please type in a valid Ensembl ID:") 
#For future scripts, will try to have this be a list or data frame column to loop through 
# but let's just focus on getting this to work with one for now. - 061324

#search Ensembl API for 'e_id' and obtain the gene name - function

#use obtained gene name to search the NCBI API and obtain the GeneBank and RefSeq ID's - function

#Save those codes and print them out. 

#Actual Loop
#Check if ID is good. "ENSG" for humans otherwise, 
# there is a three letter code for the species then a 11 number code with a period followed by the version. 
e_id_format = r"^ENSG\d{10}\.\d$"
e_id_format2 = r"^ENSG\d{11}$"

if re.match(e_id_format, e_id) or re.match(e_id_format2, e_id):
    print("Valid ID has been entered")
    #continue on inputting e_id into the first function. 
    #Check to see if the gene name is in the NCBI API. 
    #Extract any and all ID's associated with said name. 
    #Do another if statment seeing if there is GeneBank and/or RefSeq ID's, and if not then have an error print out. 
    #If either ID is present then have it print out. 
    #Will probably have the ID's saved in a list in case there are isotopes or other versions of hte gene that need to be printed out. 
else:
    print("Invalid ID")
    