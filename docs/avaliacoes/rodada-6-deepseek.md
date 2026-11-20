# Parecer independente — RODADA 6

**Escopo e método.** Li os dois PDFs transcritos, o guia de fala e os documentos de método, e confrontei os números do relatório/deck com os extratos de `resumo_estimacao`, `h2_comparaveis`, `sensibilidade_pre_periodos`, `sensibilidade_apenas_setembro`, `sensibilidade_sem_autofinanciamento`, `sensibilidade_sem_pessoal_ou_credor_publico`, `sensibilidade_sem_articulacao_sementes_fixas`, `sensibilidade_sem_gigante`, `auditoria_h2_comparaveis`, `sensibilidade_gigante` e `concentracao_gigante_h2`. Sem visuais e sem código: não avalio figuras nem audito o pipeline; avalio validade, clareza e fidelidade ao que está publicado.

## 1. Nota

| Critério | Nota |
|---|---:|
| Relevância | 9,50 |
| Redes | 9,35 |
| Profundidade | 9,30 |
| Clareza | 9,18 |
| **Média** | **9,33** |

A nota não chega a 9,5 por **dois defeitos corrigíveis**, não por limite de dados: a coluna “Sem articulação” do Quadro 3 não reproduz o CSV publicado (item 3.1) e a colisão do símbolo δ (item 3.2). Os limites de poder, componente gigante e ciclo único estão declarados e **não** são penalizados por si.

## 2. Resolução da R5

Confirmo, com conferência por nome de campo, os itens centrais da R5:

- **Auditoria H2 3+**: ≥99% das observações nas bandas principal e comparável são do gigante; peso δ=1 A 60,46% / B 66,68%; IC estreito explicitamente **condicional** à inferência municipal, sem resolver dependência entre municípios nem generalizar a outros componentes (relatório §4/§6, slides 7/11, `rede_coortes.md`, `auditoria_h2.md`). O IC de 0,055 p.p. [0,001; 0,109] é corretamente lido como diferença entre coortes quase coincidentes (Jaccard 97,4%, correlação 0,971), não como informação nova.
- **H3**: unidade rede–município, peso municipal 1 por coorte antes do núcleo, média por rede e não gasto agregado; R1+R2+R3 = total (0,0004 − 0,0512 + 0,0103 = −0,0406) e R1 interno 0,0004 + (R2+R3) −0,0410 = −0,0406. Identidades conferem.
- **H2**: previsão de vantagem positiva decrescente sob comparabilidade explicitada; δ=1 negativo com ressalvas de placebo; meia diferença como normalização, não efeito causal da distância.
- **H4**: elegibilidade só no pré, ranking de 2025 com entrantes, médias municipais 23/78 na janela de 5 p.p. distintas do salto no corte; EMD 277,1 p.p. e IC além do suporte declarados.
- **Demais itens R5**: H1/δ=0 presentes em todas as sensibilidades relevantes; 2025 nominal sem deflação; erro de sobrevivência do complemento de outubro; sem administradores muda sementes e caminhos; bandas H1 por categoria; retirada da comparação de magnitudes placebo em H3; H3 sem famílias de testes; “10 redes” adicional a “10 municípios”; não subtração do pré de B; PC2 removido; bH4-75 no relatório. Todos implementados.

## 3. Erros atuais comprovados

### 3.1 Quadro 3, coluna “Sem articulação”, não reproduz o CSV

Referência: relatório §5, Quadro 3 (`robustez.csv` citado na nota) × `sensibilidade_sem_articulacao_sementes_fixas.csv`.

| Linha | Quadro 3 | CSV publicado |
|---|---:|---:|
| H1 | −0,0150 | −0,0167201 |
| H2 δ=0 | −0,0020 | −0,01736785 |
| H2 δ=3+ | n.d. | 0,002214778 |

O caso decisivo é H2 δ=0: com **sementes fixas**, a coorte direta é preservada por construção, e o CSV traz exatamente o principal (−0,01736785, mesmo IC e mesmo EMD). Logo −0,0020 **não pode** ser a variante documentada em `docs/sensibilidades.md` (“com sementes fixas”); é a variante antiga, que remove sementes junto com os pontos de articulação — justamente o que a Rodada 1 prometeu distinguir. O texto do §5 e o slide 10 também não dizem “sementes fixas”.

