def computepay(h, r):
    p = (r * 40) + ((h-40)*(r*1.5))
    return p


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Invalid Value")
    quit()
if h <= 40:
    p = h * r
elif h > 40:
    p = computepay(h, r)
print("Pay", p)
