t = {(1,2,3):("hello"),("bye"):["raju"],("bengaluru"):"karnataka"}
r = {1:(1,2,3,"hello","bye"),"pyspider":[("basavangudi")],"qspiders":[("hebbal")]}

print(t[(1,2,3)])
print(r["pyspider"][0][7])
print(r["qspiders"][0][4])
print(t["bengaluru"][5])
print(t["bye"][0])