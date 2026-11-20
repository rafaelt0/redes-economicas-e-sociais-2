# Parecer de avaliação — EAE1429 (Redes Econômicas e Sociais)

## 1. Nota geral e notas parciais

**Nota geral: 7,4 / 10.**

| Critério | Nota | Justificativa breve |
|---|---|---|
| Relevância | **8,5** | Pergunta bem posta (o acesso ao contrato sobrevive à troca?), boa costura com captura democrática e redes de elites, desenho pré-eleitoral correto. Perde por não dialogar com a literatura brasileira de compras/corrupção e por prometer "captura" numAbstract cujos resultados são nulos imprecisos. |
| Conceitos de rede | **7,0** | Escala e engenharia impressionantes (30,6M nós, articulação, 4 variantes), mas δ nunca é definido formalmente, a projeção bipartida cria cliques, PJ como vértice-pessoa gera links espúrios e a componente gigante de 14,6% implica seleção forte em conectividade. |
| Profundidade da análise | **7,5** | Arquitetura de robustez muito acima da média (EMD, Holm, placebo, densidade, erro de reconstrução, 4 variantes). Descontado porque o placebo é do tamanho (ou maior) do efeito, o desenho é subdimensionado e a inferência muda de método entre quadros. |
| Clareza e apresentação | **6,5** | 5 páginas sobrecarregadas, `b/2` e `2b` sem definição, "Quadro" para saída de regressão, slide 10 não bate com o guia, `docs/decisoes.md` com números velhos. |
| **Ponderado (20/25/35/20)** | **7,4** | Trabalho tecnicamente ambicioso, com um resultado de manchete frágil e problemas de comparabilidade não resolvidos. |

## 2. Pontos fortes

- **Engenharia de dados de nível profissional.** 14.069.286 empresas, 16.547.513 pessoas, 24.689.604 vínculos, 8.003.121 componentes; validação de 99,72% no preenchimento 2024‑09→2024‑10 em 10,3M empresas conhecidas. Poucos trabalhos de disciplina chegam a esse nível de auditoria.
- **Diagnósticos que a maioria dos grupos esconde e vocês expõem.** O erro de reconstrução (9,4% dos vínculos de setembro fora; 21,3% dos reconstruídos ausentes em setembro, 88,8% já no preenchimento de outubro) e a nota técnica sobre a inconsistência de inferência entre Quadros 1 e 2 são exatamente o tipo de transparência que um referee valoriza.
- **Arquitetura de robustez bem pensada.** Quatro variantes (Principal, Sem articulação, Sem sócios PJ, Sem administradores), teste de densidade p = 0,993, EMD por hipótese, correção de Holm e placebos pré‑eleitorais. A célula "Sem sócios PJ: H3 total −0,0731*, R2 −0,0833*, R3 +0,0098" é informativa e honesta.
- **Snapshot de rede pré‑eleitoral (2024‑09, entradas até 13/09/2024).** Isso é um acerto de desenho: a conexão é pré‑determinada em relação à eleição de 6/10/2024, o que blinda H1–H3 contra reversão causal.
- **Boa modelagem de H2 como coortes fixas de δ** e o achado de que o contraste a 3+ passos colapsa para +0,0007 (IC [−0,0023; 0,0036]) mostram compreensão de que a vantagem de rede, se existe, deveria decair com a distância.
- **Trim around the null feito com honestidade:** a decomposição R1+R2+R3 = −0,0393 fecha aritmeticamente; o relatório não vende sinal onde não há.

## 3. Críticas e lacunas

### 3.1 Críticas sérias (conceituais, econométricas ou de identificação)

**(a) O placebo é do tamanho — ou maior — que o efeito, e isso não é tratado.** Em H3 total, placebo = −0,1132 contra estimativa −0,0393; em H2(δ=1), placebo = −0,0429 contra −0,0345; no "recorte comparável" δ=3+, placebo = +0,079 contra +0,053 (p = 0,095). Não rejeitar o placebo com ~30 clusters por lado **não é evidência de ausência de pré‑tendência**. Falta a estimativa líquida de placebo (diferença entre contraste e placebo, com IC próprio), que é o único número que sustenta ou derruba o −3,5 p.p. Como está, o sinal de δ=1 não sobrevive ao próprio diagnóstico.

**(b) O resultado de manchete é frágil a uma escolha definitional plausível.** H2(δ=1) é n.d. em "Sem administradores" e "Sem articulação" (perda de suporte < 10 municípios/lado). Ou seja: o único contraste nominalmente significativo depende de incluir administradores não sócios e de manter pontos de articulação na rede. Isso tem que estar na conclusão, não apenas no Quadro 3.

**(c) Subdimensionamento não é discutido como tal.** EMD de 14,8 p.p. em H1 é enorme. Sem média e desvio‑padrão do desfecho, o leitor não sabe se 14,8 p.p. é 3× ou 30× a média. "Estatisticamente indistinguível de zero" com essa largura é um **nulo não informativo**, não evidência de ausência de captura. A moldura do Abstract ("padrão próximo ao que Acemoglu e Robinson chamam de democracia capturada") promete mais do que o desenho entrega.

