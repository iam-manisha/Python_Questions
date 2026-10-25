#waf to count the no. of vowel in a string 
def vowel():
    st=input("enter a string:")
    count=0
    for i in st:
        if i in "AEIOUaeiou":
            count+=1
            print(count)
vowel()
