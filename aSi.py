# Initial random configuration of amorphous silicon with N=1000 atoms
# The cubic box size is L=27.8 Angstrom
# Periodic Boundary Conditions were imposed in the x,y,z direrctions
# Raymond Atta-Fynn; Department of Physics; UT Arlington
# I do this in Fortran; I am trying out Python for fun

import math as m
import random

x=list()
y=list()
z=list()

L = 27.8
N = 1000
rcut = 2.2

i=1

x.append(0.5*L*random.uniform(-1,1))
y.append(0.5*L*random.uniform(-1,1))
z.append(0.5*L*random.uniform(-1,1))

while i < N:
  x0=0.5*L*random.uniform(-1,1)
  y0=0.5*L*random.uniform(-1,1)
  z0=0.5*L*random.uniform(-1,1)

  iflag = 0

  for j in range(i):
    x1=x[j]-x0
    y1=y[j]-y0
    z1=z[j]-z0
    if x1 >  0.5*L: x1 = x1 - L
    if x1 < -0.5*L: x1 = x1 + L
    if y1 >  0.5*L: y1 = y1 - L
    if y1 < -0.5*L: y1 = y1 + L
    if z1 >  0.5*L: z1 = z1 - L
    if z1 < -0.5*L: z1 = z1 + L

    r=m.sqrt(x1**2 + y1**2 + z1**2)

    if r < rcut:
      iflag = 1
      break
  if iflag==0:
    i += 1
    x.append(x0)
    y.append(y0)
    z.append(z0)

# Print output file
outfile = open("aSi_1000.xyz","w")
print("{0:6d}".format(N),file=outfile)
print("{0:12.6f}".format(L),file=outfile)
for j in range(N):
   print("{0:s} {1:12.6f} {2:12.6f} {3:12.6f}".format("Si ",x[j],y[j],z[j]),file=outfile)
outfile.close()

