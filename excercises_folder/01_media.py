nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

media = (int(nota1)+ int(nota2))/2

#Converti media em string, porque nao aceita concatenar float com string para imprimir
print("A media do aluno é de: " + str(media))