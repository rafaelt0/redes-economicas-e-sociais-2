# Sol — Rodada 2

Síntese do parecer independente recebido em 20/11/2026. O parecer integral permanece no histórico do subagente `sol_revisao_r2` desta conversa.

**Nota geral: 8,60/10**, média simples. Relevância 9,20; redes 8,50; profundidade 8,40; clareza 8,30.

O avaliador inspecionou código, resultados, amostras renderizadas dos PDFs e agregados dos painéis reais, sem reestimar modelos. Considerou resolvidos: pontos corrigidos por viés, bootstrap conjunto com bandas fixas, validação contra rdrobust, tamanho da família de Holm, interpretação dos contrastes, sensibilidade ao complemento de outubro, diferença pós menos pré, universo de empenhos, descritivas, números de PC1/PC2, exemplo de rede e tempo do guia.

Problemas materiais identificados:

1. A definição textual de semente mencionava apenas sócio PF, enquanto o código inclui administrador PF não sócio. Corrigir e registrar ampliação operacional frente ao conceito literal de sócio.
2. A síntese de H2 enfatizava “negativo a 5%” sem levar junto o placebo, a diferença pós menos pré, a perda de suporte só com setembro/articulações e o intervalo que cruza zero sem autofinanciamento. “Firmas distantes” excedia o alcance do IC do contraste médio entre coortes.
3. O gigante domina H3 AMBOS e todas as linhas das coortes exclusivas de H4 a 50%, inclusive nas próprias bandas do RDD. Sem ele, os contrastes ficam sem suporte. Explicitar a dependência entre municípios atendidos pela mesma rede e a banda ampla de H4 a 75%.

Ajustes opcionais: retirar do guia a promessa de discutir R2 quando o slide só mostra H3 total; informar denominadores das médias de H4; informar universo eleitoral; explicar que `make all` pode ler sensibilidades existentes e invalidar os artefatos quando `leitura_sensibilidades.py` muda.

Veredito: **apto para entrega após correções focalizadas de definição e síntese**, sem necessidade de alterar o desenho principal.
