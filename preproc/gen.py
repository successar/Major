f = open('data/atis.test.w-intent.iob', 'r')
intent = []
utternance = []
labels = []
n = 0
l = 0
# for line in f :
# 	line = line.split('\t')
# 	intents = line[2].strip().split('#')
# 	n += len(intents)
# 	if len(intents) > 1 :
# 		l += 1
# 		print len(intents), l
# 	for i in intents :
# 		intent.append(i.strip())
# 		utternance.append('BOS ' + line[0].strip())
# 		labels.append(line[1].strip())

lines = f.read().split('\n\n')

for line in lines :
	line = line.split('\n')
	ins = line[-1].strip().split('#')
	n += len(ins)
	if len(ins) > 1 :
		l += 1
		print len(ins), l
	line = line[:-1]
	for i in ins :
		intent.append(i.strip())
		utt = ""
		lab = ""
		for u in line :
			u = u.split(' ')
			utt += u[0].strip() + " "
			lab += u[1].strip() + " "
		utternance.append(utt.strip())
		labels.append(lab.strip())


print n
gen = 'test/test'
g = open(gen + '.seq.in', 'w')
for u in utternance :
	g.write(u + '\n')
g.close()
g = open(gen + '.seq.out', 'w')
for u in labels :
	g.write(u + '\n')
g.close()
g = open(gen + '.labels', 'w')
for u in intent :
	g.write(u + '\n')

g.close()
	