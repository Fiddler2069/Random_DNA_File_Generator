# This program generates random DNA data file of arbitrary size

import random
dna_letter = ['A', 'C', 'T', 'G']
sequence = ""

# seq_length multiplied by 1000 in final version
seq_length = input("Length of Sequence (in multiples of 1000): ")

# actual length determined by multiplier
length = int(seq_length) * 1000

# put each 1000 dna sequence into a separate string for writing to file

file_name = input("File Name: ")

# Code Execution time code
# import time
# start_time = time.time()

# generate actual random DNA sequence
for x in range(length):
    sequence += random.choice(dna_letter)
print(sequence)

# Print Code execution time
# print ("time elapsed: {:.2f}s".format(time.time() - start_time))
# 10,000 bases takes about 0.01 seconds to generate
