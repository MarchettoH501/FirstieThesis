A=[] # extend list to include non leading 1s mod 
for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      for l in range(0,2):
        for n in range(0,2):
           for o in range(0,2):
             for p in range(0,2):
              if i+j+k+l>=1 and n+o+p>=1:
                for m in range(0,2):
                  for n in range(0,2):
                    if k==1 and i==0 and j==0 and  k!=n and k!=o:
                      if p==1 and p!=l:
                        A.append([[i,j,k,l,m],[0,n,o,p,n]])
                    elif l==1 and l!=n and l!=o and l!=p and l==j==k==0:
                      A.append([[i,j,k,l,m],[0,n,o,p,n]])
                    elif j==1 and n!=j:
                      if o==1 and k!=0: 
                        A.append([[i,j,k,l,m],[0,n,o,p,n]])
                      elif p==1 and o ==0 and l==0:
                        A.append([[i,j,k,l,m],[0,n,o,p,n]])

                        

'''                       
print(A)
print(len(A))
g1 = [1,0,0,0,0]
g2 = [0,1,0,1,0]
h1 = [1,0,0,0,0]
h2 = [0,1,0,1,0]
'''
def sign(a,b,c,d,e,f,g,h):
  if c*e+ d*f == a*g +b*h:
    return (0)
  else: 
    return (1)

def generator_group (g1,g2,h1,h2): 
  g1g2= [(g1[0]+g2[0])%2,(g1[1]+g2[1])%2,(g1[2]+g2[2])%2,(g1[3]+g2[3])%2, sign(g1[0],g1[1],g1[2],g1[3],g2[0],g2[1],g2[2],g2[3])]
  h1h2= [(h1[0]+h2[0])%2,(h1[1]+h2[1])%2,(h1[2]+h2[2])%2,(h1[3]+h2[3])%2, sign(h1[0],h1[1],h1[2],h1[3],h2[0],h2[1],h2[2],h2[3])]
  '''
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
  '''
 
  #print(g1g2)
  #change to mod addition
  #just create based questions (sing based on answrs for the generator)

def trace(g1,g2,h1,h2):
    trace=[]
    G= [(g1[0]+g2[0])%2,(g1[1]+g2[1])%2,(g1[2]+g2[2])%2,(g1[3]+g2[3])%2,(g1[4]+g2[4])%2 ]
    H= [(h1[0]+h2[0])%2,(h1[1]+h2[1])%2,(h1[2]+h2[2])%2,(h1[3]+h2[3])%2,(h1[4]+h2[4])%2]
    for i in range(0,2):
      for j in range(0,2):
        for k in range(0,2):
          for l in range(0,2):
            '''
            on't trat it as a2x5, it  a 1x5
            '''
            if i*G[0] == k*H[0] and i*G[1] == k*H[1] and j*G[2] == l*H[2] and j*G[3] == l*H[3] and G[4] == H[4]:
              trace.append(4)
            elif i*G[0] == k*H[0] and i*G[1] == k*H[1] and j*G[2] == l*H[2] and j*G[3] == l*H[3] and G[4] != H[4]:
              trace.append(-4)
            else: 
              trace.append(0)
    #return(G,H,trace)
    #print(trace)
    trace_sum= sum(trace)
    #print(trace_sum)   
    return(trace_sum)

#print(len(A))
g1=[]
g2=[]
h1=[]
h2=[]
def search ():
  theList=[]
  for r in range(0,len(A)):
    for s  in range(0,len(A)):
      g1=(A[r][0])
      g2=(A[r][1])
      h1=(A[s][0])
      h2=(A[s][1])
      theList.append(trace(g1,g2,h1,h2))
    return(theList)
theList=[]
print(search())


'''
Found the error: its when I select g1 and g2, and h1 and h2
'''