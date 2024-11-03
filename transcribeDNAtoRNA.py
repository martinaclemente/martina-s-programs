def transcribeDNAtoRNA(dna_string, i=0):
    if i == len(dna_string):
        return ''
    
    current_nucleotide = dna_string[i]
    if current_nucleotide == 'T':
        rna_nucleotide = 'U'
    else:
        rna_nucleotide = current_nucleotide
    
    return rna_nucleotide + transcribeDNAtoRNA(dna_string, i + 1)

dna_string = 'GATGGAACTTGACTACGTAAATT'
rna_string = transcribeDNAtoRNA(dna_string)

print(rna_string)