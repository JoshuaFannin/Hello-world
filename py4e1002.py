name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    times = words[5]
    time = times.split(":")
    hour = time[0]
    counts[hour] = counts.get(hour,0)+1

lst = counts.items()

lst = sorted(lst)

for k,v in lst:
    print (k,v)