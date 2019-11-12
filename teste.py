import matplotlib.pyplot as plt

# dados coletados no experimento:

tempo_min = [0, 4, 8, 12, 16, 20]
temperatura_baixa = [22, 17, 11.5, 6.4, 5.4, 5]
pressao_baixa = [0.268, 0.243, 0.258, 0.258, 0.268, 0.798]
temperatura_alta = [22, 25.3, 30.2, 34.2, 37.5, 39.9]
pressao_alta = [0.723, 0.798, 0.898, 0.968, 1.048, 1.088]
entalpia_alta = [230.3, 235, 242, 247.8, 252.7, 256.2]
entalpia_baixa = [418.7, 414.8, 409.7, 405.2, 404.1, 206.8]

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
plt.savefig('figuras/delta_entalpia_alta_x_tempo.png')