**(d) Comparabilidade das coortes de δ não está garantida.** Sobreposição mercado×porte em δ=0 de apenas 6,3% é um número alarmante. δ é correlacionado com porte, setor, grau e idade da empresa; o contraste (β_B − β_A)/2 em coortes fixas **não purga composição**. Não há tabela de balanceamento por faixa de δ, nem reweighting/matching, nem controles no local linear. O H2 é, hoje, um contraste entre populações de empresas diferentes.

**(e) Violação de SUTVA por construção do desfecho e por spillover de rede.** Se "participação no elemento em 2025" é um share que soma 1 dentro do elemento orçamentário, o ganho de uma firma é mecanicamente a perda de outra: o desfecho tem restrição de simplex e o "controle" não é controle. Além disso, o objeto de estudo *é* a externalidade de rede, então SUTVA é violada por desenho. Nada disso é discutido — e o texto cita Jackson & Wolinsky (1996) para "externalidade de doação", uso de citação que um referee de redes vai estranhar (o paper é de estabilidade par-a-par).

**(f) Erro de medida na rede sem bounding.** 21,3% dos vínculos reconstruídos ausentes em setembro e 9,4% dos vínculos de setembro fora da rede implicam erro clássico (atenuação) ou não clássico (viés de sinal desconhecido) no tratamento. Não há exercício de sensibilidade (usar só vínculos confirmados em setembro *e* outubro; ou bound à Oster). Pior: **"Vinculação empenho–ajuste: 3,7% do valor de 2025"** não é explicado. Se isso significa que só 3,7% do valor de 2025 foi casado com a base ajustada, o desfecho é medido numa fatia minúscula e selecionada, e todo o Quadro 1 está comprometido. Precisa ser resolvido antes de qualquer outra coisa.

**(g) Definições operacionais ausentes.** Nunca fica claro (i) o que é "conectada diretamente ao incumbente" — compartilhar sócio com a firma do prefeito? com doadores do partido? com o diretório?; (ii) como A e B são atribuídos e como "AMBOS" (75) entra em H2; (iii) δ é distância na projeção firma–firma (1 aresta = 1 sócio compartilhado) ou no bipartido (2 saltos)? O rótulo δ=0 "conexão direta" já é um salto no bipartido — a figura do slide 3 deveria resolver isso e não resolve. Some-se: em 2024 muitos prefeitos estão impedidos de reeleição; "M_m = margem incumbente" fica mal definido quando o incumbente não é candidato, e T=1 captura "candidato do incumbente perdeu", não "coalizão perdeu o poder" — que é o conceito de alternância.

**(h) Inferência inconsistente e não local.** Quadro 1 usa IC normal centrado na estimativa convencional com bootstrap de municípios; Quadro 2 usa CCT. O leitor compara CIs entre tabelas reportando a mesma família — não deveria. Com 14 esq./17 dir. (H3 AMBOS) e 16/17 unidades, CCT com poucos clusters é não confiável: precisa de wild cluster bootstrap ou randomization inference. E H4(75%) com **b = 73,2 p.p.** não é RDD — é comparação global disfarçada. A família de Holm não é declarada (quantos testes? H1–H4 juntos? só H4? só a coorte B de δ=1?), o que torna a correção seletiva.

### 3.2 Melhorias importantes antes da entrega

1. **Tabela de estatísticas descritivas** com média/DP de cada desfecho, participação tratada, n de municípios por lado da banda e MDE ao lado. Sem isso, EMD é ilegível.
2. **Estimativas líquidas de placebo** (efeito − placebo) com IC, e uma specification curve / multiverso para mostrar que o δ=1 não é pesca.
3. **Balanceamento por faixa de δ** (porte, setor, grau, participação pré‑2024, n de sócios) + local linear com covariáveis + reweighting; reportar o que sobra do contraste.
4. **Robustez de desfecho em níveis**: log do valor empenhado, contagem de contratos, win rate; e versão leave‑one‑out do share, para lidar com o simplex.
5. **Sensibilidade ao preenchimento**: reestimar excluindo as 2,76M empresas imputadas e reportar o quanto o δ=1 se move.
6. **Declarar o universo analisável de gasto**: 50,3% em pessoal/credores públicos e 45,5% do gasto pré‑eleitoral em credores sem sócios na RFB implicam que a análise cobre uma minoria do gasto. Isso é uma limitação central de validade externa, não nota de rodapé.
7. **H4**: rebaixar a descritivo ou excluir do teste. O contraste 40,0% vs 91,8% a 25% é artefato óbvio de composição (23 vs 78 municípios), e o "5 p.p." a 50% (82,6% vs 81,5%) não tem inferência.
8. **Diálogo com a literatura brasileira e de conexões políticas**: Ferraz & Finan (corrupção municipal), Fazekas/Broms/Dahlström (redes de favorecimento em compras), Colonnelli/Prem/Teso (patronagem), Faccio, Fisman, Khwaja & Mian (conexões políticas). A ausência é visível num trabalho sobre compras públicas brasileiras.
9. **Unificar a inferência** e declarar a família de Holm com tamanho explícito.
10. **Consertar a cadeia slide↔guia↔docs**: slide 10 mostra H1/H2(δ=0)/H3 total, mas o guia manda comentar R2/R3 em H3 sem PJ; slide 3 mostra `rede_distancias.png` enquanto o guia explica a Figura 1; slide 8 arredonda R1 para "0,000 (0,000 a 0,001)" contra +0,0004 na tabela; `docs/decisoes.md` mantém PC1 36%/37% e PC2 11,6%/1,8%.

