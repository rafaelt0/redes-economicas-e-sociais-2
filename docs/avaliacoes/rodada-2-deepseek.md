# Parecer — EAE1429, trabalho final

## 1. Escopo e limite desta avaliação

Avaliei o material transcrito: relatório (5 páginas), deck (12 slides), guia de fala, `docs/decisoes.md`, `docs/inferencia.md`, `docs/sensibilidades.md`, `docs/avaliacoes/respostas.md` e as tabelas de resultados. **O que pude verificar de fato:** consistência numérica entre texto, deck, guia e CSVs; somas de tempo do guia; contagem de páginas e slides; coerência interna das definições e da especificação; aderência das respostas da Rodada 1 ao que foi efetivamente alterado. **O que não pude verificar:** o código, o conteúdo gráfico dos slides (a transcrição é só texto — os slides 3 e 6 remetem a figuras que não aparecem no extrato), o alinhamento completo de colunas dos CSVs (a transcrição declara supressão de colunas técnicas). Não faço auditoria independente de código sem ferramentas e não trato a validação local relatada (197 testes, lint, réplicas contra `rdrobust`) como verificada por mim — trato como **declarada e internamente consistente** com `docs/inferencia.md`.

Não considero falha a ausência de resumo/abstract: o projeto define seção de Motivação, e ela cumpre a função.

---

## 2. Notas

| Critério | Nota | Justificativa em uma linha |
|---|---|---|
| Relevância | **9,00** | Pergunta de primeira ordem (persistência de poder via rede societária em compras públicas), dados primários em escala real (24,7 mi de vínculos), diálogo correto com Acemoglu-Robinson, Boas et al., Baltrunaite, Cruz et al., Schisani et al. |
| Conceitos de redes | **7,50** | Usa grafo bipartido, distância, componente gigante e pontos de articulação com correção; mas δ é a única medida estrutural mobilizada, a projeção descarta intensidade societária e a previsão de Jackson-Wolinsky não é testada com nenhuma estatística de posição |
| Profundidade | **8,20** | Rigor econométrico alto (ponto corrigido por viés em tudo, IC CCT nas categorias, bootstrap municipal nos contrastes, EMD, b/2 e 2b, Holm); profundidade analítica limitada pelo poder e pela concentração no gigante |
| Clareza | **8,50** | Títulos de slide com tese, guia com tempos e papéis, unidades declaradas, n.d. explicado; restam frases circulares e um rótulo que contradiz o estimando |

**Nota geral: 8,30** (média de igual peso: 33,2/4).

Contexto da nota: a R1 deu 8,3 (Sol) e 7,4 (DeepSeek). As revisões resolvem a maior parte das objeções específicas sem introduzir erro novo de magnitude comparável. O que impede nota maior não é ausência de significância — é (i) um EMD que excede em ordem de grandeza o desfecho de interesse, (ii) H3/H4 apoiados por uma única rede, e (iii) um punhado de afirmações que ainda vendem mais do que o estimando entrega.

---

## 3. Críticas da R1: o que ficou resolvido

| Crítica R1 | Status | Evidência |
|---|---|---|
| Inferência convencional vs. CCT | **Resolvida** | `docs/inferencia.md` descreve ponto *Bias-Corrected* em todas as estimativas; IC CCT nas categorias; bootstrap estratificado por lado com h e b fixos nos contrastes; teste de regressão contra reajustes explícitos de `rdrobust`. A não identidade dos dois métodos está declarada no Quadro 1 e no Quadro 2. |
| H2 confundia distância com efeito causal | **Resolvida** | §4 explicita `(β̂_B(d) − β̂_A(d))/2`, sobreposição de 6,3%, coortes que compartilham firmas e a frase “não identifica o efeito de reduzir a distância”. `h2_comparaveis.csv` mostra n.d. em 0, 1, 2 e 0,055 p.p. [0,001; 0,109] em 3+. |
| Preenchimento de outubro | **Resolvida na essência** | Origem por vínculo, filtro de entrada até 13/09, 99,72% de reprodução nas 10,3 mi de empresas com resposta conhecida, e a ressalva correta de que isso **não** valida as ausentes. `sensibilidade_apenas_setembro.csv` mostra que H2 em δ=1 perde suporte — reportado. |
| Gigante | **Resolvida** | `sensibilidade_gigante.csv`: 99,98% do empenho prévio de AMBOS; 100% do peso de H4-50; remoção do gigante torna H3 e H4 n.d. |
| Suporte e EMD | **Resolvida** | EMD em todas as linhas, municípios por lado, b/2 e 2b, e o aviso explícito de fragilidade assintótica com poucas unidades. |
| Universo TCESP / vinculação empenho-ajuste | **Resolvida — e parte da R1 era erro** | Os desfechos usam **todos** os empenhos do painel; os 3,7% de vinculação com ajustes servem só à classificação de contratos novos. A R1 confundiu a taxa de vinculação com a construção do desfecho. Essa objeção está retirada. |
| Definições (δ, PF/PJ, A/B, AMBOS, ranking H4, entrantes) | **Quase toda resolvida** | §2 e §3 definem δ, sementes, δ=∞, A/B, AMBOS; §4 define o ranking acumulado e a inclusão de entrantes. Restam duas lacunas pontuais (P6). |
| Divergências slides/guia/PC1/PC2 | **Resolvida** | Guia soma exatamente 600 s e as colunas por pessoa fecham (180/160/165/95); PC1 traz 41,0%/43,4%; PC2 traz 14,6%/2,1%; H3 com quatro casas no guia e no texto. |
| Placebos e sinais frágeis | **Parcialmente resolvida** | O tratamento conceitual está correto (“não deduzir balanço de não rejeição”, placebo de H3 único e repetido). Mas o δ=1 continua sendo vendido como “negativo a 5%” sem a nota de Holm nos componentes (P3). |

