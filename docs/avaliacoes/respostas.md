# Respostas aos pareceres

Revisão iniciada em 20/11/2026, a pedido do usuário. As novas avaliações usam somente Sol e DeepSeek. Os pareceres originais estão preservados nesta pasta; notas de modelos são avaliações simuladas, não notas da disciplina.

## Rodada 1

| Questão | Resposta e evidência |
|---|---|
| Inferência diferente nos quadros | Corrigir o ponto de todas as estimativas pelo viés. As categorias mantêm IC CCT; contrastes usam EP de bootstrap municipal conjunto do ponto corrigido, com bandas fixas. Não são métodos idênticos, mas passam a usar o mesmo estimador pontual. Testes confrontam pontos e réplicas com `rdrobust`; as limitações com poucos municípios são explícitas. |
| H2 confundia distância e efeito causal | Explicitar `(beta_B(d) - beta_A(d))/2`, sobreposição de firmas e composição diferente. O contraste é heterogeneidade dos efeitos eleitorais entre coortes, não intervenção na distância. Manter diagnóstico por mercado/porte e reportar falta de suporte. |
| Placebos e sinais frágeis | Tratar participação prévia como diagnóstico de continuidade, não pré-tendência. Não deduzir balanço de não rejeição. Não aplicar uma subtração automática como solução de identificação. A sensibilidade com variação pós menos pré recalcula a covariância e tem interpretação condicional própria. |
| Preenchimento de outubro | Explicitar observação posterior à eleição e hipótese de continuidade do erro no corte. Reestimar só com setembro, preservando os fornecedores sem vínculo e os denominadores. A taxa de concordância nas firmas observadas não valida as ausentes. |
| Gigante e filtros de rede | Medir concentração nas coortes analisadas, não apenas na rede nacional; verificar remoção do gigante e de articulações. Distinguir remoção de pontes de exclusão de sementes diretamente ligadas. |
| Universo de despesa | Todos os empenhos do painel entram nos desfechos. A vinculação com ajustes serve à classificação de contratos novos e não reduz o desfecho à fração vinculada. Auditar pessoal e credores públicos; publicar recorte como sensibilidade, sem alterar silenciosamente o desenho principal. |
| Conceitos e definições | Definir formalmente delta no bipartido, PF/PJ e administradores, A/B e AMBOS, ranking acumulado de H4 e inclusão de entrantes. PJ como vértice na camada de vínculos é hipótese operacional explícita, com variante sem PJ; não equivale a pessoa física doadora. |
| Dependência e interferência | O tratamento é municipal. Shares e competição geram dependência dentro do município, tratada pelo agrupamento; não se exige independência entre firmas do mesmo município. Redes entre municípios podem violar ausência de interferência; essa limitação permanece. |
| Poder e bandas | Reportar EMD, escala do desfecho, suporte e largura das bandas. Uma banda ampla e poucos municípios limitam a leitura local e a aproximação assintótica. Não mudar banda ou retirar H4 para buscar significância. |
| Clareza e sincronização | Corrigir números históricos de PC1/PC2; mostrar exemplo no slide 3; quatro casas em H3; dez minutos de guia; explicitar unidades e distinção entre médias descritivas e contrastes. |

## Recomendações que não se tornam requisitos do desenho

- Wild bootstrap ou inferência por randomização não produzem validade exata sem hipóteses adicionais. O trabalho reporta a aproximação usada e seus limites, sem alegar resolver pequeno número de municípios.
- Adicionar ciclos eleitorais, uma extensa bateria de controles ou substituir empenhos por contratos exige outro desenho e fontes. Essas extensões não são necessárias para reportar honestamente os resultados deste projeto.
- Preservamos o termo “Quadro” e o número de slides definidos pelo projeto. As preferências gerais de um parecerista não substituem as instruções do trabalho.
- A referência a Jackson e Wolinsky motiva externalidades em redes; não é usada como prova empírica de que a vantagem de uma doação se transmite.

Os resultados e a conclusão devem acompanhar os CSVs reestimados. Eventuais achados que desaparecerem com a correção continuam registrados na Rodada 1 e não serão apresentados como evidência atual.

## Rodada 2

Sol: **8,60/10**. DeepSeek: **8,30/10**. Sol leu arquivos, código e agregados locais; DeepSeek avaliou um pacote transcrito de textos e tabelas, sem acesso visual nem auditoria independente do código. A distinção de acesso deve acompanhar a comparação das notas.

