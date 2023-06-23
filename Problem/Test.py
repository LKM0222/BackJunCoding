
def roundNum(n):
    if n > int(n) + 0.49:
        return int(n+1)
    else:
        return int(n)
    

print(roundNum(0.3), roundNum(0.5), roundNum(0.7))
print(round(0.6), round(1.5))