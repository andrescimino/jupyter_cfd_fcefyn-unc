# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:00:10 2020

@author: andres
"""
import numpy as np
import sympy as sym


T0=300 #temperatura en el extremo izq
Q=1 #flujo de calor  a lo largo de la barra (uniforme)
L=2 #long de la barra
A=0.1 #area de la sección
k=0.1 #conductividad térmica

"""
Solución con diferencias finitas
"""
nx=5
Deltax=L/(nx-1)

x_df=np.linspace(Deltax, L, nx-1)
M_C=np.zeros((nx+1,nx+1))
RHS=np.zeros(nx+1)
for i in range(1, nx):

    
    M_C[i][i-1] = 1;
    M_C[i][i] = -2;
    M_C[i][i+1]   =  1;
    RHS[i] =-Q/k*Deltax



"""condiciones de contorno"""
M_C[0][0] = -2;
M_C[0][1] = 1;  
RHS[0] =-Q/k*Deltax-T0

M_C[nx][nx] = -1;
M_C[nx][nx-2] = 1;  
RHS[nx] =0
print("MC=" , M_C[:, :])
print("RHS=" ,RHS[ :])

T_cd=np.linalg.solve(M_C, RHS)

T_cd=np.append([T0], T_cd)

""" solución analítica """

T_an=np.linspace(Deltax, L, nx-1)
for i in range(nx-1): T_an[i]=T0+Q/k*L*x_df[i]-Q/2/k*x_df[i]** 2 