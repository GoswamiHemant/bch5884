#!/usr/bin/env python3
import sys


pdbname=sys.argv[1]
f=open(pdbname)
lines=f.readlines()

lis=[]
for line in lines:
	words=line.split()
	lis.append(words)
f.close()

        
mass_list=[]   
num_x = 0.0
num_y = 0.0
num_z = 0.0
den = 0.0

#assigning mass to each atom
for i in range(1337):
    atom = str(lis[i][11])                
    if atom=="C":
        mass_list.append(12.0107)
    elif atom=="N":
        mass_list.append(14.0067)
    elif atom=="S":
        mass_list.append(32.065)
    else:
        mass_list.append(15.999)
        
x_cord = 0
y_cord = 0
z_cord = 0        
        
for i in range(len(lis)):
   
	x = float(lis[i][6])         # x coordinate of atoms in input file
	y = float(lis[i][7])         # y coordinate of atoms in input file
	z = float(lis[i][8])         # z coordinate of atoms in input file
    
	num_x = num_x + mass_list[i]*x   # ∑mixi
	num_y = num_y + mass_list[i]*y   # ∑miyi
	num_z = num_z + mass_list[i]*z   # ∑mizi
	den   = den   + mass_list[i]     # ∑mi
    
	x_cord = x_cord + x               # Here we get ∑xi
	y_cord = y_cord + y               # Here we get ∑yi
	z_cord = z_cord + z               # Here we get ∑zi
    
	cx_cord = num_x/den            # x coordinate of center of mass
	cy_cord = num_y/den            # y coordinate of center of mass
	cz_cord = num_y/den            # z coordinate of center of mass
	
	gx_cord = x_cord/len(lis)      # x coordinate of center of geometry
	gy_cord = y_cord/len(lis)      # y coordinate of center of geometry
	gz_cord = z_cord/len(lis)      # z coordinate of center of geometry
    
CM  = cx_cord,cy_cord,cz_cord  # (x, y and z coordinates of center of mass)


GM = gx_cord,gy_cord,gz_cord    # (x, y and z coordinates of center of geometry)


print (' The center of mass is ({:0.3f}, {:0.3f}, {:0.3f}).'.format(cx_cord,cy_cord, cz_cord))

print (' The center of geometry is ({:0.3f}, {:0.3f}, {:0.3f}).'.format(gx_cord,gy_cord, gz_cord))

#Centering the pdbs based on the user’s choice of geometric center or the center of mass

mode = input("For the pdb centered with center of mass, type CM and for the  pdb centered with geometric center type GM : ")
centerd_lis  = lis.copy()
if mode == 'CM':
    for i in range(len(lis)):
        
        centerd_lis[i][6] = float(lis[i][6]) - CM[0]
        centerd_lis[i][7] = float(lis[i][7]) - CM[1]
        centerd_lis[i][8] = float(lis[i][8]) - CM[2]
else:
    for i in range(len(lis)):
        centerd_lis[i][6] = float(lis[i][6]) - GM[0]
        centerd_lis[i][7] = float(lis[i][7]) - GM[1]
        centerd_lis[i][8] = float(lis[i][8]) - GM[2]
    
f = open("centered.pdb", "w")
for line in lis:

	
	f.write("%-6s%5d %-4s%3s %-1s%4d %8.3f%8.3f%8.3f%6.2f%6.2f %-2s \n" %(line[0],int(line[1]),line[2],line[3],line[4],int(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),line[11]))	

f.close() 

print ("A pdb file has been generated. Please type more centered.pdb now.")