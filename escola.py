class Disciplina:

    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcularMedia(self):
        return (self.notas[0] + self.notas[1] + self.notas[2] + self.notas[3]) / 4

    def exibirSituacao(self):
        media = self.calcularMedia()
        if media >= 6.0:
            return 'Aprovado'
        elif media >= 3.0:
            return 'Em Recuperação'
        else:
            return 'Reprovado'