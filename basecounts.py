print('ENTER THE DNA SEQUENCE (paste it, then Enter on an empty line when done.)')
lines=[]
while True:
    line=input()
    if line==" ":
        break
    lines.append(line)

dna=" ".join(lines).upper()
valid_bases=set('ATCG')
if len(dna)==0:
    print('Error:No sequence entered')
elif not set(dna).issubset(valid_bases):
    print('Invalid Input: Sequence contains characters other than A, T, G, C')
else:
    no_c=dna.count('C')
    no_g=dna.count('G')
    no_a=dna.count('A')
    no_t=dna.count('T')
    print('Number of Adenine bases in the sequence is %f.'%no_a)
    print('Number of Guanine bases in the sequence is %f.'%no_g)
    print('Number of Cytosine bases in the sequence is %f.'%no_c)
    print('Number of Thymine bases in the sequence is %f.'%no_t)