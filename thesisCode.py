A=[] # extend list to include non leading 1s mod 
for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      for l in range(0,2):
        for n in range(0,2):
           for o in range(0,2):
             for p in range(0,2):
               for q in range(0,2):
                 for r in range(0,2):
                  if i+j+k+l>=1 and n+o+p>=1:
                    for m in range(0,2):
                      for n in range(0,2):
                        if k==1 and i==0 and j==0 and  k!=n and k!=o:
                          if p==1 and p!=l:
                            A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                          elif r==1 and p!=1 and q!=1:
                            A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                        elif l==1 and l!=n and l!=o and l!=p and r==1 and l==j==k==0:
                          A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                        elif q==1 and i==l==j==j==n==o==p==r==0:
                          A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                        elif j==1 and n!=j:
                          if o==1 and k!=0: 
                            A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                          elif p==1 and o ==0 and l==0:
                            A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])
                          elif  r ==1 and o== 0 and p==0:
                            A.append([[i,j,k,l,q,m],[0,n,o,p,r,n]])

                        

                        
print(A)
print(len(A))
g1 = [1,0,0,0,0]
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
  else:
    a==a

def generator_group (g1,g2,h1,h2):
  g1g2= [mod2(g1[0]+g2[0]),mod2(g1[1]+g2[1]),mod2(g1[2]+g2[2]),mod2(g1[3]+g2[3]), sign(g1[0],g1[1],g1[2],g1[3],g2[0],g2[1],g2[2],g2[3])]
  h1h2= [mod2(h1[0]+h2[0]),mod2(h1[1]+h2[1]),mod2(h1[2]+h2[2]),mod2(h1[3]+h2[3]), sign(h1[0],h1[1],h1[2],h1[3],h2[0],h2[1],h2[2],h2[3])]
  return(g1g2,h1h2)
  #print(g1g2)
  #change to mod addition
  #just create based questions (sing based on answrs for the generator)

def trace(i,j,k,l,g1g2,h1h2):
  trace=[]
  """
  for i in range(0,2):
    for j in range(0,2):
      for k in range(0,2):
        for l in range(0,2):
  """
  P= [i*g1g2[0],i*g1g2[1],j*g1g2[2],j*g1g2[3],k*h1h2[0],k*h1h2[1],l*h1h2[2],l*h1h2[3]]
  if P[0] == P[4] and P[1] == P[5] and P[2] == P[6] and P[3] == P[7] and g1g2[3]==h1h2[3]:
    trace.append(4)
  elif P[0] == P[4] and P[1] == P[5] and P[2] == P[6] and P[3] == P[7] and g1g2[3] != h1h2[3]:
    trace.append(-4)
  else: 
    trace.append(0)
  #return(trace)
  #print(trace)
  trace_sum= sum(trace)
  #print(trace_sum)   
  #return(trace_sum)






#print(len(A))
g1=[]
g2=[]
h1=[]
h2=[]
for r in range(0,243):
  for s  in range(0,243):
    for t in range(0,243):
      for v in range(0,243):
       g1==(A[r])
       g2==(A[s])
       h1==(A[t])
       h2==(A[v])


