# Loop over the lines
# Remove the spaces.
# Split the lines by using the split() function the CSV seperator split(\t).
data = open('test.csv', 'r')
# Open a new file in write mode and use the ending fasta (e.g. test.fasta)
f_out = open('test.fasta', 'w')

for line in data:
    line = line.strip()
    line_split = line.split('\t')
    # Print out line [0] and line[1] inside the loop.
    print (line_split[0], line_split[1])
    f_out.write('>' + line_split[0] + '\n')
    f_out.write(line_split[1] + '\n')
f_out.close()