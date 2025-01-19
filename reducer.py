import sys,json
r=lambda:sys.stdin.readline().strip()
n={}
for l in sys.stdin:
 t,v=l.split("\t");n[t]=json.loads(v)
p={i:1/len(n)for i in n}
for _ in range(10):
 np={}
 for i,v in n.items():
  np[i]=(1-0.85)/len(n)
  for j in v:
   if j in n and n[j]:np[i]+=0.85*p[j]/len(n[j])
 p=np
for i,v in sorted(n.items()):
 print(f"{i}\t{v}\t{p.get(i,1-0.85)/len(n)}")
