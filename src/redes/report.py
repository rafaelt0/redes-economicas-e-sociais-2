"""Etapa `report`: macros e tabelas LaTeX a partir de `resultados/` e o PDF do relatório (T19).

`numeros.tex` não é versionado: é função determinística de `results/tables` (já versionado) e
gravá-lo no repositório duplicaria a fonte e geraria conflito quando as etapas de estimação
mudarem as tabelas. Ele nasce no diretório de compilação, `<dados>/build/report`, ao lado de uma
cópia das fontes e das figuras, e só o PDF final vai para `saida`.
"""

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import polars as pl

from redes.amostra import MARCADOR
from redes.config import RAIZ, Caminhos
from redes.etapas import Contexto, Etapa
from redes.numeros import (
    ND,
    Numeros,
    decimal,
    escrever_macros,
    finito,
    juntar_lista,
    leitura_h2_comparaveis,
    status_comparavel_h2,
)

ETAPA = Etapa(
    nome="report",
    depende=("estimate",),
    le=(),
    grava=(),
    artefatos=("saida/relatorio.pdf",),
)

FONTES = RAIZ / "report"
MAXIMO_PAGINAS = 5


# O quadro apresenta os contrastes. As linhas por categoria guardam as bandas e o IC do rdrobust.
CONTRASTES = (
    ("H1", "conectada_menos_sem_conexao", "participacao_2025", "H1"),
    *(
        ("H2", f"vencedor_faixa_{d}", "participacao_2025", f"H2 ($\\delta={d}$)")
        for d in ("0", "1", "2", "3+")
    ),
    *(
        ("H3", "ambos_menos_demais", r, f"H3 ({nome})")
        for r, nome in (
            ("variacao_total", "total"),
            ("termo_r1", "R1"),
            ("termo_r2", "R2"),
            ("termo_r3", "R3"),
        )
    ),
    *(
        ("H4", f"ligada_ao_vencedor_{p}", f"mantem_posicao_{p}", rf"H4 ({p}\%)")
        for p in (25, 50, 75)
    ),
)


def _indexar(tabela: pl.DataFrame) -> dict:
    return {
        (r.get("hipotese"), r.get("categoria"), r.get("resultado"), r.get("tipo")): r
        for r in tabela.iter_rows(named=True)
    }


def _numero(linha: dict, coluna: str, casas: int = 4) -> str:
    valor = finito(linha.get(coluna))
    return ND if valor is None else decimal(valor, casas)


def _intervalo(linha: dict, sufixo: str = "") -> str:
    inferior = _numero(linha, "ic_inf" + sufixo)
    superior = _numero(linha, "ic_sup" + sufixo)
    return ND if ND in (inferior, superior) else f"[{inferior}, {superior}]"


def _quadro(
    rotulo: str, titulo: str, cabecalho: tuple[str, ...], corpo: list[list[str]], fonte: str
) -> str:
    return "\n".join(
        [
            r"\par\medskip\noindent\begin{minipage}{\linewidth}\centering",
            rf"\legendaquadro{{{rotulo}}}{{{titulo}}}",
            r"\footnotesize\setlength{\tabcolsep}{3.2pt}",
            r"\sbox{\caixaquadro}{%",
            rf"\begin{{tabular}}{{l{'c' * (len(cabecalho) - 1)}}}",
            r"\toprule",
            " & ".join(cabecalho) + r" \\",
            r"\midrule",
            *(" & ".join(linha) + r" \\" for linha in corpo),
            r"\bottomrule",
            r"\end{tabular}}",
            r"\ifdim\wd\caixaquadro>\linewidth",
            r"\resizebox{\linewidth}{!}{\usebox{\caixaquadro}}",
            r"\else\usebox{\caixaquadro}\fi",
            rf"\fonteabnt{{{fonte}}}",
            r"\end{minipage}\par\medskip",
        ]
    )


