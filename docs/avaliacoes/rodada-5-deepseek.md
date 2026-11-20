## Notas R5

| Critério | Nota | Justificativa curta |
|---|---:|---|
| Relevância | **9,40** | Pergunta clara, política e acadêmica; RDD + rede bem posicionado; resposta nula honesta. |
| Redes | **9,30** | Grafo bipartido, componentes, articulações, distâncias e variantes são sólidos; a análise empírica é dominada por um componente. |
| Profundidade | **9,30** | CCT, correção de viés, bootstrap municipal, Holm, EMD, placebos e sensibilidades; interpretação causal bem delimitada. |
| Clareza | **9,10** | Melhorou muito, mas ainda faltam definições de estimandos centrais (rede principal, permanência, fator ½). |
| **Média** | **9,28** | R4 = 9,20. Ganho real de clareza/interpretação, insuficiente para 9,5. |

## Resolução das críticas R4

| Crítica | Status | Evidência |
|---|---|---|
| D1 placebo de nível H3 | **Resolvida** | §4 e slide 8: “ele mede nível prévio, não a variação normalizada do pós”; unidade e cautela explícitas. |
| D2 H4 médias vs saltos | **Resolvida** | §4 e slide 9: “não a diferença dessas médias nem o efeito de criar uma ligação”. |
| D3 “demais” | **Resolvida** | §4 e slide 8: só A, só B ou nenhum; gigante não excluído da principal. |
| D4 R1 interno vs contraste | **Resolvida** | Nota do Quadro 2: linhas em AMBOS = saltos internos CCT; Quadro 1 subtrai demais com bootstrap. |
| D5 variantes reclassificam | **Resolvida** | §5: “reconstroem coortes e reselecionam bandas… sem manter fixo o estimando”. |
| D6 n.d. e placebo H4 | **Resolvida** | Nota do Quadro 1 define n.d. e “Pré (nível)… inclusive em H4”. |
| D7 nível vs variação | **Resolvida** | Rótulos distintos no Quadro 1 e no slide 8 (“Δempenho / gasto anual médio prévio”). |

As observações parciais do Sol (sinal de δ=1 permanece negativo; docstring de H4; placebo por nome de coluna; Jaccard 97,44%) estão contempladas. Não há regressão visível nas estimativas principais.

## Defeitos atuais comprovados

### Corrigíveis dentro do escopo

**1. H1 ausente das sensibilidades de composição e fotografia.**
Os CSVs `sensibilidade_sem_pessoal_ou_credor_publico`, `sensibilidade_apenas_setembro`, `sensibilidade_sem_autofinanciamento` e `sensibilidade_sem_gigante` trazem apenas H2(δ=1), H3 e H4. H1 é hipótese principal, e o próprio relatório informa que pessoal/credor público soma **50,7%** do empenho de 2025 (§5). Sem H1 nessa variante, o leitor não sabe se o resultado principal sobrevive ao recorte que retira metade do gasto. **Solução:** acrescentar H1 (e H2 δ=0) às tabelas ou declarar n.d. com motivo.

**2. “Rede principal” e “permanência” não estão definidas.**
§4: “Redes principais cobrem o limiar do gasto acumulado e fornecem em três dos quatro anos”; Quadro 2: “H4 (50%) · só A”; slide 9: “probabilidade de permanência entre as principais redes”. Não se define se “rede” é componente conexa, se o limiar é percentual do gasto municipal, nem qual é exatamente o desfecho binário. **Solução:** uma frase no §3/§4: rede = componente conexa do bipartido; principal = atinge o limiar de gasto acumulado pré e fornece em 3 dos 4 anos prévios; permanência = segue acima do limiar no ranking de 2025, com entrantes incluídos. Isso também explicita o efeito mecânico dos entrantes.