### 3.3 Ajustes menores (redação, tabelas, slides)

- Trocar "Quadro" por "Tabela" para saídas de regressão (ABNT/IBGE reserva "Quadro" a dados não tratados estatisticamente) e incluir "Fonte:" e "Nota:".
- Definir, em nota de tabela, o que são `b/2`, `2b`, EMD (método, poder, tamanho) e a família de Holm.
- Suavizar o Abstract: o δ=1 precisa vir com "nominalmente negativo, não robusto a Holm e a placebo".
- Explicitar os 138 municípios excluídos e o critério (sem eleição competitiva? sem incumbente? sem compra? sem conexão?).
- "Sem pontos de articulação: 2,1%" — de quê? empresas, nós, municípios?
- Padronizar citações (ACEMOGLU; ROBINSON, 2008 em caixa alta; "Oliveira, Souza e Araújo, 2025" idem).
- 12 slides em 10min05s é muito: cortar para 9–10, mover slide 6 (bloco denso de diagnósticos) para backup.
- Corrigir a unidade de "+0,053 p.p." no recorte comparável e alinhar com +0,0007 do Quadro 1 (0,07 p.p.), que parecem escalas diferentes.
- Consistência de H3: o rótulo "variação de participação da rede" é, na prática, variação do empenho normalizada pelo gasto médio pré‑eleitoral. Chamar pelo nome.

## 4. Perguntas de arguição

1. **O −3,5 p.p. de δ=1 tem sinal contrário à hipótese de captura, placebo de −4,3 p.p. e desaparece quando vocês tiram administradores não sócios. Qual é o número que sobra depois de descontar o placebo, com IC, e o que ele significa economicamente?** Se a resposta é "nada", por que ele abre o Abstract?

2. **Com EMD de 14,8 p.p. em H1 e ~30 unidades por lado na banda, qual o menor efeito que vocês detectariam com 80% de poder, e como isso se compara à média da variável dependente?** Um nulo com essa largura deve ser lido como "não há captura" ou como "não sabemos"? Qual das duas leituras o relatório adota?

3. **A sobreposição mercado×porte em δ=0 é 6,3%. Como vocês sabem que (β_B − β_A)/2 mede vantagem de rede e não composição de empresas?** Mostrem a tabela de balanceamento por faixa de δ e o que acontece com o contraste após reweighting ou controles.

4. **Se "participação no elemento" é um share que soma 1, o ganho de uma firma conectada é mecanicamente a perda das demais — como isso não contamina H1–H3?** E o que exatamente significa "vinculação empenho–ajuste de 3,7% do valor de 2025": o desfecho está medido em 3,7% do gasto, e onde estão os outros 96,3%?

## 5. Veredito final

**Já está sólido e não deve ser mexido:** o pipeline de dados e a auditoria do preenchimento 2024‑09/2024‑10 (99,72%); a construção da rede em escala e a checagem de pontos de articulação; o snapshot pré‑eleitoral; a arquitetura de robustez em quatro variantes; o teste de densidade; a existência de EMD, Holm e placebos no desenho; a decomposição R1–R3 fechando aritmeticamente; a transparência sobre o erro de reconstrução e sobre a inconsistência de inferência entre quadros. Isso é um substrato acima da média e não se refaz em uma semana.

**Indispensável corrigir antes da entrega:**
1. Resolver e explicar os **3,7% de vinculação empenho–ajuste** — se for cobertura de 3,7% do valor, todo o Quadro 1 precisa ser reescrito.
2. Reportar **estimativas líquidas de placebo com IC** e reenquadrar o δ=1 como não robusto (ou retirá‑lo da manchete).
3. Incluir **média/DP do desfecho e MDE por hipótese**, e reescrever o Abstract como nulo subdimensionado, não como captura.
4. **Balanceamento por δ + reweighting/controles** no H2 (ou declarar explicitamente que o contraste é descritivo).
5. **Definir δ, A/B/AMBOS e "incumbente"** de forma operacional, com uma figura que faça o slide 3 e o guia contarem a mesma história.
6. **Unificar a inferência** (CCT + wild bootstrap/randomization inference) e declarar a família de Holm.
7. **Sincronizar** slide 10 ↔ guia ↔ `docs/decisoes.md` e corrigir o arredondamento do slide 8.

**Recomendação:** com os itens 1–7 o trabalho sobe para a faixa 8,5–9,0. Sem eles, permanece um excelente exercício de engenharia de dados e diagnóstico cercado por uma inferência que ainda não sustenta a narrativa que o título promete.