def tabela_estimativas(resumo: pl.DataFrame) -> str:
    """Contrastes principais e complementares, com os diagnósticos do estimador."""
    linhas = _indexar(resumo)
    corpo = []
    for h, c, r, rotulo in CONTRASTES:
        linha = linhas.get((h, c, r, "contraste"), {})
        corpo.append(
            [
                rotulo,
                _numero(linha, "estimativa"),
                _intervalo(linha),
                _numero(linha, "estimativa_meia_banda"),
                _numero(linha, "estimativa_dobro_banda"),
                _numero(linha, "placebo_estimativa"),
                _numero(linha, "placebo_p_valor", 3),
                _numero(linha, "emd"),
                _numero(linha, "p_holm", 3) if h == "H4" else "---",
            ]
        )
    densidade = _numero(resumo.row(0, named=True), "densidade_p_valor", 3) if resumo.height else ND
    densidade_fmt = f"$p={densidade.replace(',', '{,}')}$" if densidade != ND else densidade
    return _quadro(
        "tab:estimativas",
        "Contrastes no corte eleitoral",
        ("Hipótese", "Efeito", "IC", "$b/2$", "$2b$", "Placebo", "$p_{pl}$", "EMD", "$p_{Holm}$"),
        corpo,
        rf"Escala decimal: fração do empenho de 2025 (H1--H2), variação normalizada (H3) e "
        rf"permanência (H4). Em H3, o placebo usa a participação pré-eleitoral da rede e "
        rf"repete-se no total e em R1--R3. IC por reamostragem de municípios; densidade "
        rf"({densidade_fmt}). EMD: efeito mínimo detectável. Holm corrige contrastes de H4 e "
        "categorias de H1, H2 e H4.",
    )


def tabela_categorias(resumo: pl.DataFrame) -> str:
    """ICs corrigidos pelo viés, bandas e suporte dos recortes discutidos no texto."""
    linhas = _indexar(resumo)
    recortes = (
        (
            "H1",
            "participacao_2025",
            ("conectada_incumbente", "sem_conexao"),
            ("H1 · incumbente direta", "H1 · sem conexão"),
        ),
        (
            "H2",
            "participacao_2025",
            ("faixa_a_0", "faixa_b_0", "faixa_a_1", "faixa_b_1"),
            ("H2 · A direta", "H2 · B direta", "H2 · A a um passo", "H2 · B a um passo"),
        ),
        ("H3", "variacao_total", ("ambos", "demais"), ("H3 · ambos", "H3 · demais")),
        ("H3", "termo_r1", ("ambos",), ("H3 · R1 em ambos",)),
        ("H3", "termo_compensacao", ("ambos",), ("H3 · R2+R3 em ambos",)),
        (
            "H4",
            "mantem_posicao_50",
            tuple(f"ligada_{g}_50" for g in ("a", "b", "ambos", "nenhum")),
            (
                r"H4 (50\%) · só A",
                r"H4 (50\%) · só B",
                r"H4 (50\%) · ambos",
                r"H4 (50\%) · nenhuma",
            ),
        ),
    )
    corpo = []
    for h, resultado, categorias, rotulos in recortes:
        for categoria, rotulo in zip(categorias, rotulos, strict=True):
            linha = linhas.get((h, categoria, resultado, "categoria"), {})
            corpo.append(
                [
                    rotulo,
                    _numero(linha, "estimativa"),
                    _intervalo(linha),
                    _numero(linha, "banda", 1),
                    _numero(linha, "municipios_tratados", 0),
                    _numero(linha, "municipios_controle", 0),
                    _numero(linha, "p_valor", 3),
                    _numero(linha, "p_valor_rede", 3),
                ]
            )
    return _quadro(
        "tab:categorias",
        "Estimativas em categorias pré-eleitorais",
        ("Categoria", "Efeito", "IC robusto", "$b$", "Esq.", "Dir.", "$p_{{mun}}$", "$p_{{rede}}$"),
        corpo,
        r"Mesmas escalas decimais do Quadro~\ref{tab:estimativas}; IC corrigido pelo viés e "
        "valores-p sem correção de Holm. "
        "Bandas em p.p. Esq./Dir. contam municípios por lado; "
        "o valor-p por rede exige ao menos dez redes por lado.",
    )


def _marca_intervalo(linha: dict, variante: str) -> str:
    return "*" if _sinal_intervalo(linha, f"_{variante}") in ("positivo", "negativo") else ""


