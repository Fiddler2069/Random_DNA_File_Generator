# Generates random DNA data file
import random
dna_letter = ['A', 'C', 'T', 'G']
sequence = ""

# seq_length multiplied by 1000 in final version
seq_length = input("Length of Sequence (in multiples of 1000): ")

# actual length determined by multiplier
length = int(seq_length) * 100

file_name = input("File Name: ")

# generate actual random DNA sequence
for x in range(length):
    sequence += random.choice(dna_letter)
print(sequence)
