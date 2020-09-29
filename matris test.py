# -*- coding: utf-8 -*-
import random

class matris(object):
    def __init__(self,y,x):
        """initiliaze a matris so it can be created via user input or randomly"""
        self.dx={}
        self.abc="abcdefghijklmnoprqstuvwxyz"
        self.x=x
        self.y=y
        for i in range(y):
            for j in range(x):
                self.dx[self.abc[i]+str(j)]=0
    def creatematris(self):
        """creates a matris via user input"""
        for i in range(self.x):
            for k in range(self.y):
                n=raw_input("add an elemet to matris : ")
                self.dx[self.abc[i]+str(k)]=n
        print ("done")

    def returnaline(self,n):
        """returns the requested line of the matris assumes n:int>=0"""
        line=[]
        for i in range(self.x):
            line.append(self.dx[self.abc[n]+str(i)])
        return line
    def returnacolumn(self,n):
        """returns the requested column of the matris assumes n:int>=0"""
        col=[]
        for i in range(self.y):
            col.append(self.dx[self.abc[i]+str(n)])
        return col

    def createrandom(self):
        """creates a random matris"""
        for i in range(self.y):
            for k in range(self.x):
                self.dx[self.abc[i]+str(k)]=random.randint(1,10)

    def __str__(self):
        """ prints out matris"""
        t=""
        for i in range (self.y):
            t+=str(self.returnaline(i))+" \n"
        return t
    def mvalue(self):
        """assumes m:matris and returns its base value"""
        x= self.dx.keys()
        x.sort()
        val=0
        for n in range(len(x)):
            val +=(self.dx[x[n]]*self.dx[x[len(x)-n-1]])
        return val

            
        
    def __lt__(self,other):
        """ compares 2 matris and returns true if self<other"""
        return self.mvalue()<other.mvalue()
    def __add__(self,other):
        """add given matris to matris 
        assumes other:matris"""
        x= self.dx.keys()
        x.sort()
        rm=matris(self.x,self.y)
        if self.x !=other.x and self.y!=other.y:
            raise TypeError("matris has to be the same size")
        for i in x:
            rm.dx[i]=self.dx[i]+other.dx[i]
        return rm
    def __sub__(self,other):
        """substrack gıven matrıs from matrıs 
        assumes other:matris"""
        x= self.dx.keys()
        x.sort()
        rm=matris(self.x,self.y)
        if self.x !=other.x and self.y!=other.y:
            raise TypeError("matris has to be the same size")
        for i in x:
            rm.dx[i]=self.dx[i]-other.dx[i]
        return rm
    def __mul__(self,other):
        """mutiply matris with given matrices 
        assumes other:matris"""
        rm=matris(self.y,other.x)
        x= rm.dx.keys()
        x.sort()
        if type(other)==int or type(other)==float:
            for i in x:
                rm.dx[i]=self.dx[i]*other
            return rm
        elif self.x !=other.y: 
            raise TypeError("matris has to be the same size")
        else:
            for k in range(self.y):
                line=self.returnaline(k)
                for j in range(other.x):
                        col=other.returnacolumn(j)
                        for i in range(len(line)):
                            a=line[i]
                            b=col[i]
                            rm.dx[self.abc[k]+str(j)] += a*b
            return rm
    def row(self,n):
        row=[]
        for i in range(self.x):
            row.append(self.abc[n]+str(i))
        return row
    def col(self,n):
        co=[]
        for i in range(self.y):
            co.append(self.abc[i]+str(n))
        return co
            
    def transpoze(self):
        """ finds given matrices transpozes  """ 
        ans=matris(self.x,self.y)
        for i in range(self.y):
            for k in range(self.x):
                ans.dx[self.abc[k]+str(i)]=self.dx[self.abc[i]+str(k)]
        return ans

    def __div__(self,other):
        raise NotImplementedError("not implemented yet")
    def det2(self):
        return self.dx["a0"]*self.dx["b1"]-self.dx["a1"]*self.dx["b0"]
    def cofactor(self,n):
        """finds given matrices cofactor for given indecis 
        assumes n : string""" 
        cofacmat=matris(self.y-1,self.x-1)
        st=self.dx.copy()
        line=self.row(self.abc.index(n[0]))
        col=self.col(n[1])
        for j in line :
            if j in st.keys():
                st.pop(j)
        for i in col:
            if i in st.keys(): st.pop(i)     
        num,roww=0,0
        for nii in sorted(st.keys()):
            cofacmat.dx[self.abc[roww]+str(num)]=st[nii]
            num+=1
            if num==self.x-1:
                    num=0
                    roww+=1
        return cofacmat

                
        

m,n=matris(2,2),matris(3,3)
m.createrandom(),n.createrandom()

print (n,"\n")
x,y,z= n.cofactor("a0"),n.cofactor("a1"),n.cofactor("a2")

print (x,y,z,x.det2(),y.det2(),z.det2())
print (x.det2()*n.dx["a0"]-y.det2()*n.dx["a1"]+z.det2()*n.dx["a2"])

                
                
                
        

            
      
        
        