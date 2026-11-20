## Nota

| Critério | Nota |
|---|---:|
| Relevância | 9,00 |
| Conceitos de redes | 8,00 |
| Profundidade/rigor | 8,20 |
| Clareza | 8,50 |
| **Geral (média igual)** | **8,43** |

Nota honesta, sem meta. A versão atual é melhor que a que recebeu 8,30 na R2: corrigiu a inferência dos contrastes, acrescentou placebo temporal real, variante com sementes fixas e corrigiu definições. O que impede 8,5+ é um erro factual de tabela e duas lacunas de discussão de robustez, não a ausência de significância.

## O que a R1 errou e não deve voltar

- **Vinculação empenho–ajuste não é o desfecho.** Os desfechos usam todos os empenhos do painel; os 3,7% de vinculação servem apenas para classificar contratos novos. A R1 tratou isso como se o desfecho fosse a fração vinculada. Não é.
- **88,8% está na direção certa.** `reconstrucao.csv`: `fracao_vinculos_extras_tambem_no_preenchimento = 0,88795`. É a fração dos vínculos reconstruídos ausentes em setembro que também aparecem no preenchimento de outubro, não o inverso.
- **Figura 1 é coerente.** Verifiquei aritmeticamente: Ana–X e doação a A ⇒ δXA=0; Bruno liga X–Y ⇒ δYA=1; Carla liga Y–Z ⇒ δZA=2; Daniel–Z e doação a B ⇒ δZB=0; δXB=2 e δYB=1. A legenda atual descreve corretamente Bruno X–Y, Carla Y–Z, Ana→A, Daniel→B. Não houve auditoria visual; a coerência é textual e aritmética.
- **O gigante não é uma empresa.** São 2.053.439 empresas (`rede_resumo.csv`). O problema relevante é a ausência de redes independentes, e isso está declarado.

## Críticas anteriores resolvidas

- **Inferência:** pontos corrigidos pelo viés em categorias e contrastes; categorias com IC CCT; contrastes com bootstrap municipal conjunto e bandas fixas; documentado como aproximação condicional, não IC CCT analítico. A crítica de “estimador convencional vs CCT” está substancialmente resolvida.
- **Composição de H2:** o texto agora diz explicitamente que `(βB−βA)/2` é heterogeneidade entre coortes, não efeito causal de reduzir distância; sobreposição de 6,3%; suporte comum com n.d. nas faixas 0–2.
- **Preenchimento de outubro:** direção corrigida, reestimação só com setembro, H2 δ=1 sem suporte declarada.
- **Gigante, articulações e suporte:** concentração de 99,98% em AMBOS/H3 e 100% em H4-50; sem gigante, H3/H4 n.d.; variante com sementes fixas separa retirada de canais de retirada de conexões políticas.
- **Universo de despesa:** 50,7% de pessoal/credor público declarado; sensibilidade sem esses gastos mantém o sinal negativo de H3 e H2 δ=1.
- **Definições:** δ formal, A/B, sementes, ranking H4, b/2, 2b, EMD, “sem conexão” como ausência de caminho a ambos. Melhorou bastante.
- **P1–P9 da R2:** a maior parte foi incorporada (semente = sócio ou administrador PF; título “empenhos municipais”; “contraste entre coortes” em vez de “gradiente”; sensibilidades no slide de H2; banda de H4-75 e denominadores; fórmula normalizada de H3; legenda da figura; distribuições transcritas; Jackson–Wolinsky como motivação; novo placebo pré-período).

## Problemas materiais remanescentes, com solução no escopo

1. **Coluna “Placebo” de H3 no Quadro 1 não bate com o CSV nem com `decisoes.md`.**
   - Quadro 1 repete `−0,1111` para H3 total, R1, R2 e R3, com p=0,130.
   - `resumo_estimacao.csv` traz placebos de contraste distintos: total `0,0798`, R1 `0,0023`, R2 `0,1261`, R3 `0,0789`, todos com p=0,130.
   - `decisoes.md` diz que o placebo de H3 é “único e repetido”.
   - **Solução:** escolher uma das três convenções e alinhar tabela, CSV e nota. Se o placebo é único, reportar o mesmo valor em todas as linhas e dizer qual é; se é por termo, usar os valores do CSV. Não muda a conclusão (p=0,130 em todas), mas é erro factual visível.

2. **Meia banda muda de sinal em H1 e H2 δ=0 e o texto não discute.**
   - H1: principal `−0,0171`; b/2 `+0,0292`; 2b `−0,0071`.
   - H2 δ=0: principal `−0,0174`; b/2 `+0,0260`; 2b `−0,0130`.
   - **Solução:** acrescentar uma frase em Resultados: “a estimativa muda de sinal em b/2, o que reforça que o intervalo largo reflete instabilidade, não um zero preciso”. É uma limitação de robustez já visível na tabela; falta interpretá-la.

3. **O contraste comparável de H2 δ=3+ tem IC estreito demais e não é explicado.**
   - `h2_comparaveis.csv`: contraste `0,000553` (0,055 p.p.), IC `[0,001; 0,109]` p.p.
   - Principal δ=3+: `0,000584` (0,058 p.p.), IC `[−0,293; 0,410]` p.p.
   - As coortes comparáveis têm ICs de cerca de 0,8 p.p.; o contraste tem 0,108 p.p., ~6–7 vezes mais estreito.
   - **Solução:** reportar no texto ou em nota o desenho pareado (município × elemento × quintil), o número de pares, a correlação/sobreposição entre as coortes e o número de réplicas válidas. Se a precisão vem de emparelhamento, dizer; se não, tratar o resultado como diagnóstico e não como evidência. Hoje o leitor não consegue reconciliar.

