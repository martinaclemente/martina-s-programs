def complement(dna_string, i=0):
    if i == len(dna_string):
        return ''
    
    current_nucleotide = dna_string[i]
    if current_nucleotide == 'T':
        new_nucleotide = 'A'
    elif current_nucleotide == 'A':
        new_nucleotide = 'T'
    elif current_nucleotide == 'C':
        new_nucleotide = 'G'
    elif current_nucleotide == 'G':
        new_nucleotide = 'C'
    else:
        new_nucleotide = '' 
    
    return new_nucleotide + complement(dna_string, i + 1)

dna_string = 'AAAACCCGGT'
complement_result =  complement(dna_string)

def reverse(complement_result):
    if len(complement_result) == 0:
        return ''
    else:
        return complement_result[-1] + reverse(complement_result[:-1])

reversed_result = reverse(complement_result)
print(reversed_result)