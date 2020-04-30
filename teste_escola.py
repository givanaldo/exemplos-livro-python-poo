from escola import Disciplina

mat = Disciplina('Matemática', [6.7, 7.0, 8.4, 9.5])
print('Disciplina: %s' % mat.nome)
print('Média: %.1f' % mat.calcularMedia(), end='  ')
print('Situação: %s' % mat.exibirSituacao())

port = Disciplina('Português', [6.7, 3.0, 2.4, 5.2])
print('\nDisciplina: %s' % port.nome)
print('Média: %.1f' % port.calcularMedia(), end='  ')
print('Situação: %s' % port.exibirSituacao())

bio = Disciplina('Biologia', [0.5, 3.0, 2.4, 2.2])
print('\nDisciplina: %s' % bio.nome)
print('Média: %.1f' % bio.calcularMedia(), end='  ')
print('Situação: %s' % bio.exibirSituacao())