**3. Fator ½ do contraste H2/H4 não justificado.**
§4: “(β̂B(d) − β̂A(d))/2”; H4 usa “a mesma meia diferença B–A”. Não há hipótese de simetria que explique a divisão por 2. Sem ela, a magnitude (“10,9 p.p.”) não tem interpretação única. **Solução:** declarar a simetria (efeito de ligação ao vencedor = +γ, ao perdedor = −γ, de modo que a meia diferença recupera γ) ou remover o ½ e renomear o contraste.

**4. Corte temporal e deflação de 2025 não declarados.**
§2 define a janela pré até setembro de 2024; §3 usa “participação em 2025”, mas não diz até que data de 2025 nem se valores são nominais ou deflacionados. **Solução:** informar a data de corte e o deflator (ou declarar nominal), como já se faz para a janela pré.

**5. Taxa de não-casamento de doadores (≈58%) não discutida.**
§2: “O cruzamento liga 41,0% dos doadores de A e 43,4% dos de B a empresas.” O relatório menciona homônimos, mas não discute seleção: os doadores não casados podem diferir sistematicamente. **Solução:** um parágrafo curto sobre seleção e, se possível, uma estatística de robustez (ex.: características observáveis dos casados vs não casados).

**6. Complemento de outubro: hipótese de continuidade não explicitada.**
§2: extração de 12/10/2024, “após a eleição, com entrada até 13/09/2024”; só se diz que “pode perder vínculos encerrados”. A data de entrada anterior à eleição é o que torna o vínculo pré-tratamento; isso deveria ser dito. **Solução:** “como a entrada é ≤ 13/09/2024, o vínculo é pré-eleitoral; a observação posterior afeta a medição, e a sensibilidade apenas-setembro dimensiona o erro.”

**7. Variante “sem administradores” também muda sementes.**
§2 diz que a ampliação operacional é “examinada na variante sem administradores”, mas não repete o alerta da Rodada 2 de que a variante altera sementes e caminhos, não só arestas. **Solução:** uma oração explicitando que a variante não isola o papel dos administradores como vínculo.

**8. Nota do Quadro 2 troca “município” por “rede”.**
“O valor-p por rede exige ao menos dez redes por lado” contradiz o Quadro 3 (“menos de dez municípios em um dos lados”) e `docs/sensibilidades.md` (“pelo menos dez municípios”). **Solução:** trocar por “municípios”.

**9. Generalização indevida em §5.**
“A remoção de pontos de articulação ou de administradores… reduz o suporte… nos contrastes indiretos e de rede (n.d.)” é falsa para “sem administradores”, cujo H2 δ=3+ é estimável (0,0004, Quadro 3). **Solução:** “nos contrastes indiretos δ=1 e δ=2 e nos de rede” ou “em quase todos”.

**10. “PC2” órfão no guia.**
`guia_de_fala.md`, slide 4: “Ligar a decisão de PC2 à robustez.” PC2 não aparece no relatório nem no deck. **Solução:** definir ou remover.

**11. Slide 6 confunde bandas com b/2 e 2b.**
“Bandas: 20,6 / 24,2 p.p.; … b/2 = 0,029; 2b = -0,007”. Os valores 20,6 e 24,2 são bandas das duas categorias (Quadro 2), não meia/dobra banda. **Solução:** rotular “bandas das categorias direta / sem conexão”.

**12. Slide 11 chama δ=3+ de “efeito pequeno”.**
O relatório é correto (“coortes quase coincidentes”, Jaccard 97,4%, “não identifica o efeito de reduzir a distância”), mas o slide diz “efeito pequeno (δ=3+)”. Com coortes 97,4% sobrepostas, a diferença pequena é quase mecânica. **Solução:** “diferença média pequena entre coortes quase coincidentes”.

**13. “23 e 78 municípios” no slide 9 não reconciliam com o Quadro 2.**
O Quadro 2 dá, para H4 50%, 26 (só A), 32 (só B), 24 (ambos) e 212 (nenhuma) municípios; `sensibilidade_gigante` dá 78 municípios em `H4_principais_50`. “23 e 78” não fecha com nenhum desses totais e pode ser observação rede–município, não município. **Solução:** corrigir o rótulo ou os números.

