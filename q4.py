nome = str ( input('escreva o nome do aluno: '))
n1 = float(input('digite a primeira nota : '))
n2 = float (input('digite a segunda nota : '))
n3 = float (input('digite a segunda nota : '))
media = (n1+n2+n3) /3

print (' a média do aluno é: {}'.format(media))

if media >= 7:
    print (' você está aprovado ')

if media <= 5:
    print(' você está reprovado ')

else :
   print (' você está de recuperação ')