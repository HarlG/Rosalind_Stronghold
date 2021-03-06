"""
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, 
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s^c of s


Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT

"""

with open('data/rosalind_revc.txt', 'r') as file:
    dna = file.read().rstrip()

#dna = "ATGGCTGCATACGCGAGGGGGAATTTCAAATACACTCCTCAGACGTTTAAAGTATGGATGCTAGGACGAAAGCGAGGAGTCTATGACAGTCCAACGCAAGCAATATCCAAGCTTCGATTCTTGTGGACCCCTAAGCGCGCATCTATACTCTATCGTCGGACCATCGGGCCTGAGTTCCAAGTACCCCCGCGCGGTGCTATATCACGCTCAGACGGCATGGGACCCGGTTCATTTATCTAATAGCGCGGATCTGCTGATAGAGCTGGAGTAGAGTAAGCCACCTTACTTCAGTCAAGCCCACCGATAGCCTTTAGGCTGGTTCCGGAAACCCTAGGTTCCTCCCCTGCAGCTGAAAATGTGAGAGCTACTCTGTTTTGAGCACGCTGTGAGTGCTGAATCACGCCACAAATTCTGAAGTCAATTAGAATCATGGTAAAGTGTGCGTCAATTTACAAATGATTCCATAGCAAGATGCCGACTTTTCACCCGGTTATCAAAGTGCATTAGAGCAGAAGTTGCTCGTTAATGCTTTCGCTGGTGGCCCGGCCTCTTCATTGCGCACAAATGGCAAGAAACCGGATGCCACCCGCTAGCGGATTTGGAATTCGTTTCTGGTCCGACGGGCTTACCGGGGTCTGGTATGTTCGTGGGCGGGCGATATCAACAATCATGCGCTTAACCCTTAATCTAACAATATACCATGCTTGAAGCTGGTTCTGGCGTAGTCTCATATCAGATCTGCACCCTCTCGGTGCTTCTTCCGACGTAAAGACGATTGAGCGATGGTCATTCTTTGAATGATGTAGTAGGCCTTAAGGATATCACTCGCTGTCGGCACAGGATAGCTGCGCAGACGTAGTCCTGCGAAATAGGGCACTAGGAGGTCAGGGTCGCACACGTCGGCATTGAACCCGATTTGGGCATAGTGTGAAGTTTTGTAATGTCTAGGAAGGAAAGCACATTCCATCCGTACCCGAAGTCACACGCGGGGACGGACGTA"

def complement_DNA (string):
    complement = ''
    comp_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for n in reversed(string):
        complement += comp_dict[n]
    return complement

print(complement_DNA(dna))