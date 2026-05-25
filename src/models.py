# =============================================================
# models.py — Entidade de domínio do sistema
# Representa uma tarefa no quadro Kanban com seus atributos
# e as transições de estado do fluxo de trabalho.
# =============================================================


class Task:
    """
    Representa uma tarefa no quadro Kanban.

    Atributos:
        titulo    (str): Nome curto da tarefa.
        descricao (str): Detalhamento do que deve ser feito.
        prioridade(str): Nível de urgência — 'Alta', 'Média' ou 'Baixa'.
        status    (str): Coluna atual no Kanban —
                         'To Do' | 'In Progress' | 'Done'.
    """

    # Status possíveis, alinhados com as colunas do quadro Kanban
    STATUS_TODO        = "To Do"
    STATUS_IN_PROGRESS = "In Progress"
    STATUS_DONE        = "Done"

    def __init__(self, titulo: str, descricao: str, prioridade: str):
        self.titulo     = titulo
        self.descricao  = descricao
        self.prioridade = prioridade
        # Toda tarefa nasce na primeira coluna do Kanban
        self.status = self.STATUS_TODO

    # ----------------------------------------------------------
    # Transições de estado
    # ----------------------------------------------------------

    def iniciar(self) -> None:
        """Move a tarefa de 'To Do' para 'In Progress'."""
        self.status = self.STATUS_IN_PROGRESS

    def concluir(self) -> None:
        """Move a tarefa de 'In Progress' para 'Done'."""
        self.status = self.STATUS_DONE

    # ----------------------------------------------------------
    # Representação textual (útil para debug)
    # ----------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"Task(titulo={self.titulo!r}, "
            f"prioridade={self.prioridade!r}, "
            f"status={self.status!r})"
        )
