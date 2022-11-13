class Farhad:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def sow(self):
        print(pow(self.a,self.b))
        print(pow(self.a,self.b,self.c))
farhad=Farhad(a=int(input()),b=int(input()),c=int(input()))
farhad.sow()