- Corrigimos a definição de semente para sócio **ou administrador** PF e documentamos a ampliação operacional. A variante sem administradores não isola apenas caminhos, pois também muda sementes.
- O título agora se refere a empenhos municipais, de acordo com o universo efetivamente analisado.
- Substituímos a manchete “gradiente” por “contrastes entre coortes de distância”. O alcance do IC de δ=3+ se refere ao contraste médio entre coortes, sem restringir efeitos individuais.
- As sensibilidades pós menos pré e sem autofinanciamento aparecem no slide de H2; fotografia e suporte acompanham o slide de síntese. A família principal e os testes isolados com Holm são distintos; não condicionamos a validade de um contraste pré-especificado à rejeição dos componentes separados.
- A exclusão do gigante, sem suporte para H3/H4, aparece no relatório e no slide de limites. A amplitude da banda de H4 a 75% e os denominadores das médias descritivas são explícitos.
- O relatório dá a fórmula normalizada de H3, define sem conexão como ausência de caminho a ambos os grupos e dimensiona o EMD frente à média do desfecho. A classificação do gasto não confunde empenhos e ajustes.
- Esclarecemos a direção do diagnóstico de reconstrução: 88,8% dos vínculos **reconstruídos recentemente e ausentes da referência de setembro** aparecem também no complemento de outubro de 2024. A reescrita sugerida pelo DeepSeek invertia esse denominador e não foi adotada.
- A legenda da figura explicita a cadeia correta: Bruno liga X–Y, Carla liga Y–Z, Ana doa a A e Daniel doa a B. A descrição sugerida pelo DeepSeek trocava as pessoas da figura, que não estava visível no pacote transcrito. Não alteramos o grafo para corresponder à descrição equivocada.
- Um componente gigante contém muitas empresas: não equivale a “uma empresa”, expressão usada no segundo parecer DeepSeek. O problema relevante é a falta de redes independentes, que mantemos como limitação.
- O trabalho já publica distribuição de graus, tamanho de componentes, distâncias, articulações e erro de reconstrução. δ não é sua única medida estrutural. A citação de Jackson e Wolinsky é motivacional, sem alegar testar estabilidade par a par ou inferir intensidade de participação societária não observada.
- O novo placebo de variação entre duas janelas pré-eleitorais examina uma ameaça distinta do contraste pós menos pré. Não renomeamos o diagnóstico existente como se já fosse um teste temporal anterior à eleição.

As novas rodadas devem avaliar essas correções concretas; não se alteram bandas, amostras principais ou conclusões para obter uma nota maior.

## Rodada 3

Sol: **9,05/10**, com nova verificação local de testes, código, agregados e PDFs. DeepSeek: **8,43/10**, com leitura de transcrição. Correções realizadas: síntese nominal de H2 já na Motivação; diagnóstico temporal da categoria B; R1 como fornecedoras anteriores diretamente ligadas a A; identificação do contraste AMBOS−demais no slide H3; elegibilidade apenas pré em H4; atualização da SPEC; meias bandas com inversão de sinal discutidas; ausência de segundo turno e médias municipais de H4 explícitas; dominância também nas bandas efetivas do RD publicada no CSV e nos artefatos. A contribuição estrutural da concentração aparece agora já na Motivação.

### Verificação das alegações de erro do DeepSeek

O parecer transcrito leu campos incorretos em algumas linhas largas de CSV. Conferência por **nome de coluna**, e não por posição:

| Fonte | Campo | Valor |
|---|---|---:|
| resumo_estimacao.csv, H3 total, contraste | placebo_estimativa | −0,11105574116440625 |
| mesma linha | placebo_p_valor | 0,1302884124847543 |
| mesma linha | emd | 0,08777496625272924 |
| H3 R1, contraste | placebo_estimativa | −0,11105574116440625 |
| mesma linha | emd | 0,002273870797677289 |
| H3 R2, contraste | placebo_estimativa | −0,11105574116440625 |
| mesma linha | emd | 0,12605157333077263 |
| H3 R3, contraste | placebo_estimativa | −0,11105574116440625 |
| mesma linha | emd | 0,07888406567362996 |

Portanto, o placebo único repetido de H3 **já coincide** entre relatório, CSV e nota. Não alteramos dados corretos para corresponder à leitura incorreta. O CSV de resumo também contém `redes_tratadas` e `redes_controle`; sua ausência em uma transcrição com colunas redundantes omitidas não constitui ausência no arquivo publicado. A nova rodada deve usar tabelas com campos nomeados para reduzir esse risco de leitura.

A unidade da tabela de permanência é `n_municipios`, e a taxa é uma média municipal por condição de vínculo. A redação foi uniformizada, sem trocar municípios por redes. A auditoria do recorte comparável quantifica sobreposição e covariância para explicar a precisão da diferença, sem alterar seu estimador nem a conclusão de que se trata de sensibilidade exploratória.

## Rodada 4

DeepSeek: **9,20/10**. Sol foi interrompido pelo limite do provedor antes de dar nota. A falta de nota não é aprovação. Foram aplicadas as observações parciais do Sol sobre precisão versus sinal em H2 e sobre a interpretação do contraste de H4.

