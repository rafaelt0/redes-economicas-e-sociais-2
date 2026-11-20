# Sol — Rodada 5

Síntese do parecer independente de 20/11/2026; o integral permanece no histórico do subagente `sol_revisao_r5`.

**9,39/10**, média simples: relevância 9,65; redes 9,35; profundidade 9,30; clareza 9,25. Veredito: **apto para entrega**, com três correções de interpretação antes de sustentar nota acima de 9,50.

As críticas da R4 foram consideradas substancialmente resolvidas. O avaliador conferiu PDFs, tabelas, agregados reais, 600 segundos de guia, 203 testes e Ruff, sem alterar arquivos. Três pontos:

1. H2 indireta também é dominada pelo gigante. Nas bandas de δ=3+, ele contém mais de 99% das observações das duas coortes principais e comparáveis. O IC estreito sob reamostragem municipal não resolve dependência entre municípios da mesma rede, nem informa outros componentes. Sem o gigante, várias coortes indiretas já não têm suporte antes da escolha da banda.
2. H3 estima variações médias por rede, com peso municipal unitário por coorte antes do núcleo. O quase zero na coorte “demais”, composta de muitas redes por município, não informa estabilidade do gasto agregado da coorte. Corrigir também a unidade de H1/H2 na SPEC para empresa–município–elemento.
3. Explicitar a previsão de vantagem ao vencedor decrescente com distância sob comparabilidade e a condição de compensação R1<0/R2+R3>0. Os sinais pontuais internos de AMBOS são inversos, com ICs cruzando zero. O contraste negativo de H2 a um passo vai contra a direção prevista, mas os diagnósticos fragilizam a interpretação.

Menores: chamar contagens do slide 3 de rede principal, R2 de fornecedoras anteriores, gráfico de H1 de ajuste convencional ilustrativo, e remover a comparação de magnitude entre placebo de nível e variação pós normalizada de H3.
