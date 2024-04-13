# /meu-projeto-flask/app/models/__init__.py

# Este arquivo é necessário para tornar o diretório `models` um pacote Python.
# Aqui você pode importar as classes do módulo `entities` para facilitar o acesso a elas.

from .entities import Entity1, Entity2, Entity3

__all__ = ['Entity1', 'Entity2', 'Entity3']

# Este arquivo está intencionalmente em branco.