- O placebo de **nível** de H3 aparece no texto e no slide correspondente, com unidade e cautela: não é o mesmo desfecho da variação normalizada pós. Não rejeitar o placebo impreciso não confirma continuidade.
- “Demais” inclui redes com caminho a apenas um grupo ou a nenhum; o gigante não é retirado dessa categoria na especificação principal. A exclusão é uma sensibilidade separada.
- R1 interno em AMBOS é um salto estimado só nessa coorte, com IC CCT. R1 do contraste subtrai o salto nas demais redes, com IC bootstrap. Proximidade dos pontos não exige igualdade dos intervalos.
- As médias municipais de H4 na janela e a meia diferença de saltos no corte usam populações, pesos e bandas diferentes. Não são estimadores da mesma diferença. O contraste não identifica o efeito causal de criar uma ligação. Mantemos a distinção: o tratamento eleitoral é a derrota do incumbente em coortes pré-fixadas; o fato de o rótulo “vencedor” depender do resultado não invalida por si só o RD nessas coortes.
- Cada variante da rede pode reclassificar coortes e escolhe novas bandas. As comparações não mantêm fixo um único estimando em amostra invariável.
- A nota do Quadro 1 define n.d. e especifica participação anterior como placebo de nível, **inclusive em H4**. Não adotamos a sugestão de chamá-lo de permanência prévia, pois esse não é o desfecho efetivamente usado pelo código.

Todas as correções são de definição, interpretação ou apresentação; as estimativas principais não foram alteradas nessas rodadas editoriais.

## Rodada 5

Sol: **9,39/10**; DeepSeek: **9,28/10**. A rodada levou a uma nova auditoria de concentração de H2, com script, testes e limites agregados que preservam a supressão. O IC estreito das coortes 3+ agora é apresentado como condicional à inferência municipal em amostras dominadas pelo gigante, sem generalização para outros componentes. A discussão distingue explicitamente essa precisão da dependência entre municípios.

H3 passou a definir unidade rede–município, peso municipal unitário por coorte antes do núcleo e interpretação como média por rede, sem confundir com gasto agregado. R1/R2/R3 são confrontados com a condição de compensação e H2 com a previsão sob comparabilidade, sem impor causalidade à distância. A SPEC corrige H1/H2 para empresa–município–elemento.

Também foram explicitados: ano de 2025 completo em valores nominais; rede como componente; principal como prefixo do ranking de empenho municipal pré e permanência como inclusão no prefixo de 2025 com entrantes; meia diferença como normalização, com interpretação de vantagem comum apenas sob simetria e comparabilidade adicionais; erro de sobrevivência do complemento de outubro; alteração conjunta de sementes/caminhos sem administradores; alcance parcial do cruzamento de doadores. Não-casamento não é automaticamente erro de pareamento: pode indicar ausência de vínculo formal em empresa.

### Pontos do DeepSeek que exigiram conferir a fonte

- H1 e H2 direto **já estão** nas sensibilidades de fotografia, autofinanciamento e escopo do gasto. A alegação de ausência veio de um extrato que selecionava apenas linhas de interesse de H2/H3/H4. Para H1, o CSV apenas-setembro tem −0,0179681168, IC [−0,2154023605; 0,1794661269]; sem autofinanciamento −0,0116543016, IC [−0,1554935246; 0,1321849214]; sem pessoal/credor público −0,0131427248, IC [−0,1569939136; 0,1307084640]. Os arquivos não foram modificados para essa correção de leitura.
- O mínimo de municípios para estimar RD e o mínimo adicional de redes para testar agrupamento por rede são critérios distintos. Não trocamos “dez redes” por “dez municípios”: ambos constam do código e da nota, cada qual para seu propósito.
- As médias municipais 23/78 na janela de cinco p.p. não devem somar as contagens por coorte nas bandas do RD. As populações, bandas e grupos são diferentes; um município pode contribuir às duas condições de vínculo. `permanencia_h4.csv` registra `n_municipios`, não número de redes.
- Não subtraímos a mudança temporal pré-eleitoral da categoria B de seu nível pós para chamá-la de efeito “líquido”. São desfechos distintos; a proximidade das magnitudes é diagnóstico, não correção automática de viés. O contraste pós menos nível pré já é estimado separadamente, com covariância apropriada e interpretação cautelosa.
- Removemos “maior magnitude” na comparação de H3 e mantivemos apenas o sinal comum e a distinção de desfechos. Precisão, sinal e interpretação são apresentados separadamente.

Os próximos pacotes de avaliação devem identificar explicitamente extratos de tabelas e fornecer as linhas de H1 das sensibilidades, evitando inferir ausência nos arquivos pela ausência numa seleção.