def tabela_robustez(robustez: pl.DataFrame) -> str:
    linhas = _indexar(robustez)
    corpo = [
        [
            rotulo,
            *(
                _numero(linha, f"estimativa_{v}") + _marca_intervalo(linha, v)
                for v in ("principal", "sem_articulacao", "sem_pj", "sem_administrador")
            ),
        ]
        for h, c, r, rotulo in CONTRASTES
        if h != "H4"
        for linha in [linhas.get((h, c, r, "contraste"), {})]
    ]
    return _quadro(
        "tab:robustez",
        "Contrastes nas quatro versões da rede",
        ("Hipótese", "Principal", "Sem articulação", "Sem sócios PJ", "Sem administradores"),
        corpo,
        r"Mesmas escalas decimais do Quadro~\ref{tab:estimativas}. "
        "Um asterisco indica IC que exclui zero.",
    )


def _sinal_intervalo(linha: dict, sufixo: str = "") -> str:
    estimativa = finito(linha.get(f"estimativa{sufixo}"))
    inferior = finito(linha.get(f"ic_inf{sufixo}"))
    superior = finito(linha.get(f"ic_sup{sufixo}"))
    if estimativa is None or inferior is None or superior is None or inferior > superior:
        return "indefinido"
    if inferior > 0:
        return "positivo"
    if superior < 0:
        return "negativo"
    return "cruza_zero"


def _estado_compensacao_h3(linhas: dict, sufixo: str = "") -> str:
    """Classifica a compensação em H3 (redes ligadas a ambos) exigindo ambos os extremos do IC."""
    s_r1 = _sinal_intervalo(linhas.get(("H3", "ambos", "termo_r1", "categoria"), {}), sufixo)
    s_comp = _sinal_intervalo(
        linhas.get(("H3", "ambos", "termo_compensacao", "categoria"), {}), sufixo
    )
    if "indefinido" in (s_r1, s_comp):
        return "indefinido"
    if s_r1 == "negativo" and s_comp == "positivo":
        return "compensacao"
    return "sem_compensacao"


def _status_comparavel_h2(h2_comparaveis: pl.DataFrame | None, faixa: str) -> str | None:
    if h2_comparaveis is None or h2_comparaveis.is_empty():
        return None
    return status_comparavel_h2(h2_comparaveis.iter_rows(named=True), faixa)


def leitura_h2_comparaveis_escala(h2_comparaveis: pl.DataFrame | None) -> str:
    """Contextualiza o contraste comparável na faixa 3+ pelo seu próprio placebo."""
    if h2_comparaveis is None or h2_comparaveis.is_empty():
        return ""
    atual = placebo = None
    for linha in h2_comparaveis.iter_rows(named=True):
        if linha.get("tipo") == "contraste" and linha.get("categoria") == "vencedor_faixa_3+":
            if linha.get("placebo"):
                placebo = linha
            else:
                atual = linha
    if not atual or not atual.get("estimavel"):
        return ""
    est = finito(atual.get("estimativa"))
    if est is None or _sinal_intervalo(atual) not in ("positivo", "negativo"):
        return ""
    if not placebo or not placebo.get("estimavel"):
        return ""
    est_pl_num = finito(placebo.get("estimativa"))
    if est_pl_num is None:
        return ""
    est_pl = decimal(100 * est_pl_num, 3)
    p_val = finito(placebo.get("p_valor"))
    p_pl = f" ($p={decimal(p_val, 3).replace(',', '{,}')}$)" if p_val is not None else ""
    return f" Nesse mesmo recorte, o placebo pré-eleitoral é de {est_pl} p.p.{p_pl}."


