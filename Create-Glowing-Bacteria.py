def Cut_the_plasmid_in_middle(u,v):
    b = u.find(v)
    p1 = u[:b+len(v)-2]
    p2 = u[b+len(v)-1:len(u)]
    return p1,p2
def Cut_the_plasmid(x,e,f):
    a1 = x.find(e)
    a2 = x.rindex(f)
    q1 = x[:a1+len(e)-1] 
    q2 = x[a1+len(e)-2:a2+len(f)-1]
    q3 = x[a2+len(f):len(x)]
    return q1,q2,q3
def complementary(i):
    str1 = "ACTG"
    str2 = "TGAC"
    y = i.maketrans(str1, str2)
    #print(x)
    return i.translate(y)
file_input = input()
file = open(file_input, 'r') 
u,v,x,y = file.readlines() 
u = u[:len(u)-1]
v = v[:len(v)-1]
x = x[:len(x)-1]
y = y[:len(x)-1]
e,f = y.split()
m,n = Cut_the_plasmid_in_middle(u,v)
p,q,r = Cut_the_plasmid(x,e,f)
strand = m+q+n
complementary_strand = complementary(strand)
print(strand)
print(complementary_strand)
file.close()
