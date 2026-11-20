**Parecer RODADA 4 — EAE1429 (FEA-USP)**
Li a versão atual inteira: relatório, deck, guia de fala, `docs/` e as tabelas nomeadas. Não auditei código; tomo como declaradas as 202 testes e o lint de 56 arquivos. Não comento elementos visuais que não estão no texto ou nas legendas.

## 1. Notas

| Critério | Nota | Comentário |
|---|---:|---|
| Relevância | 9,40 | Pergunta importante, bem situada na literatura de redes, elites e compras públicas; o achado nulo/impreciso é relevante e não maquiado. |
| Redes | 9,30 | Construção bipartida, δ, componentes, articulações e concentração estão bem resolvidos; “demais” e a dupla apresentação de R1 ainda pedem uma frase. |
| Profundidade | 9,20 | Robustez ampla, placebos, EMD, Holm, auditoria H2 e diagnóstico da coorte B; falta interpretar o placebo de H3 e reconciliar H4 descritivo × RDD. |
| Clareza | 8,90 | Texto denso, mas organizado; há ambiguidades pontuais de definição, unidade e rótulo que custam leitura. |
| **Média** | **9,20** | Execução rigorosa; os problemas restantes são de apresentação/interpretação, não de método ou de dados. |

Não atribuo nota acima de 9,5. A versão atual não o justifica, embora esteja claramente acima da minha R3 (8,43), que foi deprimida por uma leitura errada de coluna.

## 2. Resolução das críticas da R3

| Crítica R3 | Status | Evidência |
|---|---|---|
| Divergência do placebo de H3 | **Retirada** | Todos os termos de H3 têm `placebo_estimativa = −0,111055741` e `placebo_p_valor = 0,130288412`; os EMDs é que diferem. Era leitura da coluna EMD como Placebo. Não há erro de dados. |
| Auditoria de comparabilidade de H2 | **Resolvida** | Jaccard 97,44% no inteiro e 84,97% nas bandas; correlação bootstrap 0,9708876; 999 réplicas válidas; EP do contraste 0,02760 p.p. contra 0,15889 p.p. com covariância zero; tabela reproduzida a 1e−12. A natureza exploratória está declarada. |
| IC nominal já na Motivação | **Resolvida** | §1 e slide 2/11. |
| Diagnóstico da coorte B (−7,68 p.p.) | **Resolvida** | §5 e slide 7, com IC nominal [−13,50; −1,86]. |
| R1 como anteriores diretamente ligadas a A | **Resolvida** | §4, Quadro 1 e slide 8. |
| Contraste AMBOS−demais vs. interno | **Parcial** | O contraste está identificado, mas “demais” não é definido e R1 aparece com dois ICs (itens D3 e D4). |
| Gigante nas bandas do RD (100%) | **Resolvida** | §5 e slide 12; `sensibilidade_gigante` mostra 1,0 em H4_exclusivas_50, H4_rdd_A_50 e H4_rdd_B_50. |
| SPEC com definições operacionais | **Resolvida** | δ, PF/PJ, administradores, fotografia e coortes estão declarados sem atribuir a ampliação ao projeto original. |
| Métodos reprodutíveis e testes | **Declarados** | 202 testes e lint de 56 arquivos; não auditados por mim nesta rodada. |
| Detalhes visuais | **Não avaliados** | Só texto e legendas. |

## 3. Defeitos atuais comprovados

### D1. O placebo de H3 não é interpretado — principal defeito restante

**Referência:** Quadro 1, H3 total: efeito `−0,04060558`; `placebo_estimativa = −0,111055741`; `placebo_p_valor = 0,130288412`. O §4 discute o placebo de H2 (δ = 1), mas não o de H3; o slide 8 também não o traz.

**Por que é defeito:** o placebo é maior em magnitude que o efeito e tem o mesmo sinal. Sem essa frase, o leitor pode ler o −4,1% como efeito eleitoral. A conclusão “sem evidência consistente” fica mais frágil do que os próprios dados permitem.

**Solução no escopo:** uma frase no §4 e um bullet no slide 8: “O placebo de H3 é −11,1% (p = 0,130), maior em magnitude que o efeito de −4,1%; o contraste não isola um efeito eleitoral.” Não muda dado, banda ou conclusão.

### D2. H4: 82,6% × 81,5% e o contraste de 10,9 p.p. não são reconciliados

**Referência:** §4, Quadro 1 e slide 9. H4 50%: efeito `0,1092146` = 10,9 p.p.; IC [−1,829393; 2,047822] = [−182,9; 204,8] p.p.; descritivas 82,6% e 81,5% (23 e 78 municípios).

**Por que é defeito:** a diferença descritiva é 1,1 p.p. e o contraste é 10,9 p.p. Sem uma frase, parece contradição. Além disso, “ligação ao vencedor” depende do resultado; o contraste é descritivo, não causal, e o texto só diz isso das taxas, não do contraste.

**Solução no escopo:** uma frase: “As taxas 82,6% e 81,5% são médias municipais incondicionais na janela de 5 p.p.; o contraste de 10,9 p.p. é o salto local corrigido entre redes de ligação exclusiva, com IC muito amplo, e não a diferença das médias. Como a condição depende do resultado, H4 é descritiva, não causal.” Opcional: notar que o EMD de 277 p.p. está acima do suporte [0,1].

### D3. “Demais” não está definido

**Referência:** §4: “Em H3, comparamos redes com caminho a ambos os grupos (AMBOS) com as demais.” Quadro 2: “H3 · demais 0,0000 [−0,0001; 0,0001].” Slide 8: “AMBOS menos demais.”

