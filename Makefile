PYTHON ?= python

.PHONY: formatos verifica pacote limpa

formatos:
	$(PYTHON) scripts/gerar_formatos.py

verifica:
	$(PYTHON) scripts/verificar_vazamento.py

pacote: formatos
	$(PYTHON) scripts/empacotar.py

limpa:
	-rm -rf dist
	-rm -f produto/principal/formatos/modelo_planejamento.docx
	-rm -f produto/principal/formatos/modelo_planilha.xlsx