def leitura_resultados(resumo: pl.DataFrame, h2_comparaveis: pl.DataFrame | None = None) -> str:
    linhas = _indexar(resumo)
    grupos: dict[str, list[str]] = {
        "cruza_zero": [],
        "negativo": [],
        "positivo": [],
        "indefinido": [],
    }
    recortes_principais = {
        "H1": ("conectada_menos_sem_conexao",),
        "H2": ("vencedor_faixa_0", "vencedor_faixa_1"),
        "H3": ("variacao_total",),
    }
    for h, c, r, rotulo in CONTRASTES:
        if h not in recortes_principais:
            continue
        if c not in recortes_principais[h] and r not in recortes_principais[h]:
            continue
        sinal = _sinal_intervalo(linhas.get((h, c, r, "contraste"), {}))
        grupos[sinal].append(rotulo)

    status_h2_1 = (
        _status_comparavel_h2(h2_comparaveis, "1")
        if grupos["negativo"] == [r"H2 ($\delta=1$)"]
        else None
    )
    h2_1_sem_comp = status_h2_1 in ("sem_suporte", "sem_estimativa")

    clausulas: list[tuple[str, str]] = []
    if grupos["cruza_zero"]:
        rotulos = grupos["cruza_zero"]
        verbo = (
            "tem intervalo que inclui zero"
            if len(rotulos) == 1
            else "têm intervalos que incluem zero"
        )
        clausulas.append(("cruza_zero", f"{juntar_lista(rotulos)} {verbo}"))
    if grupos["negativo"]:
        rotulos = grupos["negativo"]
        if status_h2_1 == "sem_suporte":
            clausulas.append(
                (
                    "negativo",
                    r"apenas H2 ($\delta=1$) tem intervalo inteiramente abaixo de zero, "
                    "mas sem suporte no recorte comparável",
                )
            )
        elif status_h2_1 == "sem_estimativa":
            clausulas.append(
                (
                    "negativo",
                    r"apenas H2 ($\delta=1$) tem intervalo inteiramente abaixo de zero, "
                    "mas sem estimativa no recorte comparável",
                )
            )
        else:
            verbo = (
                "tem intervalo abaixo de zero"
                if len(rotulos) == 1
                else "têm intervalos abaixo de zero"
            )
            clausulas.append(("negativo", f"{juntar_lista(rotulos)} {verbo}"))
    if grupos["positivo"]:
        rotulos = grupos["positivo"]
        verbo = (
            "tem intervalo acima de zero" if len(rotulos) == 1 else "têm intervalos acima de zero"
        )
        clausulas.append(("positivo", f"{juntar_lista(rotulos)} {verbo}"))
    if grupos["indefinido"]:
        rotulos = grupos["indefinido"]
        verbo = "não foi estimável" if len(rotulos) == 1 else "não foram estimáveis"
        clausulas.append(("indefinido", f"{juntar_lista(rotulos)} {verbo}"))

    prefixo = (
        r"Nos contrastes principais (Quadros~\ref{tab:estimativas} e~\ref{tab:categorias}; "
        r"Figura~\ref{fig:rdd}), "
    )
    achados: list[str] = []
    if len(clausulas) == 2 and clausulas[0][0] == "cruza_zero" and h2_1_sem_comp:
        achados.append(f"{prefixo}{clausulas[0][1]}; {clausulas[1][1]}.")
    elif (
        len(clausulas) == 2
        and clausulas[0][0] == "cruza_zero"
        and clausulas[1][0] in ("negativo", "positivo")
    ):
        achados.append(f"{prefixo}{clausulas[0][1]}, enquanto {clausulas[1][1]}.")
    elif clausulas:
        achados.append(prefixo + "; ".join(texto for _, texto in clausulas) + ".")

    h4 = linhas.get(("H4", "ligada_ao_vencedor_50", "mantem_posicao_50", "contraste"), {})
    sinal_h4 = _sinal_intervalo(h4)
    p_holm_h4 = finito(h4.get("p_holm"))
    if sinal_h4 == "indefinido":
        trecho_h4 = r"Em H4 (50\%), o contraste não foi estimável"
    elif p_holm_h4 is None:
        trecho_h4 = r"Em H4 (50\%), o valor-p ajustado por Holm ficou indisponível"
    elif p_holm_h4 >= 0.05:
        trecho_h4 = r"Em H4 (50\%), o contraste é inconclusivo após Holm"
    elif sinal_h4 == "positivo":
        trecho_h4 = r"Em H4 (50\%), o contraste é positivo após Holm"
    elif sinal_h4 == "negativo":
        trecho_h4 = r"Em H4 (50\%), o contraste é negativo após Holm"
    else:
        trecho_h4 = r"Em H4 (50\%), o intervalo inclui zero"

    estado_h3 = _estado_compensacao_h3(linhas)
    if estado_h3 == "indefinido":
        trecho_h3 = "em redes ligadas a ambos os grupos, a compensação ficou sem estimativa"
    elif estado_h3 == "compensacao":
        trecho_h3 = "em redes ligadas a ambos os grupos, R1 cai e R2+R3 cresce (compensação)"
    else:
        trecho_h3 = "em redes ligadas a ambos os grupos, R1 e R2+R3 não confirmam compensação"
    achados.append(f"{trecho_h4}; {trecho_h3}.")
    return " ".join(achados)


