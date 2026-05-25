# conftest.py — Configuração do Pytest
#
# Este arquivo adiciona a raiz do projeto ao sys.path,
# permitindo que os testes importem "from src.models import Task"
# sem precisar instalar o pacote ou configurar PYTHONPATH.

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
