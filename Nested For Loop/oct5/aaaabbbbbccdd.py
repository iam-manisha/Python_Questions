st="aaaaabbbbcccdd"
out=""
for i in st:
    count=0
    if i not in out:
        for j in st:
            if i == j:
                count+=1
        out+= i + str(count)
print(out)

