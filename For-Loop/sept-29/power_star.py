s= 'power star'
# Out = {'power': 5, 'star': 4}
out={}
for i in s.split():
    #var[key]=new value
    out[i] = len(i)
print(out)

# S = 'power star'
# Out = {'power': 'rewop', 'star': 'rats'}
s= 'power star'
out={}

for i in s.split():
    out[i] = i[::-1]
print(out)
