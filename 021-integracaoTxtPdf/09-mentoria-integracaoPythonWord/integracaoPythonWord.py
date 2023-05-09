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




### formatação

# Pt vem de pontos que seria o tamanho da fonte
# RGBColor é das cores
# Cm é de centimetros para editar tamanho de imagem, tamanho de margem, etc
from docx.shared import Pt, RGBColor, Cm # valores de formatação

# permite criar um estilo de formatação (determina um conjunto de características para a fonte como cor, tipo de fonte, tamanho, etc)
from docx.enum.style import WD_STYLE_TYPE

paragrafo.style = documento.styles.add_style("EstiloLira", WD_STYLE_TYPE.PARAGRAPH)
paragrafo.style.font.name = "Algerian"
paragrafo.style.font.size = Pt(15)
paragrafo.style.font.bold = True
paragrafo.style.font.italic = True
paragrafo.style.font.underline = True
paragrafo.style.font.color.rgb = RGBColor(255, 0, 0)






# implementando tudo que fizemos no Python no texto.docx

documento.save('Texto.docx')