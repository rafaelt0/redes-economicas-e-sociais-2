import math

import polars as pl

from redes.numeros import leitura_h2_comparaveis, status_comparavel_h2
from redes.report import (
    CONTRASTES,
    achado_principal,
    leitura_h2_comparaveis_escala,
    leitura_resultados,
    leitura_robustez,
    numeros_tex,
    sintese_discussao,
    tabela_categorias,
    tabela_estimativas,
    tabela_robustez,
)


def test_relatorio_le_o_resumo_real_e_distingue_o_intervalo_do_contraste():
    resumo = pl.DataFrame(
        {
            "hipotese": ["H1", "H1"],
            "categoria": ["conectada_menos_sem_conexao", "conectada_incumbente"],
            "tipo": ["contraste", "categoria"],
            "resultado": ["participacao_2025", "participacao_2025"],
            "estimativa": [-0.1234, -0.8912],
            "ic_inf": [-0.5, -1.0],
            "ic_sup": [0.25, -0.4],
            "municipios_tratados": [22, 18],
            "municipios_controle": [28, 20],
        }
    )
    quadro = tabela_estimativas(resumo)
    assert "-0,1234" in quadro
    assert "-0,8912" not in quadro
    assert "reamostragem" in quadro
    assert (
        "o placebo usa a participação pré-eleitoral da rede e repete-se no total e em R1--R3"
        in quadro
    )
    categorias = tabela_categorias(resumo)
    assert "-0,8912" in categorias
    assert "18 & 20" in categorias
    assert "IC robusto" in categorias


def test_relatorio_mostra_o_suporte_e_o_contraste_do_recorte_comparavel(tmp_path):
    pl.DataFrame(
        {
            "tipo": ["contraste", "contraste"],
            "placebo": [False, False],
            "categoria": ["vencedor_faixa_1", "vencedor_faixa_3+"],
            "estimavel": [False, True],
            "estimativa": [None, 0.0023],
            "ic_inf": [None, 0.001],
            "ic_sup": [None, 0.0041],
        }
    ).write_csv(tmp_path / "h2_comparaveis.csv")
    texto = numeros_tex(tmp_path)
    assert "indefinida na faixa 1" in texto
    assert "por suporte municipal insuficiente" not in texto
    assert r"faixa 3+, o contraste foi de 0,230 p.p. (IC de 95\% de 0,100 a 0,410)" in texto


def _resumo_contrastes(
    overrides: dict[tuple[str, str, str], tuple[float | None, float | None]] | None = None,
    *,
    cat_overrides: dict[tuple[str, str, str], tuple[float | None, float | None]] | None = None,
) -> pl.DataFrame:
    sobrescritas = overrides or {}
    cats = cat_overrides or {}
    linhas = []
    for h, c, r, _ in CONTRASTES:
        inf, sup = sobrescritas.get((h, c, r), (-0.05, 0.05))
        est = (inf + sup) / 2 if (inf is not None and sup is not None) else None
        linhas.append(
            {
                "hipotese": h,
                "categoria": c,
                "resultado": r,
                "tipo": "contraste",
                "estimativa": est,
                "ic_inf": inf,
                "ic_sup": sup,
            }
        )
    for chave in (
        ("H3", "ambos", "termo_r1"),
        ("H3", "ambos", "termo_compensacao"),
    ):
        inf, sup = cats.get(chave, (-0.05, 0.05))
        est = (inf + sup) / 2 if (inf is not None and sup is not None) else None
        linhas.append(
            {
                "hipotese": chave[0],
                "categoria": chave[1],
                "resultado": chave[2],
                "tipo": "categoria",
                "estimativa": est,
                "ic_inf": inf,
                "ic_sup": sup,
            }
        )
    return pl.DataFrame(linhas)


