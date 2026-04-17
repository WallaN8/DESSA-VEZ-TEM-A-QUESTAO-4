#Criar sistema de velocimetro
# V > 80 = multa
#V < 80 = permitido
#
V = int(input("Velocidade do veiculo: "))
L = int(input("Velocidade limite: "))
if V > L:
    print("multado por quebrar limites de velocidade")

else:
    print("Limite não ultrapassado")
