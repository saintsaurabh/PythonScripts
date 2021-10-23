z ="Royal Challengers Bangalore"
g =[1,2,("bengaluru",["chennai"]),(("mumbai"),("kolkata"))]
b ={'a':['Guwahati'],('hello'):('world'),11:[['hello world'],(1,2,3,'ajanta')]}

# Challengers
print(z[6:17])

# aglr from Bangalore
print(z[19:26:2])

# Royal in reverse
print(z[-23:-28:-1])

# lengers from Challengers
print(z[-17:-10])

# nnai from chennai
print(g[2][1][0][3:7])

# kka from kolkata
print(g[3][1][::3])

# mumbai in reverse
print(g[3][0][-1:-7:-1])

# bengal from bengaluru
print(g[2][0][:6:])

# iaau from Guwahati
print(b['a'][0][:-8:-2])

# olle from hello world
print(b[11][0][0][-7:-11:-1])