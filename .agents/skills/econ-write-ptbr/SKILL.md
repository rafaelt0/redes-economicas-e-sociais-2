---
name: econ-write-ptbr
description: >-
  Guia de redação e revisão em economia aplicada (PT-BR) adaptado ao projeto
  "Redes empresariais e persistência econômica sob alternância política"
  (EAE1429, FEA-USP). Sintetiza os princípios de Cochrane, McCloskey, Shapiro,
  Head, Bellemare, Goldin & Katz, Kremer e Schwabish (baseados em
  hanlulong/econ-writing-skill) que se aplicam a relatório curto em LaTeX/ABNT
  (<= 5 páginas), deck de 10 minutos e guia de fala, com reporte de RDD,
  resultados nulos/imprecisos e números exclusivamente via macros.
---

# Escrita em Economia Aplicada (PT-BR) — Projeto EAE1429

Use esta skill ao redigir, enxugar ou revisar textos em português do relatório
(`report/relatorio.tex`), das macros narrativas (`src/redes/report.py`), dos
slides e do guia de fala (`src/redes/deck.py`, `output/guia_de_fala.md`).

> **Regra de precedência:** `docs/projeto.pdf` e `SPEC.md` prevalecem sobre
> qualquer regra geral de artigo de periódico. Nunca expanda o relatório para
> formato de *working paper* longo nem troque o padrão ABNT por `natbib`.

---

## 1. Limites invioláveis deste projeto

1. **Teto de 5 páginas** no relatório (`MAXIMO_PAGINAS = 5` em `src/redes/report.py`),
   mantendo o estilo visual de `docs/projeto.pdf` e citações ABNT (`abntex2cite`).
2. **Zero números digitados à mão:** toda estimativa, IC, banda, contagem, taxa
   ou valor-p vem de `results/tables/*.csv` via `numeros.tex` / `src/redes/report.py`
   e `src/redes/deck.py`. Se o CSV mudar, o texto e a conclusão devem atualizar
   sozinhos.
3. **Formatação brasileira consistente:**
   - Vírgula decimal (`14,8 p.p.`, `-0,011`); em modo matemático LaTeX, usar
     chaves na vírgula (`$p = 0{,}993$`) para evitar espaço espúrio.
   - Sem espaço antes de `%` (`-3,9%`, `82,6%`).
   - Siglas em português: **EMD** (efeito mínimo detectável), **p.p.** (pontos
     percentuais), **IC** (intervalo de confiança), **n.d.** (não disponível /
     suporte insuficiente).
4. **Sigilo e transparência:** células com menos de 5 unidades ficam suprimidas;
   nenhum nome, CPF ou CNPJ identificável entra nos textos ou figuras; todo
   desvio de desenho precisa estar em `docs/decisoes.md`.
5. **Fidelidade empírica:** reportar resultados nulos, negativos ou inconclusivos
   exatamente como saem, sem ajustar especificação nem exagerar inferências.

---

## 2. Princípios centrais (Cochrane, McCloskey, Shapiro, Goldin & Katz)

- **Leitor primeiro:** escreva para economistas ocupados que escaneiam o texto.
  O argumento central precisa ficar claro na primeira leitura.
- **Estilo triangular (pirâmide invertida):** diga o que o estudo **encontra**
  logo na seção 1 (Motivação) e no slide 2 do deck — nunca esconda o resultado
  para o último parágrafo como se fosse um romance policial.
