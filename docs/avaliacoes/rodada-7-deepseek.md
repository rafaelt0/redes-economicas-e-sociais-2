## Parecer independente — DeepSeek, rodada 7 (reavaliação em esforço alto)

**Escopo e método.** Esta leitura usa apenas o pacote transcrito: os dois PDFs em texto, o guia de fala, os documentos de método e os extratos/tabelas agregadas nomeados. **Não inclui auditoria independente do código, execução de testes nem inspeção visual dos PDFs ou do PPTX.** Conferi os números por *nome de campo* contra `resumo_estimacao`, `h2_comparaveis`, `sensibilidade_pre_periodos`, `sensibilidade_placebo`, `sensibilidade_apenas_setembro`, `sensibilidade_sem_autofinanciamento`, `sensibilidade_sem_pessoal_ou_credor_publico`, `sensibilidade_sem_articulacao_sementes_fixas`, `sensibilidade_sem_gigante`, `robustez`, `auditoria_h2_comparaveis`, `concentracao_gigante_h2`, `sensibilidade_gigante`, `sensibilidade_escopo_tcesp`, `permanencia_h4` e `rede_componentes`. A ausência de uma linha de categoria nos extratos seletivos não foi tratada como ausência no CSV.

## 1. Nota

| Critério | Nota |
|---|---:|
| Relevância | 9,60 |
| Uso dos conceitos de rede | 9,60 |
| Profundidade | 9,55 |
| Clareza | 9,45 |
| **Média aritmética** | **9,55** |

A nota não foi calibrada para 9,5. O patamar reflete que os dois defeitos apontados na R6 — colisão de δ e divergência do Quadro 3 — estão de fato corrigidos, e que a conferência numérica fecha em todos os pontos verificáveis. O que segura a média abaixo de 9,6 é um conjunto de arestas pequenas, quase todas de rótulo ou de reporte, não de dado.

## 2. Resolução das pendências da R6

**Colisão de δ — resolvida.** A eq. (1) usa θ^ℓ T_m M_m; δ permanece exclusivamente como distância de rede em §2, na Figura 1 e nas faixas de H2. Não há mais ambiguidade de símbolo no relatório.

**Quadro 3 — resolvido.** Confrontei as três colunas variantes com `robustez.csv`:

| Linha | Quadro 3 | `robustez.csv` (sem_articulacao) |
|---|---:|---:|
| H1 | −0,0150 | −0,0149590 |
| H2 δ=0 | −0,0020 | −0,0019504 |
| H2 δ=1 | n.d. | n.d. |
| H2 δ=3+ | n.d. | n.d. |
| H3 total | n.d. | n.d. |

A coluna agora é a variante com sementes **reselecionadas**, e a nota do quadro diz isso explicitamente, separando a sensibilidade com sementes fixas (`sensibilidade_sem_articulacao_sementes_fixas.csv`), cujo H2 δ=0 é −0,01736785 por construção. A R6 tratava como erro o que era especificação distinta mal rotulada; a rotulagem foi corrigida e os valores conferem.

**Ajustes editoriais da R7 — presentes.** “Sem esses empenhos” (§5, exclusão de pessoal/credor público); “RD da diferença de participação pós menos pré” (§5, H2 δ=1); “sem evidência de ganho compensatório em R3” (§5). Os três estão no texto atual.

## 3. Conferência numérica (amostra do que foi checado)

**Quadro 1 × `resumo_estimacao.csv`** — todos os contrastes batem: H1 −0,0171 [−0,1619; 0,1277], EMD 0,2070; H2 δ=0 −0,0174 [−0,0859; 0,0511], EMD 0,0979; δ=1 −0,0406 [−0,0716; −0,0097], EMD 0,0442; δ=2 −0,0081 [−0,0223; 0,0062]; δ=3+ 0,0006 [−0,0029; 0,0041], EMD 0,0050; H3 total −0,0406 [−0,1020; 0,0208], EMD 0,0878; R1 0,0004 [−0,0012; 0,0020]; R2 −0,0512 [−0,1394; 0,0369]; R3 0,0103 [−0,0449; 0,0654]; H4 50% 0,1092 [−1,8294; 2,0478], EMD 2,7711; H4 75% 0,0039 [−0,0796; 0,0875]. Placebos de nível e p-valores também batem por linha, inclusive o placebo único repetido de H3 em R1/R2/R3 (previsto na nota).

**Identidades algébricas.** R1+R2+R3 = 0,0004 − 0,0512 + 0,0103 = −0,0405 ≈ total −0,0406 (arredondamento). R1 interno + R2+R3 interno = 0,0004 − 0,0410 = −0,0406. H1 = direta − sem conexão = −0,0157 − 0,0014 = −0,0171. H2 δ=0 e δ=1 = (βB − βA)/2 com as categorias do Quadro 2. H4 50% = (−0,0301 + 0,2485)/2 = 0,1092. Todas fecham.