def test_achado_principal_verifica_unicidade_sobre_todos_os_contrastes():
    h2_comp = pl.DataFrame(
        {
            "tipo": ["contraste"],
            "placebo": [False],
            "categoria": ["vencedor_faixa_1"],
            "estimavel": [False],
            "motivo": ["erro-padrão degenerado"],
        }
    )
    so_h2_1 = _resumo_contrastes({("H2", "vencedor_faixa_1", "participacao_2025"): (-0.06, -0.01)})
    assert "único contraste com intervalo negativo" in achado_principal(so_h2_1, h2_comp)
    assert "não se confirmam" in sintese_discussao(so_h2_1, h2_comp)

    dois_neg = _resumo_contrastes(
        {
            ("H2", "vencedor_faixa_1", "participacao_2025"): (-0.06, -0.01),
            ("H2", "vencedor_faixa_2", "participacao_2025"): (-0.04, -0.005),
        }
    )
    assert achado_principal(dois_neg, h2_comp) == ""
    assert "depende da direção" in sintese_discussao(dois_neg, h2_comp)

    h2_1_pos = _resumo_contrastes({("H2", "vencedor_faixa_1", "participacao_2025"): (0.01, 0.06)})
    assert achado_principal(h2_1_pos, h2_comp) == ""


def test_compensacao_h3_exige_dois_extremos_finitos():
    r1_sem_inf = _resumo_contrastes(cat_overrides={("H3", "ambos", "termo_r1"): (None, 0.01)})
    assert "compensação ficou sem estimativa" in leitura_resultados(r1_sem_inf)
    assert achado_principal(r1_sem_inf) == ""

    comp_sem_sup = _resumo_contrastes(
        cat_overrides={("H3", "ambos", "termo_compensacao"): (-0.05, None)}
    )
    assert "compensação ficou sem estimativa" in leitura_resultados(comp_sem_sup)

    r1_nan = _resumo_contrastes(cat_overrides={("H3", "ambos", "termo_r1"): (math.nan, 0.01)})
    assert "compensação ficou sem estimativa" in leitura_resultados(r1_nan)


def test_h2_comparavel_distingue_suporte_municipal_de_erro_padrao_degenerado():
    so_h2_1 = _resumo_contrastes({("H2", "vencedor_faixa_1", "participacao_2025"): (-0.06, -0.01)})

    por_suporte = pl.DataFrame(
        {
            "tipo": ["categoria", "categoria", "contraste"],
            "placebo": [False, False, False],
            "categoria": ["faixa_a_1", "faixa_b_1", "vencedor_faixa_1"],
            "estimavel": [False, False, False],
            "motivo": [
                "menos de 10 municípios de um lado do corte",
                "menos de 10 municípios de um lado dentro da banda",
                "alguma categoria não é estimável",
            ],
        }
    )
    assert "por suporte municipal insuficiente" in leitura_h2_comparaveis(
        por_suporte.iter_rows(named=True)
    )
    assert "mas sem suporte no recorte comparável" in leitura_resultados(so_h2_1, por_suporte)
    assert "fica sem suporte no recorte comparável" in achado_principal(so_h2_1, por_suporte)
    assert status_comparavel_h2(por_suporte.iter_rows(named=True), "2") is None

    ep_degenerado = pl.DataFrame(
        {
            "tipo": ["categoria", "categoria", "contraste"],
            "placebo": [False, False, False],
            "categoria": ["faixa_a_1", "faixa_b_1", "vencedor_faixa_1"],
            "estimavel": [True, True, False],
            "motivo": [None, None, "erro-padrão degenerado"],
        }
    )
    texto_deg = leitura_h2_comparaveis(ep_degenerado.iter_rows(named=True))
    assert "indefinida na faixa 1" in texto_deg
    assert "suporte municipal" not in texto_deg
    assert "mas sem estimativa no recorte comparável" in leitura_resultados(so_h2_1, ep_degenerado)
    assert "fica sem estimativa no recorte comparável" in achado_principal(so_h2_1, ep_degenerado)

    misto_mesma_faixa = pl.DataFrame(
        {
            "tipo": ["categoria", "categoria", "contraste"],
            "placebo": [False, False, False],
            "categoria": ["faixa_a_1", "faixa_b_1", "vencedor_faixa_1"],
            "estimavel": [False, False, False],
            "motivo": [
                "menos de 10 municípios de um lado do corte",
                "erro-padrão degenerado",
                "alguma categoria não é estimável",
            ],
        }
    )
    assert status_comparavel_h2(misto_mesma_faixa.iter_rows(named=True), "1") == "sem_estimativa"

    misto = pl.DataFrame(
        {
            "tipo": ["categoria", "categoria", "contraste", "contraste"],
            "placebo": [False, False, False, False],
            "categoria": ["faixa_a_0", "faixa_b_0", "vencedor_faixa_0", "vencedor_faixa_1"],
            "estimavel": [False, False, False, False],
            "motivo": [
                "menos de 10 municípios de um lado do corte",
                "menos de 10 municípios de um lado do corte",
                "alguma categoria não é estimável",
                "erro-padrão degenerado",
            ],
        }
    )
    texto_misto = leitura_h2_comparaveis(misto.iter_rows(named=True))
    assert "na faixa 0 por suporte municipal insuficiente" in texto_misto
    assert "ficou sem estimativa na faixa 1" in texto_misto


