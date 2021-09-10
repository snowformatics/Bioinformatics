# RNA to Protein


DNA = """CACAAACACAGCAACTAATCCACCAGTAGCTTGAGAAGATGAGCACAATCTCACAGTGACTATAAGCAGTACACAGCGCCAGTCAACAACAATAACTATCATCTGAGAAATTCAGGGAAATACTCGACGTACACTAGAAAAATATATCGTAGGACCATCGTCCTCATCTCCTTCCCGAGTTCCCATGTCTTTGGCTGCGGAAATAGCTGAGGAGAACCTGCGCCTTTTCTCTTGCGCGTGGTGTTCCTGACTGTGACAGTGCGACTAAAGGGGGCACGGCATCCTCTTGAAGAACTATGTTGCAAAACCTGCTGCTGTTTGTGCATAGCTGAAGCAATGCCGCGGTAGCATTTTCCTTCGCTTTCGCTGAACCCAGTTCGACAACTTCAACAAGGGCCGGAATACCACGCGCCTGCCCAATCGCAGTCCTTCCTTCTGGTATCGTAGCAAGATTTGCCAAGACAGCTACAGCTTTATCGACCATTCCAGCAGCAGGGTCCATAAGCTCAACTAGGTGCTTCAATGCATCAGCTTGCACAATTCGACCCTTGTTCTCATGAAGTATGGATAAATTAAACAATGCAGTAACCGCATCTTTCTTTCCTCGTGGGCTCCCATTTCCCAGCAAGTCCACGAGAGGCTTTACAGCACCAGATCGCCCTATCCTCACTCTGTTTTCTTCAATAATTGAGAGACTGAA"""
RNA = DNA.replace('T', 'U')

RNA_dictionary = {
  "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
  "UGC":"C", "UGU":"C", "GAC":"D", "GAU":"D",
  "GAA":"E", "GAG":"E", "UUC":"F", "UUU":"F",
  "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
  "CAC":"H", "CAU":"H", "AUA":"I", "AUC":"I",
  "AUU":"I", "AAA":"K", "AAG":"K", "UUA":"L",
  "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L",
  "CUU":"L", "AUG":"M", "AAC":"N", "AAU":"N",
  "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
  "CAA":"Q", "CAG":"Q", "AGA":"R", "AGG":"R",
  "CGA":"R", "CGC":"R", "CGU":"R", "CGG":"R",
  "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S",
  "UCG":"S", "UCU":"S", "ACA":"T", "ACC":"T",
  "ACG":"T", "ACU":"T", "GUA":"V", "GUC":"V",
  "GUG":"V", "GUU":"V", "UGG":"W", "UAC":"Y",
  "UAU":"Y", "UAG":"!", "UAA":"!", "UGA":"!"
}


my_protein = ''
for i in range(0, len(RNA),3):
    codon = RNA[i:i+3]
    if codon in RNA_dictionary.keys():
        my_protein += RNA_dictionary[codon]

print (my_protein)
