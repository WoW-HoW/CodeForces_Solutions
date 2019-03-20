a=0
for i in range(int(input())):
    b=input()
    if(b=="Tetrahedron"):
        a+=4
    elif(b=="Cube"):
        a+=6
    elif(b=="Octahedron"):
        a+=8
    elif(b=="Dodecahedron"):
        a+=12
    elif(b=="Icosahedron"):
        a+=20
print(a)
