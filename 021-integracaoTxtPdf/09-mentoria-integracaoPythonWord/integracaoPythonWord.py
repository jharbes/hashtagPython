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

# Criamos um estilo para ser utilizado (conjunto de caracteristicas do texto)
# 'EstiloLira' é o nome do estilo que está sendo criado
paragrafo.style = documento.styles.add_style("EstiloLira", WD_STYLE_TYPE.PARAGRAPH)

paragrafo.style.font.name = "Algerian" # nome da fonte como está no word
paragrafo.style.font.size = Pt(15) # tamanho da fonte no padrao do word
paragrafo.style.font.bold = True # negrito ligado
paragrafo.style.font.italic = True # italico ligado
paragrafo.style.font.underline = True # sublinhado ligado
paragrafo.style.font.color.rgb = RGBColor(255, 0, 0) # cor escolhida






# implementando tudo que fizemos no Python no texto.docx

documento.save('Texto.docx')