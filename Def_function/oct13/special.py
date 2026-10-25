#waf to extract only the special characters from the string

def special():
    st=input("enter a string:")
    out=""
    for i in st:
        if  not  i.isalnum():
            out+=i
    print(out)

            
           
special()

#all method in datatypes
# crud operation in list,dict
#
#