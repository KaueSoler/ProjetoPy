# calculator/__init__.py

# Aqui você pode importar os principais componentes do pacote
from .model import CalculatorModel
from .service import CalculatorService
from .view import CalculatorView
from .controller import CalculatorController

# Define o que deve ser exposto quando alguém importa * de calculator
__all__ = ['CalculatorModel', 'CalculatorService', 'CalculatorView', 'CalculatorController']