Conferências que fiz e que fecham: H1 −0,0171 [−0,1619; 0,1277], placebo 0,0197 (p=0,821), EMD 20,7 p.p.; H2 δ=1 −0,0406 [−0,0716; −0,0097]; H3 total −0,0406 [−0,1020; 0,0208], R1 0,0004, R2 −0,0512, R3 0,0103, compensação −0,0410 [−0,0970; 0,0150]; H4-50 0,1092 [−1,8294; 2,0478], Holm 1,000. Todos batem com `resumo_estimacao.csv`. A tabela de robustez do slide 10 bate com `robustez.csv` inclusive na variante sem sócios PJ (−0,085 [−0,131; −0,039]). Isso é trabalho de sincronização sério.

---

## 4. Problemas materiais remanescentes (com solução no escopo)

**P1. O EMD torna o nulo quase sem conteúdo informativo, e isso não está dito com todas as letras.**
H1 tem EMD de 20,7 p.p. sobre um desfecho cuja média pós na coorte direta é 1,77% do elemento (DP 9,87 p.p., `descritivas_estimacao.csv`, usada em §5). O desenho só detecta efeitos ~10× a média. A literatura citada (Boas et al.; Baltrunaite) trabalha em ordem de poucos p.p. de valor de contrato.
*Solução:* (a) levar “média pós (DP)” para uma coluna do Quadro 2, lendo de `descritivas_estimacao.csv`; (b) uma frase em §6: “o EMD excede em uma ordem de grandeza a média do desfecho, de modo que o estudo é informativo sobre a ausência de efeitos grandes, não sobre ausência de efeito”. Sem reestimação, sem novos ciclos.

**P2. H3 e H4 repousam em uma única rede, e o aviso está no lugar errado.**
O gigante concentra 99,98% do empenho prévio de AMBOS e 100% do peso de H4-50 — mas isto aparece em §5–§6, enquanto §4 apresenta H3 como resultado de “redes”. Sem o gigante, H3 e H4 ficam n.d. (`sensibilidade_sem_gigante.csv`), e isso não é citado no texto.
*Solução:* uma frase ao fim de §4 e ajuste de verbo: “não se confirma compensação interna” → “não há evidência de compensação interna na rede que domina a coorte”. Acrescentar a referência ao CSV sem gigante em §5.

**P3. A significância de H2 em δ=1 é apresentada acima do que os componentes sustentam.**
O contraste −4,1 p.p. tem p=0,010, mas as categorias que o formam não sobrevivem a Holm (`faixa_b_1`: p=0,0039, **pHolm=0,0771**) e o placebo prévio é −5,0 p.p. (p=0,163), mesma direção. O slide 11 diz apenas “δ = 1: −4,1 p.p. (negativo a 5%)”.
*Solução:* qualificar em §4 e no slide 11: “o contraste combina duas categorias cujos efeitos isolados não sobrevivem a Holm; leitura sugestiva, não achado”. Uma linha, verbo ajustado.