def _quadro_robustez(
    overrides: dict[tuple[str, str, str, str, str], tuple[float | None, float | None]]
    | None = None,
    *,
    excluir: set[tuple[str, str, str, str]] | None = None,
) -> pl.DataFrame:
    sobrescritas = overrides or {}
    omitidos = excluir or set()
    variantes = ("principal", "sem_articulacao", "sem_pj", "sem_administrador")
    linhas = []
    chaves = [(h, c, r, "contraste") for h, c, r, _ in CONTRASTES if h != "H4"] + [
        ("H3", "ambos", "termo_r1", "categoria"),
        ("H3", "ambos", "termo_compensacao", "categoria"),
    ]
    for h, c, r, tipo in chaves:
        if (h, c, r, tipo) in omitidos:
            continue
        linha: dict[str, object] = {
            "hipotese": h,
            "categoria": c,
            "resultado": r,
            "tipo": tipo,
        }
        for v in variantes:
            inf, sup = sobrescritas.get((h, c, r, tipo, v), (-0.05, 0.05))
            linha[f"estimativa_{v}"] = (
                (inf + sup) / 2 if (inf is not None and sup is not None) else None
            )
            linha[f"ic_inf_{v}"] = inf
            linha[f"ic_sup_{v}"] = sup
        linhas.append(linha)
    return pl.DataFrame(linhas)


