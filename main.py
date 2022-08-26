from function import criar_matriz_curso

curso_titulo = input('Qual o título do curso? ')
curso_descricao = input('Descreva o curso: ')
curso_professor = input('Qual o nome do professor? ')
topico_1 = input('Qual o título do tópico 1? ')
data_1 = input('Qual a data que você irá abordar o tópico 1? ')
topico_2 = input('Qual o título do tópico 2? ')
data_2 = input('Qual a data que você irá abordar o tópico 2? ')
topico_3 = input('Qual o título do tópico 3? ')
data_3 = input('Qual a data que você irá abordar o tópico 3? ')
topico_4 = input('Qual o título do tópico 4? ')
data_4 = input('Qual a data que você irá abordar o tópico 4? ')
topico_5 = input('Qual o título do tópico 5? ')
data_5 = input('Qual a data que você irá abordar o tópico 5? ')
arquivo_nome = input('Que nome quer dar para o arquivo a ser gerado? ')

criar_matriz_curso(
    curso_titulo,
    curso_descricao,
    curso_professor,
    topico_1,
    topico_2,
    topico_3,
    topico_4,
    topico_5,
    data_1,
    data_2,
    data_3,
    data_4,
    data_5,
    arquivo_nome
)
