# Point mutation

seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'

score = 0
for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        print ('same')
    else:
        score += 1

print (score)