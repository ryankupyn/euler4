import palinchecker
palinlist = []
for n1 in range(100,999):
    for n2 in range(100,999):
        if palinchecker.main(n1*n2) == True:
            palinlist.append(n1*n2)
            print("first: " + str(n1) + " second: " + str(n2) + " total: " + str(n1*n2))
print max(palinlist)