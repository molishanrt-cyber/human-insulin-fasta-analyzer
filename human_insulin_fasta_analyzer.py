from Bio import SeqIO

print("="*50)
print("HUMAN INSULIN FASTA ANALYZER")
print("="*50)

print("="*50)
print("SEQUENCE ANALYSIS")
print("="*50)

record=SeqIO.read("insulin_proj.fasta","fasta")
print("SEQUENCE ID:", record.id)
print("SEQUENCE DESCRIPTION:",record.description)
print("FIRST 50 BASES:", record.seq[:50])
print("LAST 50 BASES:", record.seq[-50:])
print("SEQUENCE LENGTH:",len(record.seq))

print("="*50)
print("NUCLEOTIDE ANALYSIS")
print("="*50)

seq=str(record.seq)
print("A CONTENT:", seq.count("A"))
print("T CONTENT:", seq.count("T"))
print("G CONTENT:", seq.count("G"))
print("C CONTENT:", seq.count("C"))

g=seq.count("G")
c=seq.count("C")
gc_count=(g+c)/(len(record.seq))*100

print("GC CONTENT IS:", round(gc_count,2), "%")

a=seq.count("A")
t=seq.count("T")
at_count=(a+t)/(len(record.seq))*100

print("AT CONTENT:", round(at_count,2), "%")
print("="*50)
if gc_count>50:
    print("Biological Interpretation: The insulin gene is GC-rich")
else:
    print("Biological Interpretation: The insulin gene is AT-rich")
print("="*50)

