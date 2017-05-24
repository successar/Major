dir1 = "train/train"
dir2 = "valid/valid"
dir3 = "train2/train"

files = ['.seq.in', '.seq.out', '.labels']
p10 = 498

import random

x = range(4978)
random.shuffle(x)

for f in files :
	fp = open(dir1 + f, 'r')
	g1 = open(dir2 + f, 'w')
	g2 = open(dir3 + f, 'w')
	lines = fp.read().strip().split('\n')
	for i in range(p10) :
		g1.write(lines[i] + "\n")
	for i in range(p10, len(x)) :
		g2.write(lines[i] + "\n")
	g1.close()
	g2.close()