**Por que é defeito:** “demais” pode significar só-A, só-B ou nenhum. Isso muda a interpretação do contraste e do 0,0000 do controle.

**Solução no escopo:** uma frase: “Demais = redes com caminho a apenas um dos grupos ou a nenhum” — ajustando ao que foi efetivamente feito. Se o gigante for excluído nessa categoria, dizer.

### D4. R1 aparece duas vezes com o mesmo ponto e ICs diferentes

**Referência:** Quadro 1, H3 R1: `0,0003721851`, IC [−0,001218595; 0,001962965]. Quadro 2, “R1 em ambos”: `0,0004`, IC [−0,0003; 0,0010]. Slide 8 repete os dois.

**Por que é defeito:** parece inconsistência. Na verdade, um é o componente do contraste AMBOS−demais; o outro é o nível dentro de AMBOS. Como o efeito total em “demais” é ≈ 0, os pontos coincidem, mas os ICs não.

**Solução no escopo:** nota de tabela: “As linhas ‘em ambos’ usam apenas as redes AMBOS; como o efeito total em ‘demais’ é ≈ 0, os pontos coincidem com a decomposição do contraste, mas os ICs não.”

### D5. A robustez trata variantes como o mesmo estimando

**Referência:** §5 e Quadro 3: principal H3 `−0,0406`; sem sócios PJ `−0,0851*`; sem articulação e sem administradores `n.d.`. `docs/sensibilidades.md` diz que as bandas são recalculadas; o guia (slide 10) diz que “a mudança do grafo também reclassifica as coortes”.

**Por que é defeito:** comparar −4,1% com −8,5% como “robustez” pode refletir reclassificação de coortes, não efeito mais forte. O relatório não diz isso no §5.

**Solução no escopo:** uma frase: “Cada variante redefine coortes e bandas; as colunas são comparações descritivas, não o mesmo estimando.”

### D6. Notas de tabela incompletas (menor)

**Referência:** Quadro 1, H4 25% todo `n.d.`, sem definição de `n.d.` na nota; a nota diz “Placebo: participação prévia”, mas o desfecho de H4 é probabilidade de permanência, e os placebos são `0,03334056` (p = 0,8128492) e `0,06418607` (p = 0,2149442).

**Solução:** acrescentar “n.d. = não estimável por suporte insuficiente” e especificar o placebo de H4 (por exemplo, “permanência no pré-período”) ou remeter ao CSV.

### D7. Dois placebos de H2 com rótulos parecidos (menor)

**Referência:** Quadro 1, H2 δ = 1: placebo `−0,0504689` (p = 0,162992), “participação prévia”; §5: placebo de variação pré-eleitoral `−0,02753111`, IC [−0,07375598; 0,01869376].

**Por que é defeito:** são objetos diferentes, mas ambos aparecem como “placebo pré-eleitoral”. O leitor pode achar que há contradição.

**Solução:** renomear “placebo de nível pré” e “placebo de variação pré” no Quadro 1, no §5 e no slide 7.

## 4. Limites de dados que não devem ser penalizados como corrigíveis

- Sobreposição de 6,3% nas coortes diretas e `n.d.` no recorte comparável de δ = 0, 1 e 2: é falta de suporte, não erro de execução.
- Gigante com 99,98% do empenho de AMBOS e 100% do peso de H4: a comparação não representa muitas redes independentes; o relatório declara e mostra que, sem o gigante, H3/H4 ficam sem suporte.
- Um ciclo eleitoral, doações só de PF, preenchimento de outubro e vinculação de 3,7% a contratos: são limites de medida e de desenho. Superá-los exigiria outro projeto, não outra rodada.
- A imprecisão dos efeitos não é falha: o trabalho reporta IC, EMD e suporte, e não transforma não rejeição em ausência de efeito.

## 5. Opcionais

- Incluir uma linha com as estimativas da sensibilidade “sem pessoal ou credor público” (H2 δ = 1: −4,16 p.p.; H3 total: −7,50%; H4: n.d.) ou remeter ao CSV. O recorte existe; hoje o texto só informa a participação de 50,7%.
- Explicitar por que δ = 1 é o “contraste principal” de H2 (pré-especificação) ou chamá-lo de “contraste de interesse”. Sem isso, o rótulo “principal” pode parecer escolha ex post.
- Nomear a tabela que gera a sobreposição de 6,3% nas coortes diretas.
- Ajustar “as conexões passam por pessoas físicas” para “as doações diretas passam por PF; o grafo pode incluir sócios PJ”, pois o próprio texto inclui PJ no bipartido.

## 6. Veredito

**9,20/10.** A versão é rigorosa, honesta e corrige as críticas da R3. A alegação de divergência do placebo de H3 era leitura da coluna EMD como Placebo e está retirada; os números conferem por nome de coluna. A auditoria de H2, o diagnóstico da coorte B, a definição de R1, o contraste AMBOS−demais, a dominância do gigante nas bandas do RD e a SPEC são correções reais.

Os defeitos que restam são de apresentação e interpretação — sobretudo D1 (placebo de H3), D2 (H4 descritivo × RDD), D3 (“demais”) e D4 (R1 com dois ICs) — e todos se resolvem com frases, sem novos dados, novo desenho ou nova significância. Com D1–D5, o patamar 9,4–9,5 passa a ser defensável. Acima de 9,5 exigiria eliminar as ambiguidades, não mudar o projeto. Sem esses ajustes, **9,20 é a nota honesta**.