def leitura_robustez(robustez: pl.DataFrame) -> str:
    """Resume o padrão central do Quadro 3 a partir de robustez.csv."""
    if robustez.is_empty():
        return ""
    linhas = _indexar(robustez)
    variantes = ("principal", "sem_articulacao", "sem_pj", "sem_administrador")
    nomes_variantes = {
        "principal": "na especificação principal",
        "sem_articulacao": "na rede sem pontos de articulação",
        "sem_pj": "na rede sem sócios PJ",
        "sem_administrador": "na rede sem administradores",
    }

    def sinal(chave: tuple[str, str, str], variante: str) -> str:
        return _sinal_intervalo(linhas.get((*chave, "contraste"), {}), f"_{variante}")

    diretos = (
        (("H1", "conectada_menos_sem_conexao", "participacao_2025"), "H1"),
        (("H2", "vencedor_faixa_0", "participacao_2025"), r"H2 ($\delta=0$)"),
    )
    sinais_diretos = {rotulo: {v: sinal(chave, v) for v in variantes} for chave, rotulo in diretos}
    if any(
        s in ("positivo", "negativo") for mapa in sinais_diretos.values() for s in mapa.values()
    ):
        return ""

    nulos_por_contraste = {
        rotulo: [v for v in variantes if mapa[v] == "cruza_zero"]
        for rotulo, mapa in sinais_diretos.items()
    }
    ativos = [rotulo for rotulo, vs in nulos_por_contraste.items() if vs]
    if not ativos:
        return ""
    todos_quatro = all(len(nulos_por_contraste[r]) == len(variantes) for r in ativos)

    if len(ativos) == 2 and todos_quatro:
        sem_pj_sinais = {
            rotulo: sinal((h, c, r), "sem_pj") for h, c, r, rotulo in CONTRASTES if h != "H4"
        }
        sem_pj_neg = [rotulo for rotulo, s in sem_pj_sinais.items() if s == "negativo"]
        sem_pj_pos = [rotulo for rotulo, s in sem_pj_sinais.items() if s == "positivo"]
        chave_h2_1 = ("H2", "vencedor_faixa_1", "participacao_2025")
        chave_h3_total = ("H3", "ambos_menos_demais", "variacao_total")
        chave_h3_r2 = ("H3", "ambos_menos_demais", "termo_r2")
        if (
            sem_pj_neg == [r"H2 ($\delta=1$)", "H3 (total)", "H3 (R2)"]
            and not sem_pj_pos
            and sinal(chave_h2_1, "principal") == "negativo"
            and sinal(chave_h3_total, "principal") == "cruza_zero"
            and sinal(chave_h3_r2, "principal") == "cruza_zero"
            and _estado_compensacao_h3(linhas, "_sem_pj") == "sem_compensacao"
        ):
            return (
                r"Os contrastes diretos (H1 e H2 em $\delta=0$) seguem indistinguíveis de zero "
                r"nas quatro versões; sem sócios PJ, H2 ($\delta=1$) permanece negativo e H3 "
                "(total e R2) passa a ter intervalo abaixo de zero, sem indicar compensação."
            )
        return (
            r"Os contrastes diretos (H1 e H2 em $\delta=0$) seguem indistinguíveis de zero "
            "nas quatro versões da rede."
        )

    versoes_unicas = {v for r in ativos for v in nulos_por_contraste[r]}
    com_continuidade = all(
        "principal" in nulos_por_contraste[r] and len(nulos_por_contraste[r]) >= 2 for r in ativos
    )
    if len(ativos) == 2:
        if len(versoes_unicas) == 1:
            sole = next(iter(versoes_unicas))
            return (
                r"Os contrastes diretos (H1 e H2 em $\delta=0$) têm intervalos que incluem zero "
                f"{nomes_variantes[sole]}."
            )
        if com_continuidade:
            return (
                r"Os contrastes diretos (H1 e H2 em $\delta=0$) permanecem indistinguíveis de "
                "zero nas versões estimáveis da rede."
            )
        return (
            r"Os contrastes diretos (H1 e H2 em $\delta=0$) têm intervalos que incluem zero "
            "nas versões estimáveis da rede."
        )

    rotulo = ativos[0]
    vs = nulos_por_contraste[rotulo]
    if len(vs) == 1:
        return (
            f"Entre os contrastes diretos estimáveis, {rotulo} tem intervalo que inclui zero "
            f"{nomes_variantes[vs[0]]}."
        )
    escopo = "nas quatro versões da rede" if todos_quatro else "nas versões estimáveis da rede"
    if com_continuidade:
        return (
            f"Entre os contrastes diretos estimáveis, {rotulo} permanece indistinguível "
            f"de zero {escopo}."
        )
    return (
        f"Entre os contrastes diretos estimáveis, {rotulo} tem intervalos que incluem zero "
        f"{escopo}."
    )