**Sensibilidades × texto.** H2 δ=1 pós-menos-pré 1,25 p.p. [−4,08; 6,58] = `sensibilidade_placebo`; sem autofinanciamento −2,85 p.p. [−6,25; 0,55]; placebo de variação pré −2,75 p.p. [−7,38; 1,87]; coorte B a um passo −7,68 p.p. [−13,50; −1,86] (`sensibilidade_pre_periodos`); pessoal/credor público 50,7% (`fracao_excluido` 0,5073); sem esses empenhos, H1 e H3 cruzam zero e H2 δ=1 segue negativa com IC fora de zero; apenas setembro deixa H2 δ=1 sem suporte. Tudo confere.

**Auditorias.** Recorte comparável 3+: 2.674 estratos, Jaccard 97,44%, correlação 0,9709, 999 réplicas, contraste 0,0553 p.p. [0,0012; 0,1094] — o relatório arredonda para 0,055 e 0,001–0,109. Concentração 3+: ≥99% nas bandas principal e comparável. H3 AMBOS: 99,98% do empenho e peso do gigante. H4 exclusivas 50%: peso 100,0%. Componentes: 8.003.121 no total, 76,25% unitários. Guia: 600 s e divisão 180/160/165/95. Deck: 12 slides. Relatório: 5 páginas.

## 4. Problemas corrigíveis remanescentes

Nenhum é erro de dado; todos são de reporte. Nenhum exige mudar desenho, bandas ou conclusões.

1. **Multiplicidade na família principal não justificada.** H1 (1) + H2 (4) + H3 (4) = 9 testes nominais. O texto declara a escolha, mas não a justifica; o único contraste principal com IC fora de zero é H2 δ=1 (p = 0,010), e a categoria correspondente tem pHolm = 0,077 na família secundária. Uma frase em §3 — testes pré-especificados, avaliados separadamente — ou uma coluna Holm para os 9 fecharia a lacuna. Este é o ponto que mais pesa na nota de profundidade.
2. **Slide 6, “placebo = 0,020”** sem unidade. O placebo é nível de participação prévia, não participação de 2025; o Quadro 1 define “Pré (nível)”, o slide não. Correção de uma palavra.
3. **Notação de unidade em §5.** “média pós ponderada é 1,77% do elemento (DP 9,87 p.p.)”: 1,77% e 9,87 p.p. são a mesma escala; convém escrever “1,77 p.p.” ou “1,77% (DP 9,87%)”.
4. **Citação ABNT aninhada.** “(BRASIL. Supremo Tribunal Federal (Tribunal Pleno), 2015)” permanece; o padrão seria “(BRASIL, 2015)”. Item cosmético herdado da R6.
5. **Quadro 1 denso.** Sete colunas numéricas mais IC e a coluna “Pré (nível)” exigem leitura cuidadosa; a nota explica, mas o leitor pode confundir meia banda com placebo. Não é erro; é custo de clareza, e não pude avaliar o layout visual.

## 5. Limitações de dados (não penalizadas)

Ciclo eleitoral único; poder limitado e EMDs grandes; dominância do componente gigante em H2 3+ e H4; casamento parcial doador–empresa (41,0%/43,4%); doações PF pós-ADI 4650 como sinal fraco; homônimos e CPF de seis dígitos; empenho ≠ contrato; conexões informais e parentesco não observados; interferência entre municípios da mesma rede não absorvida pelo agrupamento; H4 com bandas amplas e IC além do suporte. Todas estão declaradas em §6 e no slide 12. Punir a nota por elas seria punir a honestidade do desenho.

## 6. Veredito

**Apta para entrega.** A entrega cumpre os requisitos de forma (5 páginas, 12 slides, guia de 600 s) e de conteúdo (conceitos e resultados apoiados nos CSVs). A pergunta é relevante, a rede é construída em escala real (24,7 milhões de vínculos), o desenho combina RDD com correção de viés, IC CCT, bootstrap municipal, densidade, placebos, EMD e Holm, e o conjunto de sensibilidades é incomum para um trabalho de graduação. Os resultados nulos são reportados sem maquiagem, com distinção explícita entre imprecisão e ausência de efeito. Os dois defeitos da R6 estão corrigidos e não encontrei divergência numérica nos pontos que pude conferir.

**Média 9,55.** Acima de 9,5 por mérito, não por calibração: o que separa a entrega de 9,6+ é a justificativa da inferência nominal na família principal e três arestas de rótulo, todas corrigíveis em texto. Não alterei arquivos e não solicito mudança de desenho.

*Observação sobre a comparação Sol/DeepSeek: não posso atestar a configuração de esforço do Sol nem reproduzir a nota 9,63 dele; este parecer cobre apenas a minha leitura em esforço alto, sem inspeção visual nem auditoria de código. A média conjunta só deve ser calculada após a rodada do Sol em High ser concluída.*
