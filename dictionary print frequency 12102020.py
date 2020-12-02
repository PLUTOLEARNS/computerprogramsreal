import json
s = "This is a super idea this \n will change the idea of learning."
wo = s.split()
d={}
for one in wo:
    k = one
    if k not in d:
        co = wo.count(k)
        d[k] = co
        print("COunting dictionaries in lists \n " ,wo)
        print(json.dumps(d,indent = 10))
