import matplotlib.pyplot as plt
import numpy as np
import math

L1      = 1
L2      = 2
angles  = np.arange(0, 360, 0.1) # 0 to 360, step = 0.1

def calculateTheta3(theta2):
  theta2Radian = math.radians(theta2)
  result = math.pow((L1/L2), 2)
  result = result * math.pow( math.sin(theta2Radian), 2 )
  result = 1 - result
  result = math.sqrt(result)
  result = math.acos(result)
  return result # radians

def calculateB(theta2):
  theta3Radians = calculateTheta3(theta2)  # radians
  theta2Radians = math.radians(theta2)     # radians
  result = L1 * math.cos(theta2Radians) + L2 * math.cos(theta3Radians)
  return result

b = []
for angleDeg in angles:
  bResult = calculateB(angleDeg)
  b.append(bResult)

plt.xlabel(r'$\Theta$' + '2 (graus)')
plt.ylabel('Posição de b (m)')
plt.title('Cinemática - 2. c)')
plt.grid()

plt.plot(angles, b)
plt.savefig('dois_c.png')