def _estado_principal(
    resumo: pl.DataFrame, h2_comparaveis: pl.DataFrame | None = None
) -> tuple[bool, bool, str | None]:
    linhas = _indexar(resumo)
    chave_h2_1 = ("H2", "vencedor_faixa_1", "participacao_2025")
    sinais = {
        (h, c, r): _sinal_intervalo(linhas.get((h, c, r, "contraste"), {}))
        for h, c, r, _ in CONTRASTES
    }
    nucleo_nulo = all(
        sinais[chave] == "cruza_zero"
        for chave in (
            ("H1", "conectada_menos_sem_conexao", "participacao_2025"),
            ("H2", "vencedor_faixa_0", "participacao_2025"),
            ("H3", "ambos_menos_demais", "variacao_total"),
        )
    )
    outros_sem_sinal = all(
        sinal in ("cruza_zero", "indefinido")
        for chave, sinal in sinais.items()
        if chave != chave_h2_1
    )
    estado_h3 = _estado_compensacao_h3(linhas)
    h2_1_sinal = sinais[chave_h2_1]
    nulos = (
        nucleo_nulo
        and outros_sem_sinal
        and estado_h3 == "sem_compensacao"
        and h2_1_sinal in ("cruza_zero", "indefinido", "negativo")
    )
    h2_1_unico_negativo = nulos and h2_1_sinal == "negativo"
    status_h2_1 = _status_comparavel_h2(h2_comparaveis, "1")
    return nulos, h2_1_unico_negativo, status_h2_1


def achado_principal(resumo: pl.DataFrame, h2_comparaveis: pl.DataFrame | None = None) -> str:
    """Síntese curta do achado empírico para abrir a Motivação na p. 1."""
    nulos, h2_1_unico_negativo, status_h2_1 = _estado_principal(resumo, h2_comparaveis)
    if nulos:
        if h2_1_unico_negativo and status_h2_1 in ("sem_suporte", "sem_estimativa"):
            motivo = "sem suporte" if status_h2_1 == "sem_suporte" else "sem estimativa"
            return (
                "Nas compras públicas municipais paulistas, as estimativas dão pouca "
                "evidência de transmissão societária; o único contraste com intervalo negativo "
                f"na especificação principal (H2 a um passo) fica {motivo} no recorte "
                "comparável."
            )
        if h2_1_unico_negativo:
            return (
                "Nas compras públicas municipais paulistas, as estimativas dão pouca "
                "evidência de transmissão societária; na especificação principal, apenas "
                r"o contraste de H2 em $\delta=1$ tem intervalo abaixo de zero."
            )
        return (
            "Nas compras públicas municipais paulistas, as estimativas dão pouca evidência "
            "de persistência política pela rede societária."
        )
    return ""


def sintese_discussao(resumo: pl.DataFrame, h2_comparaveis: pl.DataFrame | None = None) -> str:
    """Frase de abertura da Discussão ancorada nos mecanismos e no resultado observado."""
    nulos, _, _ = _estado_principal(resumo, h2_comparaveis)
    if nulos:
        return (
            "No conjunto das estimativas, os padrões previstos por captura ou por transmissão "
            "societária não se confirmam:"
        )
    return (
        "A leitura econômica dos contrastes depende da direção em cada distância, da estabilidade "
        "nos placebos e do suporte nas amostras comparáveis:"
    )


def _ler_tabela(pasta: Path, nome: str) -> pl.DataFrame:
    return pl.read_csv(pasta / nome) if (pasta / nome).is_file() else pl.DataFrame()


