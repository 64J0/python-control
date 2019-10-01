#import numpy
#import scipy
#import slycot as slycot
import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 2, 1] #(s^2) + 2s + 1
sys = control.tf(num, den)
T, yout = control.step_response(sys)

fig, ax = plt.subplots()

ax.set(xlabel='X (x)', ylabel='Y (y)', title='Entrada degrau')

ax.grid()

plt.plot(T, yout)
# print(len(T)) # 100

plt.savefig('resultado.png')
plt.show()