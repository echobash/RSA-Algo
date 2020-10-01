# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 17:30:18 2018


"""
#let p,q be two random prime nos.
p = 37
q = 79
N=p*q
phiN=(p-1)*(q-1) #This calculates the totient
e=5       #Satisfying the condition gcd(e,phiN)=1
k=3       #This value of k returns an integer for d. Found by plugging values from 0 to n where k belongs to Z(trial&error)
d=(1+(k*phiN))/5
C=(17**5)%2923
print("LCM(p,q),N= ",N)
print("Totient function,phiN= ",phiN)
print("Encryption value,e= ",e)
print("Decryption value,d= ",d)
M=17      #This is the message to be sended to some random guy/girl
print("Encryption key is given by C=(M**e)modN\n=> C=(17**5)mod2923\n=> C=",C)             #This key is private
print("Decryption key is given by M=(C**d)modN\n=> M=(2202**1685)mod2923\n=> M=",((2202**1685)%2923))  #This key is public




