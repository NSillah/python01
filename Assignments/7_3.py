fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
for line in inp:
    if not line.strip().startswith("X-DSPAM-Confidence: 0.8475") : continue
pos = line.find(':')
num = float(line[pos+1:]) 
total = float(num)
count = float(total + 1)
print 'Average spam confidence: ', float( total / count )