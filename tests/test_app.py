# =============================================================
# test_app.py — Testes automatizados do Kanban Task Manager
#
# Como executar:
#   pytest tests/ -v
#
# Cobertura:
#   - Criação de tarefa (título, descrição, prioridade)
#   - Status inicial correto ("To Do")
#   - Transições de estado: iniciar() e concluir()
#   - Fluxo Kanban completo: To Do → In Progress → Done
#   - Validação das três prioridades
# =============================================================

from src.models import Task


# =============================================================
# Grupo 1 — Criação de tarefa
# =============================================================

def test_criacao_titulo():
    """O título informado deve ser armazenado corretamente."""
    tarefa = Task("Estudar Flask", "Aprender rotas e templates", "Alta")
    assert tarefa.titulo == "Estudar Flask"


def test_criacao_descricao():
    """A descrição informada deve ser armazenada corretamente."""
    tarefa = Task("Estudar Flask", "Aprender rotas e templates", "Alta")
    assert tarefa.descricao == "Aprender rotas e templates"


def test_criacao_prioridade():
    """A prioridade informada deve ser armazenada corretamente."""
    tarefa = Task("Estudar Flask", "Aprender rotas e templates", "Alta")
    assert tarefa.prioridade == "Alta"


def test_status_inicial_to_do():
    """Toda tarefa recém-criada deve começar com status 'To Do'."""
    tarefa = Task("Nova Tarefa", "Descrição qualquer", "Baixa")
    assert tarefa.status == "To Do"


# =============================================================
# Grupo 2 — Transições de estado (fluxo Kanban)
# =============================================================

def test_iniciar_tarefa():
    """iniciar() deve mover a tarefa para 'In Progress'."""
    tarefa = Task("Implementar rotas", "Criar endpoints Flask", "Alta")
    tarefa.iniciar()
    assert tarefa.status == "In Progress"


def test_concluir_tarefa():
    """concluir() deve mover a tarefa para 'Done'."""
    tarefa = Task("Projeto", "Finalizar projeto", "Média")
    tarefa.concluir()
    assert tarefa.status == "Done"


def test_fluxo_completo_kanban():
    """A tarefa deve percorrer as três colunas na ordem correta."""
    tarefa = Task("Tarefa Completa", "Percorrer todas as colunas", "Alta")

    # Estado inicial
    assert tarefa.status == "To Do"

    # Primeira transição
    tarefa.iniciar()
    assert tarefa.status == "In Progress"

    # Segunda transição
    tarefa.concluir()
    assert tarefa.status == "Done"


# =============================================================
# Grupo 3 — Prioridades
# =============================================================

def test_prioridade_alta():
    """Deve aceitar e armazenar a prioridade 'Alta'."""
    tarefa = Task("Urgente", "Resolver bug crítico", "Alta")
    assert tarefa.prioridade == "Alta"


def test_prioridade_media():
    """Deve aceitar e armazenar a prioridade 'Média'."""
    tarefa = Task("Melhoria", "Refatorar código", "Média")
    assert tarefa.prioridade == "Média"


def test_prioridade_baixa():
    """Deve aceitar e armazenar a prioridade 'Baixa'."""
    tarefa = Task("Documentação", "Atualizar README", "Baixa")
    assert tarefa.prioridade == "Baixa"
