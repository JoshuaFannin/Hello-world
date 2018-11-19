fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('Invalid file!')
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    input = line.find(' ')
    num = line[input+1 : ]
    grade = num.strip()
    total = total + float(grade)
print ('Average spam confidence:', total / count)
