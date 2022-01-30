A=("a","b")
print(A[1])
g1 = [1,0,0,1,0]
g2 = [0,1,0,1,0]
h1 = [1,0,0,0,0]
h2 = [0,1,0,1,0]
def sign(a,b,c,d,e,f,g,h):
  if c*e+ d*f == a*g +b*h:
    return (0)
  else: 
    return (1)
def mod2 (a):
  if a ==2:
    a= 0
  elif a==1: 
    a==1
  elif a==0:
    a==0
def generator_group (g1,g2,h1,h2):
  g1g2= [(g1[0]+g2[0]),(g1[1]+g2[1]),(g1[2]+g2[2]),(g1[3]+g2[3]), sign(g1[0],g1[1],g1[2],g1[3],g2[0],g2[1],g2[2],g2[3])]
  h1h2= [(h1[0]+h2[0]),(h1[1]+h2[1]),(h1[2]+h2[2]),(h1[3]+h2[3]), sign(h1[0],h1[1],h1[2],h1[3],h2[0],h2[1],h2[2],h2[3])]
  if g1g2[1]==2:
    g1g2[1]=0
  elif g1g2[2]==2:
    g1g2[2]=0
  elif g1g2[3]==2:
    g1g2[3]=0
  elif h1h2[1]==2:
    h1h2[1]=0
  elif h1h2[2]==2:
    h1h2[2]=0
  elif h1h2[3]==2:
    h1h2[3]=0
  return(g1g2,h1h2)
print(generator_group(g1,g2,h1,h2))
List=(1,2,3,4,5)
print(max(List))