- **Concretude, não abstração:** prefira magnitudes com unidade econômica
  (`-1,1 p.p.; EMD de 14,8 p.p.`) a frases vazias ("analisamos os dados e
  encontramos padrões interessantes").
- **Voz ativa e tempo presente:** use "combinamos", "comparamos", "estimamos",
  "os dados mostram" (nosso grupo em primeira pessoa do plural) e presente ao
  citar a literatura ("Boas, Hidalgo e Richardson (2014) mostram que...").
  Reserve a voz passiva para descrições de procedimento onde o agente não
  importa ou notas de quadros.
- **Economia verbal:** corte toda palavra ou frase que não carregue informação.
  Evite "aquecimento de garganta" na abertura de parágrafos ("A literatura há
  muito se interessa por...", "Vale ressaltar que...", "É importante notar que...").
- **Simplicidade:** prefira palavras diretas ("usar" em vez de "utilizar",
  "vários" em vez de "diversos", "pessoas" em vez de "agentes", "mostra" em vez
  de "evidencia de maneira robusta").

---

## 3. Escrita e reporte de Regressão Descontínua (RDD)

Ao descrever o desenho e os resultados de RDD:

1. **Comece pela variável de corte e pelo limiar:** defina $M_m$ (margem em
   p.p.) e $T_m = \mathbf{1}(M_m < 0)$ em linguagem direta antes da equação.
2. **Explicite a hipótese de identificação e a validade local:** sob
   continuidade dos resultados potenciais em $M_m = 0$, vitórias e derrotas
   apertadas são localmente comparáveis. Deixe claro que o estimador identifica
   o **efeito local no corte** (eleições apertadas), não o efeito médio em
   disputas folgadas.
3. **Separe o que é identificado do que é hipótese:** o desenho identifica o
   efeito causal da derrota/vitória eleitoral sobre a alocação; a transmissão
   da vantagem pela rede societária é examinada como hipótese.
4. **Reporte sempre o pacote completo de credibilidade:**
   - estimador local linear com núcleo triangular, banda MSE-ótima e ICs
     robustos corrigidos pelo viés (Calonico, Cattaneo e Titiunik, 2014);
   - teste de densidade / manipulação no corte (Cattaneo, Jansson e Ma, 2020);
   - sensibilidade à janela ($b/2$ e $2b$) e contagem de municípios de cada lado;
   - placebos com desfechos pré-eleitorais (2021–2024);
   - agrupamento de erros-padrão no nível do tratamento (município) e comparação
     por rede;
   - quando um placebo aponta na mesma direção do efeito ou fica próximo de
     10%, sinalize explicitamente cautela na leitura.

---

## 4. Resultados nulos, imprecisos e múltiplos testes

- **Um resultado nulo é um resultado informativo**, não um fracasso.
- **Distinga sempre *imprecisão* de *zero preciso*:**
  - *Impreciso:* intervalo de confiança largo e EMD elevado que incluem tanto
    zero quanto efeitos economicamente relevantes — **não** diga "não há efeito";
    diga que os dados não permitem descartar efeitos relevantes.
  - *Zero preciso:* intervalo estreito e EMD pequeno (ex.: empresas distantes
    $\delta = 3+$) — aqui é correto afirmar que os dados restringem o efeito a
    magnitudes pequenas.
- **Significância econômica acima de asteriscos:** traduza estimativas para
  unidades interpretáveis (p.p. de participação no elemento de despesa, % do
  gasto anual médio pré-eleitoral, probabilidade de permanência) e reporte ICs
  e EMDs junto com estimativas pontuais.
- **Múltiplos testes:** declare explicitamente quais hipóteses são principais
  (H1–H3) e quais recebem correção de Holm (H4 e categorias secundárias); em
  H4, baseie a leitura no p-valor ajustado, não no bruto.
- **Diálogo honesto com a literatura:** explique como o achado (ou a ausência
  de ganho claro) se posiciona frente a estudos próximos (ex.: doações
  individuais de sócios pós-ADI 4650 em um único ciclo municipal vs. doações
  empresariais ou compras federais em Boas et al., 2014 e Baltrunaite, 2020).

---

## 5. Quadros, figuras e robustez

- **Legendas e notas autossuficientes (padrão ABNT: título acima, fonte/nota
  abaixo):** o leitor deve conseguir interpretar o quadro sem caçar definições
  no corpo do texto. Sempre informe:
  - unidade da variável dependente;
  - tipo e nível do IC (ex.: IC de 95% por reamostragem de municípios vs. IC
    robusto CCT corrigido pelo viés);
  - significado de colunas abreviadas (`Esq.`/`Dir.`, `EMD`, `$p_{pl}$`, `n.d.`);
  - motivo de células `n.d.` (ex.: suporte menor que 10 municípios de um lado).
- **Robustez comentada, não apenas tabelada:** toda tabela de robustez precisa
  de um parágrafo curto que diga (i) o que permanece estável nas quatro
  variantes, (ii) onde o sinal ou a significância mudam (ex.: `sem sócios PJ`),
  e (iii) por que surgem `n.d.` (fragmentação de componentes reduzindo o
  suporte municipal).
- **Figuras (princípio de Schwabish/Tufte):** minimize tinta não-dado, prefira
  rótulos diretos quando possível e explique na nota da figura a unidade do
  eixo e o que representam as barras de erro.

---

## 6. Apresentação (deck e guia de fala)

- **Ritmo de 10 minutos (10 a 12 slides, 4 pessoas):** chegue à pergunta e ao
  achado central nos 2 primeiros slides; evite slides de "revisão de literatura"
  longa.
- **Unidade explícita em todo slide empírico:** cada slide de H1–H4 deve deixar
  clara a unidade do resultado e a distinção entre imprecisão e efeito pequeno.
- **Slide de síntese (slide 11) ancorado nos resultados:** resuma os achados
  reais das quatro hipóteses com magnitudes e EMD, em vez de repetir a
  definição genérica de cada hipótese.
- **Guia de fala:** tópicos curtos (o que precisa ser dito), nunca texto
  corrido para leitura em voz alta. Nunca leia a tabela célula por célula:
  aponte direção, magnitude, precisão e estabilidade.

---

## 7. Padrões anti-IA em português (PT-BR)

Evite marcas típicas de texto gerado por IA em português:

- **Palavras e muletas a evitar:** "mergulhar", "panorama", "cenário complexo",
  "multifacetado", "crucial", "fundamental" (em excesso), "robusto" fora de seu
  sentido estatístico/econométrico, "abrangente", "alavancar", "lançar luz
  sobre", "pavimentar o caminho", "fator determinante", "desempenhar um papel
  central", "vale ressaltar que", "cabe destacar que", "nesse sentido",
  "diante disso", "adicionalmente", "outrossim".
- **Estruturas mecânicas a evitar:**
  - contrastes formuláicos repetitivos ("não se trata apenas de X, mas sim de Y");
  - frases todas com o mesmo comprimento médio (alterne frases curtas de
    8–12 palavras com períodos mais longos de 15–25 palavras);
  - tríades forçadas em todo parágrafo ("clareza, precisão e profundidade");
  - conclusões em tom de comunicado corporativo em vez de reflexão analítica.
- **Prefira:** vocabulário natural de economia aplicada em português
  (empenho líquido, elemento de despesa, margem eleitoral, efeito local no
  corte, suporte municipal, erro de cruzamento), especificidade institucional
  (TCESP, TSE, Receita Federal, ADI 4650) e ressalvas calibradas.

---

## 8. Checklist rápido de revisão (3 olhares)

Antes de fechar uma revisão do relatório ou do deck, confira:

1. **Metodologista (RDD e redes):**
   - [ ] Variável de corte, hipótese de continuidade e validade local explícitas?
   - [ ] Densidade, $b/2$, $2b$, placebos pré-eleitorais, agrupamento e EMD reportados?
   - [ ] Nulos distinguem imprecisão (EMD alto) de efeito pequeno (EMD baixo)?
   - [ ] Células `n.d.` e mudanças na robustez explicadas com honestidade?
2. **Economista de campo (economia política e compras públicas):**
   - [ ] Achado central aparece já na Seção 1 e no Slide 2?
   - [ ] Magnitudes traduzidas em unidades econômicas (p.p., % do gasto prévio)?
   - [ ] Posicionamento justo frente a Boas et al. (2014), Baltrunaite (2020),
         Acemoglu e Robinson (2008), Akhtari et al. (2022)?
   - [ ] Limites de medida (doação individual, homônimos, empenho vs. contrato)
         claros, sem exagerar conclusões?
3. **Revisor de clareza e integridade técnica (PT-BR / LaTeX):**
   - [ ] Nenhum número de resultado digitado à mão em `report/relatorio.tex`?
   - [ ] Padrão PT-BR respeitado (`0{,}993` em math mode, sem espaço antes de `%`,
         `EMD` em vez de `MDE`, sem muletas de IA)?
   - [ ] Quadros e figuras com notas ABNT autossuficientes?
   - [ ] `output/relatorio.pdf` tem no máximo 5 páginas, `output/deck.pdf` tem o
         mesmo número de slides de `deck.pptx`, e `make test && make lint` passam?
