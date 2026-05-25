# =============================================================
# app.py — Ponto de entrada da aplicação Flask
#
# Como executar (da raiz do projeto):
#   python src/app.py
#
# Acesse em:
#   http://localhost:5000
# =============================================================

import sys
import os

# Garante que a raiz do projeto esteja no path,
# permitindo que "from src.xxx import" funcione
# independentemente de onde o script é chamado.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from src.routes import configure_routes

# Inicializa a instância Flask
app = Flask(__name__)

# Registra todas as rotas definidas em routes.py
configure_routes(app)

if __name__ == "__main__":
    # debug=True ativa o reloader automático em desenvolvimento.
    # Nunca usar debug=True em produção.
    app.run(debug=True)
