import os
from math import *



def ty(l):
    if l[len(l)-1] != ' ':
        l = l + ' '

    u = 0
    q = 0
    n = []
    while len(l) > u:
        if l[u] == ' ':
            n.append(l[q:u])
            q = u + 1
        u += 1
    return n

  

def r(file):
    a = open(file,'r')
    txt = a.readlines()
    v = []
    i = 0
    while len(txt) > i:
        v.append(txt[i])
        v.append(' ')
        i += 1
    
    p = []
    for t in range(0,len(v)):
       e = 0
       while len(v[t]) > e:
           p.append(v[t][e])
           e += 1

    r = 0
    x = ''
    while len(p) > r:
       if p[r] != '\n':
         x = x + p[r]
       r += 1

    y = ty(x)
    if '' in y:
        y.remove('')

    return y    



def premiere(n):
   files = r'C:\pre\save_premier.txt'
   with open(files,'r') as mx:
      k = [2]
      for a in range(2,n):   
          b = a
          v = []
          p = []
          s = []
          while a > 2:
               if b < 100:
                  v.append(b%(a-1))
               a -= 1
        
            
          if 0 not in v and v != []:
              k.append(b)

          srb = []
          osp = int(sqrt(n))
          slb = 0
          snb = len(k) - 1
          while len(k) > slb:
             if osp >= k[snb]:
                 srb.append(k[0:snb+1])
                 break
             slb += 1
             snb -= 1


          if b > 100:
              d = int(sqrt(b))
              o = 0
              t = len(srb[0])-1
              while len(srb[0]) > o:
                  if d >= srb[0][t]:
                     s.append(srb[0][0:t+1])
                     break
                  o += 1
                  t -= 1   
   
              ln = 0
              while len(s[0]) > ln:
                   p.append(b%s[0][ln])
                   ln += 1
              
              

              if 0 not in p:
                  k.append(b)
           
     
      
      
      m = open(files,'w')
      for tu in range(0,len(k)):
         m.write(str(k[tu]))
         m.write('\n')

      

      
      hv = []
      dx = []
      hp = len(k) - 1
      for su in range(0,len(k)):
          if k[hp] - k[hp-1] > 0:
            hv.append(k[hp] - k[hp-1])
            dx.append(str(k[hp])+' - '+str(k[hp-1]))
            hp = hp - 1

      
      fil = r'C:\pre\distance.txt'
      sl = open(fil,'w')
      sn = open(r'C:\prei\distance2.txt','w')
      io = len(hv)
      while io > 0:
            sl.write(dx[io-1]+' : '+str(hv[io-1]))
            sl.write('\n')
            sn.write(str(hv[io-1]))
            sn.write('\n')
            io -= 1

     
         
         

      m.close()
      sl.close()
      sn.close()
      




def premier(n):
  with open(r'C:\pre\save_premier.txt','r') as ki:
    txt = ki.readlines()
    if txt != []:
      az = r(r'C:\pre\save_premier.txt')
      qd = []
      for aq in range(0,len(az)):
         qd.append(eval(az[aq]))
      if n >= qd[len(qd)-1]:
         srb = []
         osp = int(sqrt(n))
         slb = 0
         snb = len(qd) - 1
         while len(qd) > slb:
             if osp >= qd[snb]:
                 srb.append(qd[0:snb+1])
                 break
             slb += 1
             snb -= 1
         ap = []
         for at in range(qd[len(qd)-1],n):
            ao = int(sqrt(at))
            ad = 0
            af = len(srb[0]) - 1
            aw = []
            ac = []
            while len(srb[0]) > ad:
               if ao >= srb[0][af]:
                  aw.append(srb[0][0:af+1])
                  break
               ad += 1
               af -= 1

            lm = 0
            while len(aw[0]) > lm:
               ac.append(at%aw[0][lm])
               lm += 1

            if 0 not in ac:
               ap.append(at)

         am = open(r'C:\pre\save_premier.txt','a') 
         for aze in range(0,len(ap)):
                ap[aze] = str(ap[aze])
                am.write(ap[aze])
                am.write('\n')
        

         hp = len(ap) - 1
         hv = []
         lc = []
         for su in range(0,len(ap)):
            if eval(ap[hp]) - eval(ap[hp-1]) > 0:
               hv.append(eval(ap[hp]) - eval(ap[hp-1]))
               lc.append(str(ap[hp])+' - '+str(ap[hp-1]))
               hp = hp - 1

         sl =  open(r'C:\pre\distance.txt','a')
         sn = open(r'C:\prei\distance2.txt','a')
         io = len(hv)
         while io > 0:
            sl.write(lc[io-1]+' : '+str(hv[io-1]))
            sl.write('\n')
            sn.write(str(hv[io-1]))
            sn.write('\n')
            io -= 1

         
         am.close()
         sl.close()
         sn.close()
         
      
      else:
          print('go to file C:\pre\save_premier.txt you find what do you want.')
    else:

        premiere(n)          
              
              

      
while True:
   b = input('Enter a value :')
   b = int(b)
   premier(b)
