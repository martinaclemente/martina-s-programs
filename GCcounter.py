def parse_fasta(data):
    sequences = {}
    label = None
    
    for line in data.splitlines():
        if line.startswith(">"):
            label = line[1:]  
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    
    return sequences

def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

def highest_gc_content(fasta_data):
    sequences = parse_fasta(fasta_data)
    
    max_gc_label = None
    max_gc_content = 0.0
    
    for label, dna in sequences.items():
        gc = gc_content(dna)
        if gc > max_gc_content:
            max_gc_content = gc
            max_gc_label = label
    
    return max_gc_label, max_gc_content

fasta_data = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''

label, gc_content_value = highest_gc_content(fasta_data)
print(label)
print(f"{gc_content_value:.6f}")