def test_leitura_h2_comparaveis_escala_e_robustez():
    h2_comp = pl.DataFrame(
        {
            "tipo": ["contraste", "contraste"],
            "placebo": [False, True],
            "categoria": ["vencedor_faixa_3+", "vencedor_faixa_3+"],
            "estimavel": [True, True],
            "estimativa": [0.00053, 0.00079],
            "ic_inf": [0.00004, -0.0001],
            "ic_sup": [0.00102, 0.0016],
            "p_valor": [0.03, 0.095],
        }
    )
    escala = leitura_h2_comparaveis_escala(h2_comp)
    assert "0,079 p.p." in escala
    assert "p=0{,}095" in escala

    base_sem_pj = {
        ("H2", "vencedor_faixa_1", "participacao_2025", "contraste", "principal"): (-0.06, -0.01),
        ("H2", "vencedor_faixa_1", "participacao_2025", "contraste", "sem_pj"): (-0.06, -0.01),
        ("H3", "ambos_menos_demais", "variacao_total", "contraste", "sem_pj"): (-0.11, -0.03),
        ("H3", "ambos_menos_demais", "termo_r2", "contraste", "sem_pj"): (-0.13, -0.03),
        ("H3", "ambos", "termo_r1", "categoria", "sem_pj"): (-0.0003, 0.001),
        ("H3", "ambos", "termo_compensacao", "categoria", "sem_pj"): (-0.12, -0.05),
    }
    assert "nas quatro versões; sem sócios PJ" in leitura_robustez(_quadro_robustez(base_sem_pj))

    # Remover um IC de H1 não pode manter a afirmação "nas quatro versões".
    h1_ausente = _quadro_robustez(
        {
            **base_sem_pj,
            ("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste", "sem_pj"): (
                None,
                None,
            ),
        }
    )
    assert "versões estimáveis da rede" in leitura_robustez(h1_ausente)
    assert "quatro versões" not in leitura_robustez(h1_ausente)

    # Remover toda a linha de H1 não pode resumir H1 como indistinguível de zero.
    sem_linha_h1 = _quadro_robustez(
        base_sem_pj,
        excluir={("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste")},
    )
    texto_sem_h1 = leitura_robustez(sem_linha_h1)
    assert "H1" not in texto_sem_h1
    assert r"H2 ($\delta=0$)" in texto_sem_h1
    assert "nas quatro versões da rede" in texto_sem_h1

    # Sem H2 (delta=1) negativo na principal, não afirma "permanece negativo".
    h2_nao_era_neg = _quadro_robustez(
        {
            **base_sem_pj,
            ("H2", "vencedor_faixa_1", "participacao_2025", "contraste", "principal"): (
                -0.05,
                0.05,
            ),
        }
    )
    assert "permanece negativo" not in leitura_robustez(h2_nao_era_neg)

    # Com H3 (total) ou H3 (R2) já negativo na principal, não afirma "passa a ter".
    h3_ja_era_neg = _quadro_robustez(
        {
            **base_sem_pj,
            ("H3", "ambos_menos_demais", "variacao_total", "contraste", "principal"): (
                -0.11,
                -0.03,
            ),
        }
    )
    assert "passa a ter" not in leitura_robustez(h3_ja_era_neg)
    h3_r2_ja_era_neg = _quadro_robustez(
        {
            **base_sem_pj,
            ("H3", "ambos_menos_demais", "termo_r2", "contraste", "principal"): (-0.13, -0.03),
        }
    )
    assert "passa a ter" not in leitura_robustez(h3_r2_ja_era_neg)

    # Com compensação ou IC incompleto em sem_pj, não afirma "sem indicar compensação".
    com_compensacao = _quadro_robustez(
        {
            **base_sem_pj,
            ("H3", "ambos", "termo_r1", "categoria", "sem_pj"): (-0.05, -0.01),
            ("H3", "ambos", "termo_compensacao", "categoria", "sem_pj"): (0.01, 0.05),
        }
    )
    assert "sem indicar compensação" not in leitura_robustez(com_compensacao)

    r1_incompleto = _quadro_robustez(
        {
            **base_sem_pj,
            ("H3", "ambos", "termo_r1", "categoria", "sem_pj"): (None, 0.001),
        }
    )
    assert "sem indicar compensação" not in leitura_robustez(r1_incompleto)

    comp_incompleto = _quadro_robustez(
        {
            **base_sem_pj,
            ("H3", "ambos", "termo_compensacao", "categoria", "sem_pj"): (-0.12, None),
        }
    )
    assert "sem indicar compensação" not in leitura_robustez(comp_incompleto)


def test_h2_comparavel_rejeita_extremos_nao_finitos_ou_ausentes(tmp_path):
    csv_texto = (
        "tipo,placebo,categoria,estimavel,motivo,estimativa,ic_inf,ic_sup,p_valor\n"
        "contraste,false,vencedor_faixa_0,true,,nan,-0.01,0.02,0.5\n"
        "contraste,false,vencedor_faixa_1,true,,0.01,inf,0.02,0.5\n"
        "contraste,false,vencedor_faixa_2,true,,0.01,,0.02,0.5\n"
    )
    (tmp_path / "h2_comparaveis.csv").write_text(csv_texto, encoding="utf-8")
    tex = numeros_tex(tmp_path)
    bloco = tex.split(r"\newcommand{\leituraHDoisComparaveis}{", 1)[1].split("}", 1)[0]
    assert "nan" not in bloco.lower()
    assert "inf" not in bloco.lower()
    assert "indefinida nas faixas 0, 1 e 2" in bloco

    df = pl.read_csv(tmp_path / "h2_comparaveis.csv")
    for faixa in ("0", "1", "2"):
        assert status_comparavel_h2(df.iter_rows(named=True), faixa) == "sem_estimativa"


def test_leitura_resultados_trata_p_holm_ausente_e_compensacao_h3():
    sem_holm = _resumo_contrastes()
    texto_sem_holm = leitura_resultados(sem_holm)
    assert "valor-p ajustado por Holm ficou indisponível" in texto_sem_holm
    assert "inconclusivo após Holm" not in texto_sem_holm

    com_comp = _resumo_contrastes(
        cat_overrides={
            ("H3", "ambos", "termo_r1"): (-0.05, -0.01),
            ("H3", "ambos", "termo_compensacao"): (0.01, 0.05),
        }
    )
    assert "R1 cai e R2+R3 cresce (compensação)" in leitura_resultados(com_comp)