**Solução no escopo**: regenerar o Quadro 3 a partir do CSV publicado; se a intenção for manter as duas variantes, rotular a coluna como “sem articulação, sementes reselecionadas” e acrescentar a coluna “sementes fixas”, alinhando `docs/sensibilidades.md`. Não muda a conclusão (“H1 e H2 δ=0 cruzam zero em todas as variantes”), mas hoje tabela e CSV divergem.

### 3.2 Colisão do símbolo δ

Referência: §2 “δik = min…/2” (distância de rede) × §3 equação (1) “δ^ℓ T_m M_m” (coeficiente de interação do RD) × §4 “H2 (δ = 0, 1, 2, 3+)”. O mesmo δ nomeia a distância e o coeficiente de inclinação. O leitor precisa inferir pelo contexto; em H2 o δ do eixo é distância, não o parâmetro do modelo.

**Solução no escopo**: renomear a interação para θ^ℓ (ou τ^ℓ) na equação e no texto, ou renomear a distância para k/d. Correção de uma linha na eq. (1) e duas menções.

## 4. Opcionais (não são erros)

1. **Multiplicidade na família principal.** H1 (1) + H2 (4) + H3 (4) = 9 testes nominais; a taxa de erro família é ~37%. O texto diz que H1–H3 são principais com inferência nominal, mas não justifica a escolha. Uma frase (“testes pré-especificados, cada hipótese avaliada separadamente”) ou uma coluna Holm para os 9 testes resolveria; o δ=1 já aparece com pHolm 0,077 na categoria, o que sinaliza o risco.
2. **Controle de H1 estruturalmente isolado.** O controle é “sem caminho a A nem B”, isto é, firma isolada; H1 é o salto diferencial conectada × isolada, não “conectada × não conectada comparável”. Vale uma oração explicitando isso; a validade do RD não é afetada (coortes pré-fixadas), só a generalização.
3. **1,25 p.p. pós-menos-pré.** É um RD sobre a variação unitária (bandas do pós), não a diferença dos dois saltos reportados (−4,06 e −2,75). “Janelas distintas” explica a interpretação, mas não por que o número não é −1,31; uma oração (“não é a diferença dos dois saltos”) evita a leitura errada.
4. **“Média por rede”.** Com peso municipal 1 dividido entre as redes do município, é média ponderada por município das médias por rede, não média simples sobre redes. “Cada município soma peso um” já quase diz isso; trocar “média por rede” por “média das redes com peso municipal unitário” fecha a lacuna.
5. **Descritivas de H4 em 25% e 75%.** São 40,0% vs 91,8% e 96,2% vs 49,3%; o relatório só reporta 50% (82,6% vs 81,5%). Como o RD em 25% não é estimável e em 75% tem banda de 73,2 p.p., a escolha do limiar central é defensável, mas convém dizer por que as outras descritivas não entram.
6. **“16.547.513 pessoas” (slide 3)** vs “vértices de pessoas/PJ” (§2). Precisão mínima.
7. **Gramática**: “Sem administradores mudam sementes e caminhos” → “A variante sem administradores muda sementes e caminhos”. Citação da ADI 4650 com parênteses aninhados; ABNT pediria “(BRASIL, 2015)”.

## 5. Limites de dados (não punidos)

Ciclo único, poder limitado, dominância do gigante, casamento parcial doador–empresa (41,0%/43,4%), homônimos, empenho ≠ contrato, ausência de conexões informais. Estão declarados no §6 e no slide 12; punir a nota por eles seria punir a honestidade do desenho.

## 6. Veredito

Trabalho de altíssimo nível para EAE1429: pergunta relevante, rede construída com 24,7 milhões de vínculos, RDD com CCT, bootstrap municipal, placebos, EMD, densidade, Holm e um conjunto raro de sensibilidades; conclusões nulas reportadas sem maquiagem e com distinção explícita entre imprecisão e ausência de efeito. A conferência numérica que fiz (Quadro 1 × extratos; Quadro 2 × identidades de H1/H2/H3/H4; tempos do guia = 600 s; 12 slides; 5 páginas) fecha em quase todos os pontos.

**Média 9,33.** Fica abaixo de 9,5 por dois defeitos corrigíveis — a inconsistência do Quadro 3 com o CSV de articulação e a colisão de δ —, não por limite inevitável de dados. Corrigidos os dois, e com os opcionais 1–3 incorporados, o trabalho passa com folga para a faixa 9,5+.
