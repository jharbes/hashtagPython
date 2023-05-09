"""
Integração Python Word

Instalar biblioteca python-docx

pip install python-docx

"""

from docx import Document

# criando o documento no Python
documento = Document()

faturamento = 1000

# aqui você edita tudo o que você quer
texto = f"""Fala Lira,

O faturamento da empresa ontem foi de R${faturamento}

Tamo junto, abs.
"""

paragrafo = documento.add_paragraph(texto) 