def test_leitura_robustez_variante_unica_e_sem_principal():
    sem_principal_so_pj = {
        ("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste", v): (None, None)
        for v in ("principal", "sem_articulacao", "sem_administrador")
    } | {
        ("H2", "vencedor_faixa_0", "participacao_2025", "contraste", v): (None, None)
        for v in ("principal", "sem_articulacao", "sem_administrador")
    }
    texto_dois = leitura_robustez(_quadro_robustez(sem_principal_so_pj))
    assert "na rede sem sócios PJ" in texto_dois
    assert "têm intervalos que incluem zero" in texto_dois
    assert "permanec" not in texto_dois
    assert "versões estimáveis" not in texto_dois

    texto_um = leitura_robustez(
        _quadro_robustez(
            sem_principal_so_pj,
            excluir={("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste")},
        )
    )
    assert "H1" not in texto_um
    assert r"H2 ($\delta=0$) tem intervalo que inclui zero na rede sem sócios PJ." in texto_um
    assert "permanece" not in texto_um
    assert "versões estimáveis" not in texto_um

    duas_sem_principal = {
        ("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste", v): (None, None)
        for v in ("principal", "sem_administrador")
    } | {
        ("H2", "vencedor_faixa_0", "participacao_2025", "contraste", v): (None, None)
        for v in ("principal", "sem_administrador")
    }
    texto_duas = leitura_robustez(_quadro_robustez(duas_sem_principal))
    assert "têm intervalos que incluem zero nas versões estimáveis da rede." in texto_duas
    assert "permanec" not in texto_duas

    sem_est = _quadro_robustez(
        {
            ("H1", "conectada_menos_sem_conexao", "participacao_2025", "contraste", "sem_pj"): (
                0.01,
                0.05,
            )
        }
    ).with_columns(pl.lit(None, dtype=pl.Float64).alias("estimativa_sem_pj"))
    assert "n.d.*" not in tabela_robustez(sem_est)


def test_csv_parcial_categoria_vazia_e_estimativa_ausente(tmp_path):
    (tmp_path / "h2_comparaveis.csv").write_text(
        "tipo,placebo,categoria,estimavel,motivo,estimativa,ic_inf,ic_sup,p_valor\n"
        "contraste,false,,false,alguma categoria não é estimável,,,,\n"
        "contraste,false,malformada,true,,0.01,-0.01,0.03,0.5\n"
        "contraste,false,vencedor_faixa_0,true,,0.001,-0.001,0.003,0.5\n",
        encoding="utf-8",
    )
    (tmp_path / "resumo_estimacao.csv").write_text(
        "hipotese,estimativa\nH1,0.1\n", encoding="utf-8"
    )
    tex = numeros_tex(tmp_path)
    assert "na faixa 0, o contraste foi de 0,100 p.p." in tex

    # Estimativa principal em branco em H1 com ICs finitos deve virar n.d. no quadro e na prosa.
    rob = _quadro_robustez().with_columns(
        pl.when(
            (pl.col("hipotese") == "H1")
            & (pl.col("categoria") == "conectada_menos_sem_conexao")
            & (pl.col("tipo") == "contraste")
        )
        .then(None)
        .otherwise(pl.col("estimativa_principal"))
        .alias("estimativa_principal")
    )
    assert "n.d." in tabela_robustez(rob)
    texto_rob = leitura_robustez(rob)
    assert "quatro versões" not in texto_rob
    assert "permanec" not in texto_rob
    assert "têm intervalos que incluem zero nas versões estimáveis da rede." in texto_rob

    # Mesmo comportamento no resumo principal: estimativa ausente invalida o contraste.
    res = _resumo_contrastes().with_columns(
        pl.when((pl.col("hipotese") == "H1") & (pl.col("tipo") == "contraste"))
        .then(None)
        .otherwise(pl.col("estimativa"))
        .alias("estimativa")
    )
    assert "H1 não foi estimável" in leitura_resultados(res)
