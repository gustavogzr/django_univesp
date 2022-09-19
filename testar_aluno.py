from website.models import AlunoUnivesp

# Inserindo um aluno
aluno = AlunoUnivesp(
    nome='Fulano',
    sobrenome='de Tal',
    matricula='123.456-78')
aluno.save()

# Buscar todos os alunos
AlunoUnivesp.objetos.all()

# Buscar com filtros
alunos = AlunoUnivesp.objetos
    .exclude(nome='Fulano')
    .filter(matricula_gt=123)
    .all()

# Excluir um aluno
aluno = AlunoUnivesp.objetos
    .filter(nome='Fulano')
    .first()
aluno.delete()