## Rodada 6

Sol: **9,56/10**; DeepSeek: **9,33/10**. Sol reproduziu as 36 linhas da auditoria de concentração; DeepSeek conferiu textos e extratos nomeados, sem inspeção visual nem auditoria do código.

- Corrigimos a colisão de notação: a interação do RD usa θ; δ continua a designar distância de rede.
- O Quadro 3 e o slide 10 usam `robustez.csv`, com sementes **reselecionadas** após remover articulações. A sensibilidade adicional com sementes **fixas** é outro exercício, publicado em `sensibilidade_sem_articulacao_sementes_fixas.csv`. As notas agora distinguem as duas variantes. A diferença apontada não era erro nos valores da tabela: eram duas especificações diferentes com rotulagem insuficiente. O Quadro 3 reproduz −0,0150 (H1), −0,0020 (H2 direto) e n.d. (H2 3+) de `robustez.csv`; com sementes fixas, os valores são −0,0167201, −0,01736785 e 0,002214778, respectivamente. O direto coincide com o principal por construção. Nenhum CSV foi substituído ou ajustado para igualar os exercícios.
- H1–H3 têm inferência nominal, sem garantia conjunta de controle do erro familiar. Não alegamos pré-registro formal. O cálculo de 37% do parecer assume nove testes independentes; os contrastes dependem das mesmas unidades e H3 é aditivo, de modo que esse número não é uma taxa calculada para este projeto.
- Ausência de caminho às sementes de A e B não implica isolamento societário: pode haver componentes com várias empresas sem doador elegível. Mantivemos a definição correta de H1; não adotamos o rótulo “firma isolada” sugerido no parecer.
- A análise pós menos pré estima a mudança entre níveis de participação nas janelas correspondentes. Não subtrai o diagnóstico de **mudança entre dois períodos pré-eleitorais** do nível pós. O texto agora explicita essa diferença, além de não lhe atribuir correção causal automática.
- H3 inclui redes com fornecedoras anteriores no município; R3 conta entrantes dessas redes. O texto usa médias das redes com peso municipal unitário e mantém a distinção de gasto agregado no deck. A exclusão de pessoal/credor público agora acompanha os resultados: H1 e H3 total com IC cruzando zero; H2 a um passo negativa com IC nominal fora de zero.
- O slide 3 nomeia os vértices de sócios/administradores PF/PJ. O slide 4 usa escala linear de 0% a 100%, rótulos nas barras e distingue participação das empresas de participação dos componentes. O rodapé do slide 8 identifica AMBOS como a coorte dominada por uma rede. O guia confronta o sinal de H2 com a previsão sob comparabilidade.

Verificação após os ajustes: 208 testes passam e Ruff aprova 58 arquivos. O relatório mantém cinco páginas, o deck 12 slides nos dois formatos, e o guia 600 segundos. As estimativas principais permanecem inalteradas.

## Rodada 7

O primeiro parecer do Sol deu **9,63/10** (relevância 9,65; redes 9,70; profundidade 9,62; clareza 9,55). A conferência visual e a reconversão independente do PPTX confirmaram a consistência dos formatos. A redação explicita a exclusão de empenhos de pessoal ou credor público, o RD da diferença de participação pós menos pré e a falta de evidência de compensação em R3. Relatório e deck recompilados, com 15 testes focados e lint aprovados. O usuário informou que a execução apareceu em Low. Para a meta, vale a avaliação em High da rodada seguinte.

Na reexecução, o DeepSeek deu **9,55/10** (relevância 9,60; redes 9,60; profundidade 9,55; clareza 9,45) e considerou a entrega apta. Conferiu a distinção entre as duas variantes de articulação, a notação da equação e os valores dos quadros e sensibilidades. A revisão foi textual. No parecer, os 99,98% da coorte AMBOS se referem ao empenho prévio. A fração exata do peso municipal continua suprimida no CSV para proteger contagens pequenas.

## Rodada 8 — Sol em High

O [novo parecer do Sol](rodada-8-sol-high.md), enviado com `reasoningEffort: high` no T3, deu **9,60/10** (relevância 9,7, redes 9,8, profundidade 9,6 e clareza 9,3) e considerou o trabalho apto. O Sol revisou os mesmos artefatos enviados ao DeepSeek. As duas médias superaram 9,5.

Após os pareceres, explicitamos o denominador municipal de H3, o fornecimento em pelo menos três dos quatro anos pré-eleitorais para H4 e a unidade do placebo no slide 6. Os CSVs de resultados coincidem com os da versão avaliada. O relatório tem cinco páginas, o deck tem 12 slides no PDF e no PPTX, e o guia soma 600 segundos. Os 15 testes focados e o lint passaram, e a renderização dos slides editados foi conferida.
