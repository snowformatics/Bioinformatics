# GC

seq = """CACAAACACAGCAACTAATCCACCAGTAGCTTGAGAAGATGAGCACAATCTCACAGTGACTATAAGCAGTACACAGCGCCAGTCAACAACAATAACTATCATCTGAGAAATTCAGGGAAATACTCGACGTACACTAGAAAAATATATCGTAGGACCATCGTCCTCATCTCCTTCCCGAGTTCCCATGTCTTTGGCTGCGGAAATAGCTGAGGAGAACCTGCGCCTTTTCTCTTGCGCGTGGTGTTCCTGACTGTGACAGTGCGACTAAAGGGGGCACGGCATCCTCTTGAAGAACTATGTTGCAAAACCTGCTGCTGTTTGTGCATAGCTGAAGCAATGCCGCGGTAGCATTTTCCTTCGCTTTCGCTGAACCCAGTTCGACAACTTCAACAAGGGCCGGAATACCACGCGCCTGCCCAATCGCAGTCCTTCCTTCTGGTATCGTAGCAAGATTTGCCAAGACAGCTACAGCTTTATCGACCATTCCAGCAGCAGGGTCCATAAGCTCAACTAGGTGCTTCAATGCATCAGCTTGCACAATTCGACCCTTGTTCTCATGAAGTATGGATAAATTAAACAATGCAGTAACCGCATCTTTCTTTCCTCGTGGGCTCCCATTTCCCAGCAAGTCCACGAGAGGCTTTACAGCACCAGATCGCCCTATCCTCACTCTGTTTTCTTCAATAATTGAGAGACTGAA"""


gc = round((seq.count('C') + seq.count('G')) / len(seq) * 100)

print (gc)