4. **“Sem segundo turno” aparece no deck e não no relatório nem em `decisoes.md`.**
   - Deck, slide 3: “506 municípios analisáveis, sem a capital e sem segundo turno”.
   - Relatório: só “sem a capital”; `decisoes.md` não menciona segundo turno.
   - **Solução:** acrescentar a exclusão de segundo turno à seção de dados e às limitações, com a contagem em `data/exclusoes.csv`, ou retirar a expressão do deck se não for verdadeira. O universo de 506 entre 645 municípios paulistas exige essa explicação.

5. **Unidade “23 e 78 municípios” no deck vs “redes” no relatório.**
   - Relatório: “agrupa redes com e sem ligação ao vencedor”.
   - Deck, slide 9: “82,6% ... e 81,5% ... (23 e 78 municípios)”.
   - **Solução:** usar a mesma unidade nos dois artefatos e dizer se 23/78 são redes ou municípios. Se forem redes, corrigir o deck; se forem municípios, corrigir o relatório. É inconsistência textual verificável.

6. **A Motivação destaca o resultado menos robusto.**
   - Primeira página: “O contraste a um passo (δ = 1) é negativo (-4,1 p.p.)”, sem a ressalva de que o placebo de nível é `−5,0 p.p.` (p=0,163), o placebo de variação é `−2,75 p.p.` e a sensibilidade sem autofinanciamento é `−2,85 p.p.` com IC incluindo zero.
   - **Solução:** acrescentar na própria Motivação uma oração curta: “mas esse contraste é frágil ao placebo pré-eleitoral e à exclusão do autofinanciamento”. Não é afirmação falsa, é seletividade de ênfase.

7. **Detalhes de clareza que custam pouco e rendem.**
   - “A vinculação entre empenhos e ajustes” — “ajustes” não é definido; trocar por “contratos/ajustes” ou remover.
   - “AMBOS” só aparece entre parênteses; formalizar “redes com caminho a A e a B”.
   - “Limiar central” não é definido como 50%.
   - “Cobrem o limiar do gasto acumulado” — “atingem” é mais claro.
   - EMD de H4-50 = 277,1 p.p. é maior que o intervalo do desfecho (probabilidade); dizer “EMD acima do suporte do desfecho, portanto sem informação prática”, em vez de apresentar o número como grandeza.
   - “Contagens por rede ... em `resumo_estimacao.csv`”: o CSV traz municípios tratados/controle, não redes; apontar o arquivo correto ou acrescentar as colunas.

## Limitações reais que estão honestamente tratadas

Poucos clusters, aproximação assintótica frágil, composição das coortes, preenchimento de outubro, interferência entre municípios da mesma rede, dominância do gigante em H3/H4, 50,7% de pessoal/credor público, homônimos e CPF de seis dígitos, sócios PJ como hipótese operacional, empenho ≠ contrato. Estão declaradas e não devem ser tratadas como falhas por si. A ausência de significância também não é erro. O que reduz nota são as afirmações/formatos inadequados acima, não o resultado nulo.

Não auditei código nem figuras. A validação local reportada (199 testes + lint, PDFs de 5 páginas/12 slides, guia de 600 s, réplicas comparadas com `rdrobust`) é tomada como declarada, não como verificada por mim.

## Opcionais

- Tabela de sobreposição e correlação das coortes comparáveis de H2, com número de pares e réplicas.
- Poder do teste de densidade, não só o p=0,993.
- Wild bootstrap ou inferência por randomização como diagnóstico opcional, sem alegar validade exata.
- Placebo de rede/município para H3, além do placebo de participação.
- Figura com eixos e unidades separados por painel, se ainda não estiver assim.
- Tabela descritiva de H4 com N de redes e de municípios por categoria.

## Quatro perguntas de arguição

1. O único contraste nominalmente negativo é H2 δ=1. Como vocês conciliam esse resultado com o placebo de nível de `−5,0 p.p.` e o placebo de variação de `−2,75 p.p.`, ambos na mesma direção, e com a sensibilidade sem autofinanciamento que cruza zero?
2. O que exatamente a coluna “Placebo” de H3 no Quadro 1 reporta? Por que ela repete `−0,1111` enquanto o CSV traz `0,0798`, `0,0023`, `0,1261` e `0,0789`?
3. O contraste comparável de H2 δ=3+ tem IC de `[0,001; 0,109]` p.p., muito mais estreito que o principal e que as coortes individuais. O que gera essa precisão: emparelhamento, correlação entre coortes ou sobreposição de firmas? Qual é a sobreposição?
4. O deck diz “sem segundo turno”, mas o relatório e o registro de decisões não. Quantos municípios foram excluídos por segundo turno, e como isso afeta a validade local e o poder?

## Veredito

Trabalho honesto, bem executado e dentro do escopo da disciplina. A rede é usada com conceitos adequados (bipartido, componentes, articulações, distâncias, variantes), o RDD é tratado com seriedade (correção de viés, CCT, bootstrap, densidade, placebos, EMD, Holm, sensibilidades) e os resultados nulos/imprecisos são apresentados como tais, não maquiados. Não é uma tese e não precisa ser. A nota 8,43 reflete isso: acima da R2 (8,30) pelas correções concretas, abaixo de 8,5+ por um erro factual de tabela, uma lacuna de interpretação de banda e uma inconsistência de universo entre deck e relatório. Corrigidos os itens 1–5, o trabalho fica confortavelmente em 8,5–8,6 sem mudar nenhuma conclusão.