def numeros_tex(pasta: Path, sintetica: bool = False) -> str:
    resumo = _ler_tabela(pasta, "resumo_estimacao.csv")
    robustez = _ler_tabela(pasta, "robustez.csv")
    h2_comparaveis = _ler_tabela(pasta, "h2_comparaveis.csv")
    campos = {
        "tabelaEstimativas": tabela_estimativas(resumo),
        "tabelaCategorias": tabela_categorias(resumo),
        "tabelaRobustez": tabela_robustez(robustez),
        "achadoPrincipal": achado_principal(resumo, h2_comparaveis),
        "leituraResultados": leitura_resultados(resumo, h2_comparaveis),
        "leituraHDoisCompEscala": leitura_h2_comparaveis_escala(h2_comparaveis),
        "leituraRobustez": leitura_robustez(robustez),
        "sinteseDiscussao": sintese_discussao(resumo, h2_comparaveis),
        "leituraHDoisComparaveis": leitura_h2_comparaveis(
            h2_comparaveis.iter_rows(named=True)
        ).replace("%", r"\%"),
        "avisoAmostra": r"\textbf{Amostra sintética para teste.}" if sintetica else "",
    }
    return escrever_macros(Numeros.ler(pasta)) + "".join(
        f"\\newcommand{{\\{nome}}}{{%\n{corpo}\n}}\n" for nome, corpo in campos.items()
    )


def contar_paginas(pdf: Path) -> int:
    """Páginas de um PDF: `pdfinfo` quando existe, senão contagem dos objetos /Type /Page."""
    if shutil.which("pdfinfo"):
        saida = subprocess.run(
            ["pdfinfo", str(pdf)], capture_output=True, text=True, check=True
        ).stdout
        return int(re.search(r"^Pages:\s+(\d+)", saida, re.MULTILINE).group(1))  # type: ignore[union-attr]
    return len(re.findall(rb"/Type\s*/Page(?![a-z])", pdf.read_bytes()))


def preparar(caminhos: Caminhos, destino: Path) -> Path:
    """Copia fontes e figuras para `destino` e grava `numeros.tex`; devolve o `.tex` principal."""
    destino.mkdir(parents=True, exist_ok=True)
    for nome in ("relatorio.tex", "referencias.bib"):
        shutil.copy2(FONTES / nome, destino / nome)
    for antigo in destino.glob("*.pdf"):
        antigo.unlink()
    pasta_figuras = caminhos.resultados / "figures"
    for figura in pasta_figuras.glob("*.pdf") if pasta_figuras.is_dir() else ():
        shutil.copy2(figura, destino / figura.name)
    sint = (caminhos.dados / MARCADOR).is_file()
    (destino / "numeros.tex").write_text(
        numeros_tex(caminhos.resultados / "tables", sint), encoding="utf-8"
    )
    return destino / "relatorio.tex"


def compilar(principal: Path) -> Path:
    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", principal.name],
        cwd=principal.parent,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return principal.with_suffix(".pdf")


def executar(ctx: Contexto) -> None:
    reconstrucoes = () if (ctx.caminhos.dados / MARCADOR).is_file() else ("reconstrucao",)
    ctx.caminhos.exigir_resultados(
        (
            "resumo_estimacao",
            "robustez",
            "comparabilidade_h2",
            "h2_comparaveis",
            "permanencia_h4",
            "rede_resumo",
            "links_pc1",
            "validacao_panel",
            "mercados_sem_empenho",
            *reconstrucoes,
        ),
        (
            "figura1_exemplo",
            "rede_componentes",
            "rede_distancias",
            "gradiente_h2",
            "decomposicao_h3",
        ),
        "pdf",
    )
    principal = preparar(ctx.caminhos, ctx.caminhos.dados / "build" / "report")
    try:
        pdf = compilar(principal)
    except subprocess.CalledProcessError as erro:
        raise RuntimeError(f"latexmk falhou:\n{erro.stdout[-3000:]}") from erro
    paginas = contar_paginas(pdf)
    if not 0 < paginas <= MAXIMO_PAGINAS:
        raise RuntimeError(f"relatório com {paginas} páginas; o máximo é {MAXIMO_PAGINAS}")
    ctx.caminhos.saida.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=ctx.caminhos.saida) as pasta:
        compilado = Path(pasta) / pdf.name
        shutil.copy2(pdf, compilado)
        compilado.replace(ctx.caminhos.saida / pdf.name)
