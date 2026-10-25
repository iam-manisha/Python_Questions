#78. WAP to extract all the key-value pairs from the dictionary only if the keys are of string datatype and values are integers.
dict={'a':45,'b':56,'c':75,10:"ok"}
for key,values in dict.items():
    if type(key) == str and type(values)== int:
        print(key,values)
        
