import matplotlib.pyplot as plt
import numpy as np
import math

R = [3, 8, 6, 10] # Elos estáticos
theta = [0, 60, 27, 100] # 27 e 100 sao os valores de chute para a primeira iteracao

def norm(f):
  return math.sqrt(math.pow(f[0], 2) + math.pow(f[1], 2))

def mnewton(theta):
  index = 0 
  thetaRad = [0, 0, 0, 0]

  while (index < (len(theta))):
    thetaRad[index] = math.radians(theta[index])
    index += 1

  t2 = thetaRad[1]
  t3b = thetaRad[2]
  t4b = thetaRad[3]
  eps = 1e-10 # condição de convergência

  S = R[0]
  P = R[1]
  Q = R[2]
  L = R[3]

  f = np.matrix([
    [ P*math.cos(t3b) - Q*math.cos(t4b) + S*math.cos(t2) - L ],
    [ P*math.sin(t3b) - Q*math.sin(t4b) + S*math.sin(t2) ]  
  ])

  while norm(f) > eps:
    J = np.matrix([
      [ -P*math.sin(t3b) , Q*math.cos(t4b) ],
      [ P*math.cos(t3b) , -Q*math.cos(t4b) ]
    ])
    MulM = (-1) * np.linalg.inv(J) * f
    t3b = (t3b + MulM[0])
    t4b = (t4b + MulM[1])
    f = np.matrix([
      [ P*math.cos(t3b) - Q*math.cos(t4b) + S*math.cos(t2) - L ],
      [ P*math.sin(t3b) - Q*math.sin(t4b) + S*math.sin(t2) ]  
    ])
  
  return math.degrees(t3b) % 360, math.degrees(t4b) % 360

print(mnewton(theta))
