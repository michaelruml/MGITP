seznam = [3,15,21,3216,54,21,548,654,21,3,654,987,5,1,5,6,5,4,0,87,98,7,54,654,32,15,4,68,7,54,3,21,5,46,8,7,5,3,1,2,2,33,654,87455458]
print("amount of numbers:", len(seznam))
print("minimum:", min(seznam))
print("maximum:", max(seznam))
print("medium:", sum(seznam)/len(seznam))
print("all:", sum(seznam))
seznam = sorted(seznam)
print("top 5:", seznam[len(seznam)-1], seznam[len(seznam)-2], seznam[len(seznam)-3], seznam[len(seznam)-4], seznam[len(seznam)-5])