**P4. O rótulo “gradiente por distância” contradiz o estimando declarado.**
Figura 3 chama-se “Gradiente por distância”; slide 7 chama-se “O gradiente por distância”; o texto de §4 diz, corretamente, que o contraste não identifica efeito de reduzir distância.
*Solução:* renomear figura e slide para “Heterogeneidade entre coortes de distância”. Só rótulo. Hoje o material se contradiz na manchete e no corpo.

**P5. A frase do preenchimento é circular como está escrita.**
§2: “88,8% dos vínculos adicionais já aparecem no preenchimento de outubro de 2024”. O complemento **vem** de outubro; a frase, lida literalmente, é tautológica. Pela descrição em `docs/decisoes.md` (“Erro de reconstrução”), o referente pretendido é a fotografia **mais recente** filtrada por entrada até 13/09/2024.
*Solução:* reescrever como “88,8% dos vínculos acrescentados pelo complemento também constam da fotografia mais recente com entrada até 13/09/2024”, citando `validacao_rfb.csv`.

**P6. Duas definições ainda faltam e uma contagem não é dada.**
(a) “Sem conexão” em H1: o slide 6 diz “não têm caminho a **nenhum** grupo” (δ=∞ para A e B); o relatório diz só “sem conexão”, que também poderia significar “não diretamente conectada” (δ≥1). (b) A fórmula de H3 não é dada: “variação do empenho da rede dividida pelo gasto anual médio pré-eleitoral” não diz se o numerador é nível de 2025 ou 2025 menos média pré. (c) Quantos mercados entram com participação zero (`mercados_sem_empenho.csv`) não é reportado, e essa escolha é justamente a que evita seleção pós-tratamento.
*Solução:* três frases — uma em §3 (definir “sem conexão” = δ=∞ nos dois grupos), uma em §3 com a fórmula exata de H3, uma em §4 com a contagem de mercados zerados. Nenhuma reestimação.

**P7. O placebo de nível não cobre reversão mecânica à média.**
As fornecedoras anteriores do incumbente foram favorecidas **durante** o mandato 2021–2024; parte da queda pós-eleição pode ser retorno à média, não perda de acesso. O placebo atual é de nível de participação prévia e, por construção, não detecta isso.
*Solução:* estender a H1 e H2 o placebo de **variação** (2021–2022 vs. 2023–2024) que já existe em `sensibilidade_placebo.csv` para H2, e reportá-lo no Quadro 1. Usa o pipeline existente; é o teste mais diretamente ligado à ameaça.

**P8. A comparação com Boas et al. e Baltrunaite é feita como se os regimes fossem equivalentes.**
§6 diz “contraste com retornos positivos encontrados sob doações empresariais ou em compras federais”. O regime é outro (PJ proibida desde a ADI 4650), o doador é outro (PF sócia) e a esfera é outra (municipal).
*Solução:* uma frase explicitando que o nulo é compatível tanto com ausência de transmissão via sócios quanto com doação de PF ser sinal mais fraco de vínculo — e que o desenho não separa as duas leituras.

**P9. A Figura 1 não permite recalcular δ.**
Com os rótulos atuais (δ_XA=0, δ_YA=1, δ_ZA=2), o leitor não consegue deduzir por que Y está a um passo de A: falta dizer que Carla liga X e Y e Daniel liga Y e Z, e que Ana é sócia de X e doou a A, Bruno sócio de Z e doou a B. Sendo a figura o único lugar onde o conceito de distância no bipartido é ensinado, isso é custo pedagógico real.
*Solução:* completar a legenda com essas quatro frases.

Menores, verificáveis: “p de Holm: n.d..” (ponto duplo, slide 9); o slide 8 remete a “equação 4 do projeto”, numeração que não existe no relatório (lá só há a equação 1); o teste de densidade não declara banda nem ordem do polinômio.

---

## 5. O que está claramente bom (para não parecer que só há resenha)

- A coorte “sem conexão” tem efeito estimado 0,0014 [−0,0009; 0,0037], isto é, ~0,1 p.p. com intervalo estreito. É um controle interno forte: não há choque municipal amplo na derrota, o que sustenta a leitura do contraste de H1.
- A decomposição de H3 fecha por identidade (R1+R2+R3 = total) e a compensação é reportada com a mesma banda e a mesma amostra — evita o erro clássico de comparar coeficientes de amostras distintas.
- A reinserção de fornecedores com participação zero em mercados sem empenho positivo é exatamente a decisão certa contra seleção pós-tratada, e está registrada em `docs/decisoes.md`.
- A transparência sobre o que não é estimável (n.d. com motivo em cada linha, contagens por lado, supressão de células pequenas) é acima da média da disciplina.
- O guia de fala é o melhor artefato do conjunto: 600 s exatos, papéis definidos, e instruções do tipo “não ler a tabela”, “ler o placebo antes de ler o efeito”.

