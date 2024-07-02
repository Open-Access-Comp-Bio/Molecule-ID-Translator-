from search_functions import name_search
from search_functions import ncbi_search
from search_functions import uniprot_search
from Bio import Entrez

Entrez.email = "ouranm@gmail.com"

def name_test():
    test_case_1 = "ENSG0000012048"
    test_case_2 = "ENSG0000012048   " 
    test_case_3 = "   ENSG0000012048" #these two test cases are for formatting errors. 
    test_case_4 = "ENSG00000141510"
    test_case_5 = "ENSG00000133703"
    
    expected1 = "BRCA1" 
    expected2 = "TP53" 
    expected3 = "KRAS"
    
    assert name_search(test_case_1) == expected1, "Name Test Case 1 Failed"
    assert name_search(test_case_2) == expected1, "Name Test Case 2 Failed"
    assert name_search(test_case_3) == expected1, "Name Test Case 3 Failed"
    assert name_search(test_case_4) == expected2, "Name Test Case 4 Failed"
    assert name_search(test_case_5) == expected3, "Name Test Case 5 Failed" 
    
def ncbi_test():
    test_case_1 = "BRCA1"
    test_case_2 = "TP53"
    test_case_3 = "KRAS"
    
    expected1 = "672"
    expected2 = "7157"
    expected3 = "3845"
    
    assert ncbi_search(test_case_1) == expected1, "NCBI Test Case 1 Failed"
    assert ncbi_search(test_case_2) == expected2, "NCBI Test Case 2 Failed"
    assert ncbi_search(test_case_3) == expected3, "NCBI Test Case 3 Failed"
    
def uniprot_test():
    test_case_1 = "BRCA1"
    test_case_2 = "TP53"
    test_case_3 = "KRAS"
    
    expected1 = "P38398"
    expected2 = "Q12888"
    expected3 = "P01116"
    
    assert uniprot_search(test_case_1) == expected1, "Uniprot Test Case 1 Failed"
    assert uniprot_search(test_case_2) == expected2, "Uniprot Test Case 2 Failed"
    assert uniprot_search(test_case_3) == expected3, "Uniprot Test Case 3 Failed"