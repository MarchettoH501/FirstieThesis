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
                if (i*o+j*p)%2==(l*n)%2:
                  if k==1 and n+o+p>0:
                   A.append([[i,j,k,l],[0,n,o,p]])
                  elif i==n==0 and j==1 and o+p>0:
                    A.append([[i,j,k,l],[0,n,o,p]])
                  elif i==j==n==o==0 and k==p==1:
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
'g1=[]'
'g2=[]'
'h1=[]'
'h2=[]'
def search ():
  theList=[]
  for r in range(0,len(A)):
   G1=(A[r][0])
   G2=(A[r][1])
   theList.append((G1,G2))
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
  
"g1=[1, 0, 0, 0]"
"g2=[0, 1, 0, 1]"
"h1=[1,0,0,0]"
"h2=[0,1,0,1]"
"g3=[1, 0, 0, 0]"
"g4=[0, 1, 0, 1]"
"h3=[1,0,0,0]"
"h4=[0,1,0,1]"
def play(g1,g2,g3,g4,h1,h2,h3,h4):
  check=[[g1,g2],[g3,g4],[h1,h2],[h3,h4]]
  w=0
  streak=[]
  for x in range(0,2):
    for y in range (0,2):
      for a1 in range(0,2):
        for a2 in range(0,2):
          for b1 in range(0,2):
            for b2 in range(0,2):
              checkA1=check[x][0].copy()
              checkA2=check[x][1].copy()
              checkB1=check[y+2][0].copy()
              checkB2=check[y+2][1].copy()
              checkA1.append(a1)
              checkA2.append(a2)
              checkB1.append(b1)
              checkB2.append(b2)
              a= answers(checkA1,checkA2,checkB1,checkB2)[0]
              b=answers(checkA1,checkA2,checkB1,checkB2)[1]
              w =w+(trace(checkA1,checkA2,checkB1,checkB2)*(Vchsh(a,b,x,y)/(4*4*4*4)))
              'w =w+(trace(checkA1,checkA2,checkB1,checkB2)*1)'
              'win =+ sum(w)/len(w)'
              'streak.append(win)'
              checkA1.remove(checkA1[4])
              checkA2.remove(checkA2[4])
              checkB1.remove(checkB1[4])
              checkB2.remove(checkB2[4])
  return(w) 

'play(g1,g2,g3,g4,h1,h2,h3,h4)'
def findStrategyCHSH(A):
  R=[]
  S=search()
  for i in  range(0,len(S)):
    for j in  range(0,len(S)):
      for k in  range(0,len(S)):
        for l in  range(0,len(S)):
          g1=S[i][0]
          g2=S[i][1]
          g3=S[j][0]
          g4=S[j][1]
          h1=S[k][0]
          h2=S[k][1]
          h3=S[l][0]
          h4=S[l][1]
          R.append(play(g1,g2,g3,g4,h1,h2,h3,h4))
  print(max(R))
findStrategyCHSH(A)

  