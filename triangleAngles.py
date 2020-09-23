#!/usr/bin/env python3
#https://github.com/GoswamiHemant/bch5884
import math

def distance(x1, y1, x2, y2):
    lengthSq = ((x1-x2)**2+(y1-y2)**2)
    return lengthSq
    
print("Please enter all the vertices of the triangle ")
vertex1x = float(input('coordinate-x of vertex-1: '))
vertex1y = float(input('coordinate-y of vertex-1: '))
vertex2x = float(input('coordinate-x of vertex-2: '))
vertex2y = float(input('coordinate-y of vertex-2: '))
vertex3x = float(input('coordinate-x of vertex-3: '))
vertex3y = float(input('coordinate-y of vertex-3: '))

P2 = distance(vertex1x, vertex1y, vertex2x, vertex2y)
Q2 = distance(vertex1x, vertex1y, vertex3x, vertex3y)
R2 = distance(vertex2x, vertex2y, vertex3x, vertex3y)

#P=length of AB
#Q=length of BC
#R=length of CA

P = math.sqrt(P2);  
Q = math.sqrt(Q2);  
R = math.sqrt(R2); 
 
# Here I am using Cosine law to calculate angles alpha, beta and gamma
#A=alpha, B=beta, C=gamma

A = float(math.acos((Q2 + R2 - P2) / (2 * Q * R)));  
B = float(math.acos((P2 + R2 - Q2) / (2 * P * R)));  
C = float(math.acos((P2 + Q2 - R2) / (2 * P * Q)));  
  
    
# Here I am converting radian to degree  

A = A * 180 / math.pi;  
B = B * 180 / math.pi;  
C = C * 180 / math.pi; 

# Here is the command to print all the angles  

print("alpha : %f" %(A))  
print("beta : %f" %(B)) 
print("gamma : %f" %(C))