fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Invalid file!")
    quit()

for line in fh:
    sline = str.strip(line)
    print (str.upper(sline))
