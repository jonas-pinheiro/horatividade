#!/usr/bin/env python3
"""Varre tudo que sera empacotado (produto/) procurando termos proibidos e padroes de risco.

Termos: contexto/termos_proibidos.txt (um por linha, case-insensitive, sem acento).
Padroes de risco: e-mail, CPF, telefone, CEP e codigos de habilidade com cara de inventados.
Falha (exit != 0) se encontrar qualquer coisa.
Uso: python scripts/verificar_vazamento.py
"""
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ALVO = RAIZ / "produto"
EXTENSOES_TEXTO = {".md", ".txt", ".yaml", ".yml", ".csv"}

PADROES_RISCO = [
    ("e-mail", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("CPF", re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")),
    ("telefone", re.compile(r"\(\d{2}\)\s?9?\d{4}[- ]\d{4}")),
    ("CEP", re.compile(r"\b\d{5}-\d{3}\b")),
    ("codigo de habilidade (conferir se e inventado)", re.compile(r"\b(?:EF|EM|EI)\d{2}[A-Z]{1,4}\d{2,3}\b")),
]


def sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def carregar_termos():
    candidatos = [RAIZ / "contexto" / "termos_proibidos.txt", RAIZ / "CONTEXTO" / "termos_proibidos.txt"]
    for c in candidatos:
        if c.exists():
            linhas = [l.strip() for l in c.read_text(encoding="utf-8").splitlines()]
            return [sem_acento(l).lower() for l in linhas if l and not l.startswith("#")]
    print(f"ERRO: termos_proibidos.txt nao encontrado em {candidatos[0].parent} nem em {candidatos[1].parent}")
    sys.exit(2)


def main():
    if not ALVO.exists():
        print(f"ERRO: pasta alvo nao existe: {ALVO}")
        sys.exit(2)

    termos = carregar_termos()
    achados = []
    arquivos = sorted(p for p in ALVO.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSOES_TEXTO)

    for arq in arquivos:
        texto = arq.read_text(encoding="utf-8", errors="replace")
        normalizado = sem_acento(texto).lower()
        rel = arq.relative_to(RAIZ)

        for termo in termos:
            if len(termo) <= 4:
                padrao = re.compile(r"\b" + re.escape(termo) + r"\b")
                ocorre = bool(padrao.search(normalizado))
            else:
                ocorre = termo in normalizado
            if ocorre:
                achados.append(f"{rel}: termo proibido '{termo}'")

        for nome, padrao in PADROES_RISCO:
            for m in padrao.finditer(texto):
                achados.append(f"{rel}: padrao de risco [{nome}]: '{m.group(0)}'")

    print(f"verificados {len(arquivos)} arquivos em {ALVO.relative_to(RAIZ)}/")
    if achados:
        print(f"\nFALHOU — {len(achados)} ocorrencia(s):")
        for a in achados:
            print(f"  - {a}")
        sys.exit(1)
    print("ok: nenhum vazamento encontrado")


if __name__ == "__main__":
    main()
