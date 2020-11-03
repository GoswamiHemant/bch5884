#!/usr/bin/env python3
import math


def function1(pdb_file):
    
    
	lis = []
	with open(pdb_file) as lines:
		for line in lines:
			words = line.split()
			lis.append(words)
	return lis


list1 = function1("2FA9noend.pdb")
list2 = function1("2FA9noend2mov.pdb")


def function2(list1,list2):
    
    n = len(list1)
    total_sum = 0
    for i in range(n):
        
        v_x = float(list1[i][6])            # listing x coordinate of atoms in 2FA9noend.pdb
        w_x = float(list2[i][6])            # listing x coordinate of atoms in 2FA9noend2mov.pdb
        
        v_y = float(list1[i][7])            # listing y coordinate of atoms in 2FA9noend.pdb
        w_y = float(list2[i][7])            # listing y coordinate of atoms in 2FA9noend2mov.pdb
        
        v_z = float(list1[i][8])            # listing z coordinate of atoms in 2FA9noend.pdb
        w_z = float(list2[i][8])            # listing z coordinate of atoms in 2FA9noend2mov.pdb
        
        total_sum = total_sum + (w_x - v_x)**2 + (w_y - v_y)**2 + (w_z - v_z)**2   #squaring the difference bewteen x, y and z coordinates of atoms in  list 1 and list2. 
    total_sum = total_sum/n     # Dividing the sum of squares by total number of atoms
    total_sum = math.sqrt(total_sum)   #square root of final value
    return total_sum

RMSD = function2(list1,list2)
print("The RMSD between these two protein structures is : %.2f" %RMSD)