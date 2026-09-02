#!/usr/bin/env python3
"""Roda a verificacao de vazamento e gera os zips de distribuicao em dist/.

- dist/horatividade-principal-vX.Y.Z.zip  <- produto/principal/
- dist/horatividade-bump-vX.Y.Z.zip       <- produto/bump/
Versao lida do CHANGELOG.md (primeiro cabecalho [X.Y.Z]).
Nunca inclui contexto/, demo/, producao/ nem scripts/.
Uso: python scripts/empacotar.py
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIST = RAIZ / "dist"
EXCLUIR_NOMES = {"__pycache__", ".DS_Store", "Thumbs.db"}


def versao() -> str:
    changelog = RAIZ / "CHANGELOG.md"
    if not changelog.exists():
        print("ERRO: CHANGELOG.md nao encontrado")
        sys.exit(2)
    m = re.search(r"\[(\d+\.\d+\.\d+)\]", changelog.read_text(encoding="utf-8"))
    if not m:
        print("ERRO: nenhuma versao [X.Y.Z] no CHANGELOG.md")
        sys.exit(2)
    return m.group(1)


def verificar():
    print("== verificacao de vazamento ==")
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "verificar_vazamento.py")])
    if r.returncode != 0:
        print("ERRO: verificacao de vazamento falhou; pacote nao gerado")
        sys.exit(1)


def zipar(origem: Path, destino: Path):
    arquivos = [
        p for p in sorted(origem.rglob("*"))
        if p.is_file()
        and p.name not in EXCLUIR_NOMES
        and not p.name.startswith("~$")
        and not p.suffix.lower() in {".tmp", ".bak"}
    ]
    if not arquivos:
        print(f"ERRO: nada para empacotar em {origem}")
        sys.exit(1)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for p in arquivos:
            z.write(p, p.relative_to(origem.parent))
    print(f"gerado: {destino.relative_to(RAIZ)} ({len(arquivos)} arquivos, {destino.stat().st_size // 1024} KB)")


def main():
    v = versao()
    print(f"versao: {v}")
    verificar()
    DIST.mkdir(exist_ok=True)
    zipar(RAIZ / "produto" / "principal", DIST / f"horatividade-principal-v{v}.zip")
    zipar(RAIZ / "produto" / "bump", DIST / f"horatividade-bump-v{v}.zip")
    print("ok: pacotes gerados em dist/")


if __name__ == "__main__":
    main()
