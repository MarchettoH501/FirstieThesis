import random
A=[] # extend list to include non leading 1s mod 
for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      for l in range(0,2):
        for n in range(0,2):
           for o in range(0,2):
             for p in range(0,2):
              if i+j+k+l>=1 and n+o+p>=1:
                    if k==1 and i==0 and j==0 and  k!=n and k!=o:
                      if p==1 and p!=l:
                        A.append([[i,j,k,l],[0,n,o,p]])
                    elif l==1 and l!=n and l!=o and l!=p and l==j==k==0:
                      A.append([[i,j,k,l],[0,n,o,p]])
                    elif j==1 and n!=j:
                      if o==1 and k!=0: 
                        A.append([[i,j,k,l],[0,n,o,p]])
                      elif p==1 and o ==0 and l==0:
                        A.append([[i,j,k,l],[0,n,o,p]])
def trace(g1,g2,h1,h2):
    trace=[]
    for i in range(0,2):
      for j in range(0,2):
        for k in range(0,2):
          for l in range(0,2):
            '''
            on't trat it as a2x5, it  a 1x5
            '''
            G= [(i*g1[0]+j*g2[0])%2,(i*g1[1]+j*g2[1])%2,(i*g1[2]+j*g2[2])%2,(i*g1[3]+j*g2[3])%2,(i*g1[4]+j*g2[4])%2 ]
            H= [(k*h1[0]+l*h2[0])%2,(k*h1[1]+l*h2[1])%2,(k*h1[2]+l*h2[2])%2,(k*h1[3]+l*h2[3])%2,(k*h1[4]+l*h2[4])%2]
            if G[0] == H[0] and G[1] == H[1] and G[2] == H[2] and G[3] == H[3] and G[4] == H[4]:
              trace.append(4)
            elif G[0] == H[0] and G[1] == H[1] and G[2] == H[2] and G[3] == H[3] and G[4] != H[4]:
              trace.append(-4)
            else: 
              trace.append(0)
            #return(trace)

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
"theList=[]"
"print(search())"

q1= random.randint(0,1)
q2= random.randint(0,1)
def Vchsh(a,b,x,y):
  if x==1 and y ==1:
    if a==b: 
      return(0)
    else:
      return(1)
  else:
      if a==b: 
        return(1)
      else:
        return(0)

def answers(g1,g2,h1,h2):
  if g1[4]==g2[4]: 
    a= 0
  else:
    a=1
  if h1[4]==h2[4]: 
    b=0
  else:
    b=1
  return(a,b)
  
g1=[1, 0, 0, 0]
g2=[0, 1, 0, 0]
h1=[1,0,0,0]
h2=[0,0,0,1]
def play(g1,g2,h1,h2,x,y):
  w=[]
  streak=[]
  for a1 in range(0,2):
    for a2 in range(0,2):
      for b1 in range(0,2):
        for b2 in range(0,2):
          g1.append(a1)
          g2.append(a2)
          h1.append(b1)
          h2.append(b2)
          w.append(trace(g1,g2,h1,h2)*(Vchsh(answers(g1,g2,h1,h2)[0],answers(g1,g2,h1,h2)[1],x,y))/(16))
          win= sum(w)/len(w)
          streak.append(win)
          g1.remove(g1[4])
          g2.remove(g2[4])
          h1.remove(h1[4])
          h2.remove(h2[4])
  print(streak) 
play(g1,g2,h1,h2,1,1)