**14. Banda de 73,2 p.p. do H4 75% só aparece no deck.**
O deck a cita; o relatório diz apenas “bandas amplas”. Uma banda de 73,2 p.p. no eixo de margem eleitoral é quase global e muda a leitura. **Solução:** levar o número ao Quadro 1/2 ou retirá-lo do slide.

**15. Teste de densidade sem estatística e sem poder.**
“p = 0,993” é apresentado sem estatística, banda ou N efetivo. Um p tão próximo de 1 pede leitura de poder. **Solução:** reportar a estatística e uma frase sobre poder.

**16. Termos de H3 com p bruto e Holm ambíguo.**
§3: “As comparações secundárias recebem correção de Holm”; Quadro 2 traz p brutos para R1 (0,243) e R2+R3 (0,151); a nota do Quadro 1 não inclui H3 na família Holm. **Solução:** declarar que os termos de H3 são componentes de uma única decomposição pré-especificada e descritivos, não testes separados.

**17. “De maior magnitude” compara unidades diferentes.**
§4: placebo de nível de H3 é “-11,1 p.p. de participação prévia… de maior magnitude” que o pós (-4,1% do gasto). As unidades não são comparáveis. **Solução:** remover “de maior magnitude” ou dizer “em outra unidade, não comparável”.

**18. O pós de δ=1 não é comparado ao pré na mesma escala.**
A coorte B a um passo tem pré -7,68 p.p. e pós -8,07 p.p.; o líquido é ≈ -0,4 p.p., praticamente nulo. O texto diz “fragiliza”, mas não explicita que o pós é da ordem do pré. **Solução:** uma frase com os dois números e o líquido.

### Limites de dados (não corrigíveis sem outro projeto)

- **Gigante:** 99,98% do peso de AMBOS e 100% das coortes exclusivas de H4. H3/H4 não representam muitas redes independentes; sem o gigante, ficam sem suporte. Isso é limite da fotografia societária, não erro de execução.
- **Não-casamento de ≈58% dos doadores:** exige outro pareamento (CPF completo, parentesco, vínculos informais) para resolver.
- **Um ciclo eleitoral:** poder e EMD continuam limitados; mais ciclos exigiriam outro desenho.
- **H4 como teste de “redes”: ** com uma única rede dominante, H4 é, na prática, a persistência do gigante. O relatório já diz isso; não há correção dentro do escopo.

## Opcionais

- Resumo de 3–4 linhas e um parágrafo final de conclusão respondendo diretamente à pergunta da Motivação.
- Tabela de estatísticas descritivas (grau, componente, δ) no corpo, não só em CSV.
- Mover a caveat “100% do peso exclusivo é o gigante” para o parágrafo de H4 nos Resultados, não só para Robustez/Limites.
- No slide 9, liderar com “inconclusivo/não informativo” e deixar 10,9 p.p. entre parênteses.
- Verificar se o repositório citado no slide 12 está de fato público antes da apresentação.

## Veredito

**9,28/10.** O trabalho resolveu as sete críticas da R4 de forma verificável e manteve a honestidade sobre resultados nulos e fragilidades pré-eleitorais. Não chega a 9,5 porque ainda há defeitos corrigíveis que afetam a interpretação dos estimandos centrais — sobretudo a ausência de H1 nas sensibilidades de composição do gasto, a indefinição de “rede principal/permanência” e o fator ½ sem hipótese —, além de inconsistências pontuais entre deck, relatório e guia. Nenhum desses exige novos dados; todos cabem em uma revisão editorial de 5 páginas e 12 slides. Os limites que restam (gigante, não-casamento, um ciclo) são de dados e estão, em sua maioria, divulgados com transparência.
