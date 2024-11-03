def countNucleotides(dna_string, i=0, count= None):
    if count is None:
        count = {'A':0, 'C':0, 'G':0, 'T':0}

    if i == len(dna_string):
        return count['A'], count['C'], count['G'], count['T']
    
    nucleotide = dna_string[i]
    if nucleotide in count:
        count[nucleotide] += 1
    
    return countNucleotides(dna_string, i + 1, count)

dna_string ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
result = countNucleotides(dna_string)

print(result)