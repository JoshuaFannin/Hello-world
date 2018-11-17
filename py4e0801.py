fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Invailid file name!')
    quit

lst = list()

for line in fh:
    words = (line.split())
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
