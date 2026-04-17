#1.Pergunte o valor da compra (em reais)
#2.Pergunte se o cliente é cliente VIP (s/n)
#3.O cliente ganha frete grátis se:
#•Compra for maior que R$ 100 OU for cliente VIP
#4.Exiba se o cliente tem direito ao frete grátis ou não
#
valor = float(input("preço: "))
s = True
n = False


if input("tem vip?: ") == True:
    print("frete gratis, a compra esta á: ", valor)
else:
    print("sem direito a desconto.", valor)
