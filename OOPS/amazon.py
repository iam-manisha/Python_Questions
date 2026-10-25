class Amazon:
    products=[{"id":1,
               "name":"Smartphone",
               "price":15999,
               "category":"Electronics"},
               {"id":2,
               "name":"Laptop",
               "price":35999,
               "category":"Electronics"},
               {"id":3,
               "name":"earbuds",
               "price":5999,
               "category":"Electronics"},
               {"id":4,
               "name":"smartwatch",
               "price":6599,
               "category":"Electronics"},               
               {"id":5,
               "name":"speaker",
               "price":999,
               "category":"Electronics"},]

ob1=Amazon()
print("before Modification")
for i in Amazon.products:
    print(i)
print("-"*50)

#modify w.r.t class
#Syntax: var[key]=newvalue

for i in Amazon.products:
    i["Discount"]="5%"
for i in Amazon.products:
    print(i)
for i in ob1.products:
    print(i)

#modify w.r.t Object
#if it is smartphone then add 5%
for i in ob1.products:
    if i["name"]=="Smartphone":
        i["Discount"]="5%"
        break

#ob1.products.append({'id':6,"name":"bike","Price":50000,"category":"2-wheeler"})
ob1.products=["hii"]

for i in Amazon.products:
    print(i)
print('-'*50)
for i in ob1.products:
    print(i)
