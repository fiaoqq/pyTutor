"""Valida a base de conhecimento em data/. Sem LLM, sem dependências.

Rode com: python src/verificar_base.py
"""

import glob
import json
import os

PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    arquivos = sorted(glob.glob(os.path.join(PASTA_RAIZ, "data", "*.json")))
    assert arquivos, "nenhum arquivo JSON encontrado em data/"

    total = 0
    for caminho in arquivos:
        with open(caminho, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)  # quebra aqui se o JSON for inválido
        topicos = dados.get("topicos", [])
        assert topicos, f"{caminho}: nenhum tópico encontrado"
        for topico in topicos:
            faltando = [c for c in ("id", "titulo", "explicacao") if not topico.get(c)]
            assert not faltando, f"{caminho}: tópico com campos faltando {faltando}: {topico}"
        total += len(topicos)
        nome = os.path.basename(caminho)
        print(f"OK  {nome}: {len(topicos)} tópico(s)")

    print(f"\nBase válida: {len(arquivos)} arquivo(s), {total} tópico(s) no total.")


main()
