# =============================================================
# routes.py — Rotas HTTP e template HTML do sistema Kanban
# Define todos os endpoints da aplicação e a interface visual.
# =============================================================

from flask import render_template_string, request, redirect
from src.models import Task

# Lista em memória que persiste durante a sessão do servidor.
# Em uma versão futura pode ser substituída por um banco de dados.
tarefas: list[Task] = []

# =============================================================
# Template HTML — Interface Kanban
# =============================================================

HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kanban Task Manager</title>

    <style>

        /* -------------------------------------------------- */
        /* Reset e base                                        */
        /* -------------------------------------------------- */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            min-height: 100vh;
            background: linear-gradient(
                135deg,
                #14001f,
                #2d1148,
                #4b1f73,
                #6d28d9
            );
            color: white;
            padding: 40px;
        }

        /* -------------------------------------------------- */
        /* Cabeçalho                                           */
        /* -------------------------------------------------- */

        h1 {
            text-align: center;
            margin-bottom: 35px;
            font-size: 48px;
            font-weight: 700;
            letter-spacing: 2px;
            color: #f5e9ff;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
        }

        .container {
            max-width: 1500px;
            margin: auto;
        }

        /* -------------------------------------------------- */
        /* Formulário de cadastro                              */
        /* -------------------------------------------------- */

        form {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 28px;
            padding: 25px;
            margin-bottom: 40px;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        }

        input,
        select {
            flex: 1;
            min-width: 200px;
            padding: 16px;
            border: none;
            outline: none;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.12);
            color: white;
            font-size: 15px;
            cursor: pointer;
        }

        input::placeholder {
            color: #ccc;
        }

        select option {
            background: #2d1148;
            color: white;
        }

        button {
            padding: 16px 28px;
            border: none;
            border-radius: 18px;
            background: linear-gradient(135deg, #c084fc, #9333ea);
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            font-size: 15px;
            white-space: nowrap;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 18px rgba(192, 132, 252, 0.6);
        }

        /* -------------------------------------------------- */
        /* Quadro Kanban — 3 colunas                           */
        /* -------------------------------------------------- */

        .kanban {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .column {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(14px);
            border-radius: 28px;
            padding: 22px;
            min-height: 600px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        .column h2 {
            text-align: center;
            margin-bottom: 25px;
            font-size: 26px;
            color: #f3d9ff;
        }

        /* Contador de tarefas por coluna */
        .column-count {
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 2px 10px;
            font-size: 14px;
            margin-left: 8px;
            vertical-align: middle;
        }

        /* -------------------------------------------------- */
        /* Cards de tarefa                                     */
        /* -------------------------------------------------- */

        .task {
            background: rgba(255, 255, 255, 0.10);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 22px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .task:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
        }

        .titulo {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #ffffff;
        }

        .descricao {
            color: #e9d5ff;
            margin-bottom: 14px;
            font-size: 14px;
            line-height: 1.5;
        }

        /* -------------------------------------------------- */
        /* Badge de prioridade — cor varia conforme o nível   */
        /* -------------------------------------------------- */

        .badge {
            display: inline-block;
            margin-bottom: 16px;
            padding: 5px 12px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 600;
        }

        .badge-alta {
            background: rgba(244, 63, 94, 0.25);
            border: 1px solid rgba(244, 63, 94, 0.5);
            color: #fda4af;
        }

        .badge-media {
            background: rgba(251, 191, 36, 0.25);
            border: 1px solid rgba(251, 191, 36, 0.5);
            color: #fde68a;
        }

        .badge-baixa {
            background: rgba(34, 197, 94, 0.25);
            border: 1px solid rgba(34, 197, 94, 0.5);
            color: #86efac;
        }

        /* -------------------------------------------------- */
        /* Botões de ação                                      */
        /* -------------------------------------------------- */

        .buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn {
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 14px;
            color: white;
            font-size: 13px;
            font-weight: 600;
            transition: 0.3s;
        }

        .btn-iniciar {
            background: linear-gradient(135deg, #7c3aed, #9333ea);
        }

        .btn-iniciar:hover {
            box-shadow: 0 0 14px rgba(147, 51, 234, 0.7);
            transform: translateY(-1px);
        }

        .btn-concluir {
            background: linear-gradient(135deg, #22c55e, #16a34a);
        }

        .btn-concluir:hover {
            box-shadow: 0 0 14px rgba(34, 197, 94, 0.6);
            transform: translateY(-1px);
        }

        .btn-excluir {
            background: linear-gradient(135deg, #f43f5e, #e11d48);
        }

        .btn-excluir:hover {
            box-shadow: 0 0 14px rgba(244, 63, 94, 0.6);
            transform: translateY(-1px);
        }

        /* -------------------------------------------------- */
        /* Responsivo                                          */
        /* -------------------------------------------------- */

        @media (max-width: 1100px) {
            .kanban {
                grid-template-columns: 1fr;
            }
        }

    </style>
</head>

<body>
<div class="container">

    <h1>✨ Kanban Task Manager ✨</h1>

    <!-- ---------------------------------------------------- -->
    <!-- Formulário de cadastro de nova tarefa                 -->
    <!-- ---------------------------------------------------- -->

    <form method="POST" action="/add">

        <input
            type="text"
            name="titulo"
            placeholder="Título da tarefa"
            required
        >

        <input
            type="text"
            name="descricao"
            placeholder="Descrição"
            required
        >

        <!-- Seletor de prioridade com opções fixas -->
        <select name="prioridade" required>
            <option value="" disabled selected>🎯 Prioridade</option>
            <option value="Alta">🔴 Alta</option>
            <option value="Média">🟡 Média</option>
            <option value="Baixa">🟢 Baixa</option>
        </select>

        <button type="submit">+ Adicionar Tarefa</button>

    </form>

    <!-- ---------------------------------------------------- -->
    <!-- Quadro Kanban                                          -->
    <!-- ---------------------------------------------------- -->

    <div class="kanban">

        <!-- Coluna: TO DO -->
        <div class="column">
            <h2>
                📌 To Do
                <span class="column-count">
                    {{ tarefas | selectattr('status', 'equalto', 'To Do') | list | length }}
                </span>
            </h2>

            {% for tarefa in tarefas %}
                {% if tarefa.status == "To Do" %}
                    <div class="task">

                        <div class="titulo">{{ tarefa.titulo }}</div>
                        <div class="descricao">{{ tarefa.descricao }}</div>

                        <!-- Badge com cor dinâmica conforme prioridade -->
                        {% if tarefa.prioridade == "Alta" %}
                            <span class="badge badge-alta">🔴 Alta</span>
                        {% elif tarefa.prioridade == "Média" %}
                            <span class="badge badge-media">🟡 Média</span>
                        {% else %}
                            <span class="badge badge-baixa">🟢 Baixa</span>
                        {% endif %}

                        <div class="buttons">
                            <a class="btn btn-iniciar" href="/iniciar/{{ loop.index0 }}">▶ Iniciar</a>
                            <a class="btn btn-excluir" href="/delete/{{ loop.index0 }}">🗑 Excluir</a>
                        </div>

                    </div>
                {% endif %}
            {% endfor %}
        </div>

        <!-- Coluna: IN PROGRESS -->
        <div class="column">
            <h2>
                🚀 In Progress
                <span class="column-count">
                    {{ tarefas | selectattr('status', 'equalto', 'In Progress') | list | length }}
                </span>
            </h2>

            {% for tarefa in tarefas %}
                {% if tarefa.status == "In Progress" %}
                    <div class="task">

                        <div class="titulo">{{ tarefa.titulo }}</div>
                        <div class="descricao">{{ tarefa.descricao }}</div>

                        {% if tarefa.prioridade == "Alta" %}
                            <span class="badge badge-alta">🔴 Alta</span>
                        {% elif tarefa.prioridade == "Média" %}
                            <span class="badge badge-media">🟡 Média</span>
                        {% else %}
                            <span class="badge badge-baixa">🟢 Baixa</span>
                        {% endif %}

                        <div class="buttons">
                            <a class="btn btn-concluir" href="/concluir/{{ loop.index0 }}">✅ Concluir</a>
                            <a class="btn btn-excluir"  href="/delete/{{ loop.index0 }}">🗑 Excluir</a>
                        </div>

                    </div>
                {% endif %}
            {% endfor %}
        </div>

        <!-- Coluna: DONE -->
        <div class="column">
            <h2>
                ✅ Done
                <span class="column-count">
                    {{ tarefas | selectattr('status', 'equalto', 'Done') | list | length }}
                </span>
            </h2>

            {% for tarefa in tarefas %}
                {% if tarefa.status == "Done" %}
                    <div class="task">

                        <div class="titulo">{{ tarefa.titulo }}</div>
                        <div class="descricao">{{ tarefa.descricao }}</div>

                        {% if tarefa.prioridade == "Alta" %}
                            <span class="badge badge-alta">🔴 Alta</span>
                        {% elif tarefa.prioridade == "Média" %}
                            <span class="badge badge-media">🟡 Média</span>
                        {% else %}
                            <span class="badge badge-baixa">🟢 Baixa</span>
                        {% endif %}

                        <div class="buttons">
                            <a class="btn btn-excluir" href="/delete/{{ loop.index0 }}">🗑 Excluir</a>
                        </div>

                    </div>
                {% endif %}
            {% endfor %}
        </div>

    </div><!-- /.kanban -->

</div><!-- /.container -->
</body>
</html>
"""


# =============================================================
# Registro de rotas
# =============================================================

def configure_routes(app) -> None:
    """Registra todos os endpoints HTTP no app Flask."""

    @app.route("/")
    def index():
        """Renderiza a página principal com o quadro Kanban."""
        return render_template_string(HTML, tarefas=tarefas)

    # ----------------------------------------------------------

    @app.route("/add", methods=["POST"])
    def add():
        """
        Recebe o formulário e cria uma nova tarefa na lista.
        Redireciona para a página principal após a inserção.
        """
        titulo     = request.form["titulo"]
        descricao  = request.form["descricao"]
        prioridade = request.form["prioridade"]

        nova_tarefa = Task(titulo, descricao, prioridade)
        tarefas.append(nova_tarefa)

        return redirect("/")

    # ----------------------------------------------------------

    @app.route("/iniciar/<int:id>")
    def iniciar(id: int):
        """Move a tarefa de 'To Do' para 'In Progress'."""
        tarefas[id].iniciar()
        return redirect("/")

    # ----------------------------------------------------------

    @app.route("/concluir/<int:id>")
    def concluir(id: int):
        """Move a tarefa de 'In Progress' para 'Done'."""
        tarefas[id].concluir()
        return redirect("/")

    # ----------------------------------------------------------

    @app.route("/delete/<int:id>")
    def delete(id: int):
        """Remove a tarefa da lista pelo índice."""
        tarefas.pop(id)
        return redirect("/")
