def to_rna(dna_strand):
    
    mapping = {"C": "G", "G": "C", "T": "A", "A": "U"}
    
    return "".join(mapping[word] for word in dna_strand)