---

## 6. Opcionais (não exigidos para a nota)

1. Heterogeneidade por posição na rede: grau do vértice ou k-core das fornecedoras, testando se a vantagem se concentra nas mais centrais. É o teste mais direto da previsão de Jackson-Wolinsky e usa o grafo já construído — hoje essa citação é motivacional e nada mais.
2. Variante com participação societária **ponderada** (25% vs. 100%) em vez de vínculo binário; quantificaria o custo de informação da projeção.
3. Assortatividade e coeficiente de agrupamento do componente gigante, em uma linha de texto — daria conteúdo à afirmação de que a rede “tem um núcleo”.
4. Se o formato de 12 slides for fixo, trocar o slide 9 (H4, EMD 277 p.p.) por um slide de mecanismo/heterogeneidade e mover H4 para o apêndice falado. Não é necessário: H4 já está rotulada como exploratória.

---

## 7. Arguição (4 perguntas)

**Q1 — Vínculo por administrador.** Por que compartilhar um administrador deveria transmitir vantagem política? E, se a resposta é “é proxy de coordenação”, explique por que H1 sobrevive à remoção de administradores (−0,016 [−0,156; 0,124]) mas H3 e H4 ficam sem suporte (`robustez.csv`, `sensibilidade_sem_articulacao_sementes_fixas.csv`). Espero: distinção entre remoção de vínculo (muda composição) e remoção de pessoa-ponte (fragmenta componente), e reconhecimento de que o canal administrativo é o elo conceitualmente mais frágil do grafo.

**Q2 — Sinal de δ=1.** Sob transmissão simétrica, `(β_B − β_A)/2` estima τ > 0; vocês obtêm −4,1 p.p. Por que ler isso como “sinal oposto ao previsto” e não como consequência de coortes que compartilham firmas (6,3% na direta) e diferem em mercado e porte, ainda mais com placebo prévio de −5,0 p.p. na mesma direção? Espero: aceitar que a leitura é no máximo sugestiva e apontar `h2_comparaveis.csv` como o diagnóstico relevante.

**Q3 — Poder.** O EMD de H1 é 20,7 p.p. e a média pós da coorte direta é 1,77% (DP 9,87). Que magnitude a literatura que vocês citam prevê, em pontos de participação no elemento? O que exatamente este desenho descarta e o que ele apenas não distingue? Espero: recusa de “não há efeito” e a formulação correta — descarta-se efeito grande, não efeito da ordem de 1–5 p.p.

**Q4 — O que resta de “redes” em H3/H4.** O gigante responde por 99,98% do empenho prévio de AMBOS e 100% do peso de H4-50; removido, ambas ficam n.d. O que vocês aprenderam sobre redes, e não sobre uma empresa grande? Espero: reconhecer que H3/H4 testam uma rede dominante, e que a evidência sobre “redes” como classe é o resultado nulo bem estimado das coortes distantes (δ=3+, 0,1 p.p., EMD 0,5 p.p.) — não H3.

---

## 8. Veredito

**Aprovado com distinção, nota 8,30.** Trabalho de desenho sério sobre dados próprios em escala real, com um problema de pesquisa legítimo para a disciplina e — o ponto que mais pesa a favor — um tratamento de inferência e de limitações que não tenta transformar imprecisão em achado. As revisões da R1 são reais, não cosméticas: o estimando de H2 foi reescrito, a inferência foi unificada no ponto corrigido, o preenchimento passou a ser auditado por origem e a concentração no gigante passou a ser medida nas coortes analisadas. A R1 errou ao tratar a vinculação empenho-ajuste como restrição do desfecho; essa objeção está retirada.

O teto da nota não vem das hipóteses nulas. Vem de três coisas concretas e corrigíveis sem nova rodada de estimação: um EMD que excede a média do desfecho em uma ordem de grandeza, dois resultados de rede que são, na prática, um resultado sobre uma empresa, e cerca de uma dúzia de linhas de texto que ainda prometem mais do que o estimando entrega (P3, P4, P5, P8). Com P1–P6 aplicados — todas as correções estão no escopo e usam arquivos já existentes — o trabalho sobe de faixa sem tocar em uma única estimativa.
