import matplotlib.pyplot as plt

# dados coletados no experimento:

tempo_min = [0, 4, 8, 12, 16, 20]
temperatura_baixa = [22, 17, 11.5, 6.4, 5.4, 5]
pressao_baixa = [0.17, 0.145, 0.16, 0.16, 0.17, 0.7]
temperatura_alta = [22, 25.3, 30.2, 34.2, 37.5, 39.9]
pressao_alta = [0.625, 0.7, 0.8, 0.87, 0.95, 0.99]
entalpia_alta = [92.9, 106.8, 127.3, 145.3, 157.9, 168]
entalpia_baixa = [92.47, 71.51, 48.45, 27.02, 22.83, 21.67]

# cálculo das variações

vetor_delta_entalpia_alta = [0, 0, 0, 0, 0, 0]
vetor_delta_entalpia_baixa = [0, 0, 0, 0, 0, 0]

# Qh

aux = 0
while(aux < (len(tempo_min) - 1)):
    aux += 1
    vetor_delta_entalpia_alta[aux] = entalpia_alta[aux] - entalpia_alta[0]

# Ql

aux = 0
while(aux < (len(tempo_min) - 1)):
    aux += 1
    vetor_delta_entalpia_baixa[aux] = entalpia_baixa[aux] - entalpia_baixa[0]

# delta entalpia alta

plt.ylabel(r'$\Delta$' + 'Qh (kJ/kg)')
plt.xlabel('Tempo (minutos)')
plt.title('')
plt.grid()

plt.plot(tempo_min, vetor_delta_entalpia_alta, '*-')
plt.savefig('delta_entalpia_alta_x_tempo.png')

# tempo x pressao alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Pressão alta (MPa)')
plt.title('')
plt.grid()

plt.plot(pressao_alta, tempo_min, '*-')
plt.savefig('tempo_x_pressao_alta.png')

# tempo x entalpia alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Entalpia alta (kJ/kg)')
plt.title('')
plt.grid()

plt.plot(entalpia_alta, tempo_min, '*-')
plt.savefig('tempo_x_entalpia_alta.png')

# tempo x temperatura baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Temperatura baixa (Celsius)')
plt.title('')
plt.grid()

plt.plot(temperatura_baixa, tempo_min, '*-')
plt.savefig('tempo_x_temperatura_baixa.png')

# tempo x temperatura alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Temperatura alta (Celsius)')
plt.title('')
plt.grid()

plt.plot(temperatura_alta, tempo_min, '*-')
plt.savefig('tempo_x_temperatura_alta.png')

# tempo x pressao baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Pressão baixa (MPa)')
plt.title('')
plt.grid()

plt.plot(pressao_baixa, tempo_min, '*-')
plt.savefig('tempo_x_pressao_baixa.png')

# tempo x entalpia baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel(r'$\Delta$' + 'Ql (kJ/kg)')
plt.xlabel('Tempo (minutos)')
plt.title('')
plt.grid()

plt.plot(tempo_min, vetor_delta_entalpia_baixa, '*-')
plt.savefig('delta_entalpia_baixa_x_tempo.png')

# tempo x Ql

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel('Tempo (minutos)')
plt.xlabel('Entalpia baixa (kJ/kg)')
plt.title('')
plt.grid()

plt.plot(entalpia_baixa, tempo_min, '*-')
plt.savefig('tempo_x_entalpia_baixa.png')