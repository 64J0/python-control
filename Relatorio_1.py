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

# Cálculo Beta no condensador

beta = [0, 0, 0, 0, 0, 0]

aux = 0
while(aux < (len(tempo_min) -1)):
    aux += 1
    beta[aux] = (vetor_delta_entalpia_baixa[aux])/(vetor_delta_entalpia_alta[aux] - vetor_delta_entalpia_baixa[aux])

# Cálculo do Beta linha no evaporador

beta_linha = [0, 0, 0, 0, 0, 0]

aux = 0
while(aux < (len(tempo_min) - 1)):
    aux += 1
    beta_linha[aux] = (vetor_delta_entalpia_alta[aux])/(vetor_delta_entalpia_alta[aux] - vetor_delta_entalpia_baixa[aux])

# delta entalpia alta

plt.ylabel(r'$\Delta$' + 'Qh (kJ/kg)')
plt.xlabel('Tempo (minutos)')
plt.title('')
plt.grid()

plt.plot(tempo_min, vetor_delta_entalpia_alta, '*-')
plt.savefig('figuras/delta_entalpia_alta_x_tempo.png')

# tempo x pressao alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Pressão alta (MPa)')
plt.title('')
plt.grid()

plt.plot(tempo_min, pressao_alta, '*-')
plt.savefig('figuras/tempo_x_pressao_alta.png')

# tempo x entalpia alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Entalpia alta (kJ/kg)')
plt.title('')
plt.grid()

plt.plot(tempo_min, entalpia_alta, '*-')
plt.savefig('figuras/tempo_x_entalpia_alta.png')

# tempo x temperatura baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura baixa (Celsius)')
plt.title('')
plt.grid()

plt.plot(tempo_min, temperatura_baixa, '*-')
plt.savefig('figuras/tempo_x_temperatura_baixa.png')

# tempo x temperatura alta

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura alta (Celsius)')
plt.title('')
plt.grid()

plt.plot(tempo_min, temperatura_alta, '*-')
plt.savefig('figuras/tempo_x_temperatura_alta.png')

# tempo x pressao baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Pressão baixa (MPa)')
plt.title('')
plt.grid()

plt.plot(tempo_min, pressao_baixa, '*-')
plt.savefig('figuras/tempo_x_pressao_baixa.png')

# tempo x entalpia baixa

plt.cla() # clear axis
plt.clf() # clear figure

plt.ylabel(r'$\Delta$' + 'Ql (kJ/kg)')
plt.xlabel('Tempo (minutos)')
plt.title('')
plt.grid()

plt.plot(tempo_min, vetor_delta_entalpia_baixa, '*-')
plt.savefig('figuras/delta_entalpia_baixa_x_tempo.png')

# tempo x Ql

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel('Entalpia baixa (kJ/kg)')
plt.title('')
plt.grid()

plt.plot(tempo_min, entalpia_baixa, '*-')
plt.savefig('figuras/tempo_x_entalpia_baixa.png')

# tempo x Beta

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel(r'$\beta$' + '')
plt.title('')
plt.grid()

plt.plot(tempo_min, beta, '*-')
plt.savefig('figuras/tempo_x_beta.png')

# tempo x Beta_linha

plt.cla() # clear axis
plt.clf() # clear figure

plt.xlabel('Tempo (minutos)')
plt.ylabel(r'$\beta$'  + '\'')
plt.title('')
plt.grid()

plt.plot(tempo_min, beta_linha, '*-')
plt.savefig('figuras/tempo_x_beta_linha.png')