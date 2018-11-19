text = "X-DSPAM-Confidence:    0.8475"
input = text.find(' ')
num = text[input+1 : ]
answer = num.strip()
print (float(answer))
