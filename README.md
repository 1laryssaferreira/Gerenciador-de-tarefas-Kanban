# ✨ Kanban Task Manager

> Sistema web de gerenciamento de tarefas com metodologia ágil Kanban  
> Disciplina de Engenharia de Software — UniFECAF

---

## Sobre o Projeto

O **Kanban Task Manager** é um sistema web desenvolvido em Python com Flask que permite gerenciar tarefas em um quadro Kanban com três colunas: **To Do**, **In Progress** e **Done**.

O projeto foi desenvolvido para a disciplina de Engenharia de Software, simulando o ambiente de trabalho da empresa fictícia **TechFlow Solutions**, contratada por uma startup de logística para criar uma ferramenta ágil de acompanhamento de fluxo de trabalho.

---

## Funcionalidades

- ✅ Cadastrar tarefas com título, descrição e prioridade
- 📋 Visualizar quadro Kanban em tempo real
- ▶ Mover tarefa de **To Do** → **In Progress**
- ✅ Mover tarefa de **In Progress** → **Done**
- 🗑 Excluir tarefas em qualquer coluna
- 🎯 Priorizar tarefas: **Alta** 🔴 / **Média** 🟡 / **Baixa** 🟢
- 🔢 Contador de tarefas por coluna

---

## Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| Flask | latest | Framework web |
| Pytest | latest | Testes automatizados |
| GitHub Actions | — | Integração contínua (CI) |

---

## Metodologia Ágil — Kanban

O desenvolvimento seguiu a metodologia **Kanban**, com o quadro organizado em três colunas:

| Coluna | Descrição |
|---|---|
| 📌 To Do | Tarefas planejadas ainda não iniciadas |
| 🚀 In Progress | Tarefas em execução |
| ✅ Done | Tarefas concluídas |

O próprio sistema reflete o Kanban na prática: cada tarefa cadastrada segue o fluxo das colunas conforme avança no desenvolvimento.

---

## Mudança de Escopo

O escopo inicial previa apenas cadastro simples com status binário (Pendente/Concluída).

Durante o desenvolvimento foi adicionada a funcionalidade de **prioridade das tarefas** (Alta, Média, Baixa) e o fluxo foi reformulado para o modelo Kanban de três colunas.

**Justificativa:** a startup precisava diferenciar tarefas urgentes das rotineiras para alocar recursos com eficiência. O custo da mudança foi baixo por estar no início do desenvolvimento.

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/task-manager.git
cd task-manager
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o sistema

```bash
python src/app.py
```

Acesse em: **http://localhost:5000**

### 4. Executar os testes

```bash
pytest tests/ -v
```

---

## Estrutura do Projeto

```
task-manager/
│
├── src/                        # Código-fonte da aplicação
│   ├── __init__.py
│   ├── app.py                  # Ponto de entrada Flask
│   ├── models.py               # Entidade Task (domínio)
│   └── routes.py               # Rotas HTTP + template HTML
│
├── tests/                      # Testes automatizados
│   ├── __init__.py
│   └── test_app.py             # 10 testes unitários (Pytest)
│
├── docs/                       # Documentação e diagramas UML
│
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline GitHub Actions
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Testes Automatizados

10 testes unitários com Pytest cobrindo:

| Grupo | Testes |
|---|---|
| Criação de tarefa | título, descrição, prioridade, status inicial |
| Transições de estado | iniciar(), concluir(), fluxo completo |
| Prioridades | Alta, Média, Baixa |

```bash
pytest tests/ -v
```

---

## Integração Contínua

O pipeline em `.github/workflows/ci.yml` executa automaticamente a cada **push** ou **pull request** na branch `main`:

1. Checkout do repositório
2. Configuração do Python 3.11
3. Instalação das dependências
4. Execução dos testes com Pytest

---

## Histórico de Commits

O repositório mantém commits semânticos descritivos seguindo o padrão **Conventional Commits**:

```
feat: inicializa estrutura do projeto Flask
feat: implementa classe Task com status To Do
feat: adiciona rota /add para cadastro de tarefas
feat: adiciona rotas /iniciar e /concluir para fluxo Kanban
feat: implementa rota /delete para exclusão de tarefas
style: cria template HTML com layout Kanban e gradiente roxo
feat: adiciona campo de prioridade e badges coloridos
test: implementa 10 testes unitários com Pytest
ci: configura pipeline GitHub Actions
docs: atualiza README com estrutura e instruções completas
```
