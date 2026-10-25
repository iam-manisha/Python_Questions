st = 'python'
vowel=0
consonant= 0
for i in st:
    if i in 'aeiouAEIOU':
        vowel+=1
    else:
        consonant+=1
print("Vowel",vowel)
print("Consonant",consonant)
