#1.Pergunte ao usuário a nota do aluno (0 a 10)
#2.Classifique a nota em conceitos:
#•A → nota maior ou igual a 9
#•B → nota maior ou igual a 7 e menor que 9
#•C → nota maior ou igual a 5 e menor que 7
#•D → nota menor que 5
#Requisitos:
#•Utilize if, elif e else
#•Converta a entrada para número float
nota = float(input("nota da prova: "))
if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("c")
else:
    print("D")