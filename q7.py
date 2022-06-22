chomem = 0
cmulher = 0

for i in range(0, 56):
  nome = input("escreva seu nome")
  sexo = str(input('escreva seu sexo: '))

  if sexo == 'masculino' :
    chomem = chomem + 1 
    print(' você é homem ')

  elif sexo == 'feminino':
    cmulher = cmulher + 1
    print ('você é mulher')

print('o numero de mulheres é: {}'.format(cmulher))
print('o numero de homens é: %d' % chomem)