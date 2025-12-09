# Investigação de Algoritmos de Gradient Boosting e Transfer Learning na Predição de Óbito por COVID-19

## Resumo do Projeto

Este projeto investiga a influência de diferentes algoritmos de gradient boosting (LightGBM, XGBoost e CatBoost) e da técnica de transfer learning sobre a importância atribuída às variáveis preditoras e sobre a justiça algorítmica na predição de óbito hospitalar por COVID-19. Utilizamos modelos explicáveis com valores de Shapley (SHAP) na base de dados IACOV-BR.

## Objetivos Específicos

1. **Comparar a estabilidade das explicações**: Analisar a importância global das features entre LightGBM, XGBoost e CatBoost treinados no mesmo conjunto de dados.

2. **Avaliar o impacto do transfer learning**: Investigar como o transfer learning afeta a importância das features e o desempenho preditivo em contextos de "alto recurso" e "baixo recurso".

3. **Identificar vieses explícitos e implícitos**: Detectar contribuições diretas de raça/cor e sexo, bem como contribuições diferentes para as mesmas variáveis clínicas entre grupos demográficos.

4. **Analisar viés implícito via SHAP**: Verificar se os modelos atribuem contribuições preditivas distintas a variáveis clínicas baseadas nos atributos demográficos dos pacientes.

## Estrutura do Projeto

```
daicarvalho/
├── data/
│   ├── raw/                          # Dados brutos originais
│   │   ├── F_Tabela_Geral_Final.xlsx (base não tratada)
│   │   └── df_iacov_treated.xlsx     (base tratada)
│   └── processed/                    # Dados processados e limpos
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb       # Análise exploratória e descritiva
│   ├── 02_preprocessing.ipynb              # Pré-processamento de dados
│   ├── 03_modeling_lightgbm.ipynb          # Modelagem com LightGBM
│   ├── 04_modeling_xgboost.ipynb           # Modelagem com XGBoost
│   ├── 05_modeling_catboost.ipynb          # Modelagem com CatBoost
│   ├── 06_shap_analysis.ipynb              # Análise SHAP e explicabilidade
│   ├── 07_algorithmic_fairness.ipynb       # Análise de justiça algorítmica
│   └── 08_transfer_learning.ipynb          # Transfer learning e comparações
├── src/
│   ├── __init__.py
│   ├── data_loader.py                # Funções para carregar dados
│   ├── preprocessing.py              # Funções de pré-processamento
│   ├── modeling.py                   # Funções para treinamento de modelos
│   ├── shap_analysis.py              # Funções para análise SHAP
│   └── fairness_metrics.py           # Funções para métricas de justiça
├── results/                          # Resultados de modelos e análises
├── figures/                          # Gráficos e visualizações
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Este arquivo

```

## Bases de Dados

### Base Não Tratada (F_Tabela_Geral_Final.xlsx)
- **Dimensões**: 16.836 pacientes × 78 variáveis
- **Características**: Contém dados brutos com muitos valores faltantes
- **Variável alvo**: `obito` (óbito hospitalar)

### Base Tratada (df_iacov_treated.xlsx)
- **Dimensões**: 6.011 pacientes × 26 variáveis
- **Características**: Dados já selecionados e limpos
- **Variável alvo**: `death` (óbito)

## Variáveis Principais

### Demográficas
- `age` / `idade`: Idade do paciente
- `male` / `genero`: Sexo do paciente
- `raca`: Raça/cor (apenas na base não tratada)

### Vitais
- `heart_rate` / `fc`: Frequência cardíaca
- `resp_rate` / `fr`: Frequência respiratória
- `sys_press` / `pa_sist`: Pressão arterial sistólica
- `dias_press` / `pa_diast`: Pressão arterial diastólica
- `temp`: Temperatura
- `saturacao`: Saturação de oxigênio

### Laboratoriais
- `hemoglobin` / `hb`: Hemoglobina
- `platelets` / `plaquetas`: Plaquetas
- `leukocytes` / `leucocitos`: Leucócitos
- `crp` / `proteina_c_reativa`: Proteína C reativa
- `hematocrit` / `ht`: Hematócrito
- E muitas outras variáveis laboratoriais

### Desfechos
- `death` / `obito`: Óbito hospitalar (variável alvo)
- `icu` / `uti`: Internação em UTI
- `mv` / `vm`: Ventilação mecânica

## Dependências

O projeto utiliza as seguintes bibliotecas principais:

- **Manipulação de dados**: pandas, numpy
- **Visualização**: matplotlib, seaborn, plotly
- **Modelagem**: scikit-learn, lightgbm, xgboost, catboost
- **Explicabilidade**: shap
- **Análise estatística**: scipy, statsmodels
- **Pré-processamento**: imbalanced-learn

Veja `requirements.txt` para a lista completa.

## Como Usar

### 1. Instalação

```bash
# Clonar o repositório
git clone https://github.com/daicarvalho/daicarvalho.git
cd daicarvalho

# Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executar Notebooks

Os notebooks devem ser executados na seguinte ordem:

1. **01_exploratory_analysis.ipynb**: Entenda os dados através de análises descritivas
2. **02_preprocessing.ipynb**: Limpe e prepare os dados para modelagem
3. **03_modeling_lightgbm.ipynb**: Treine e avalie o modelo LightGBM
4. **04_modeling_xgboost.ipynb**: Treine e avalie o modelo XGBoost
5. **05_modeling_catboost.ipynb**: Treine e avalie o modelo CatBoost
6. **06_shap_analysis.ipynb**: Analise explicabilidade com SHAP
7. **07_algorithmic_fairness.ipynb**: Investigue justiça algorítmica
8. **08_transfer_learning.ipynb**: Implemente e compare transfer learning

### 3. Estrutura dos Notebooks

Cada notebook segue a seguinte estrutura:

- **Introdução**: Explicação do objetivo e conceitos-chave
- **Importações**: Bibliotecas necessárias
- **Carregamento de dados**: Leitura dos dados
- **Análise/Processamento**: Código principal com explicações detalhadas
- **Resultados**: Visualizações e interpretações
- **Conclusões**: Resumo dos aprendizados

## Conceitos-Chave Explicados

### Gradient Boosting
Técnica de aprendizado de máquina que constrói modelos sequencialmente, onde cada novo modelo corrige os erros do anterior. Oferece excelente desempenho preditivo.

### SHAP (SHapley Additive exPlanations)
Método baseado em teoria dos jogos para explicar previsões de modelos. Fornece valores que indicam a contribuição de cada variável para a predição.

### Transfer Learning
Técnica que utiliza conhecimento aprendido em uma tarefa para melhorar o desempenho em outra tarefa. Útil quando dados são limitados.

### Justiça Algorítmica
Análise de vieses nos modelos, garantindo que as previsões sejam justas para diferentes grupos demográficos.

## Resultados Esperados

Este projeto produzirá:

- Modelos de predição de óbito por COVID-19 com alta acurácia
- Análises comparativas de estabilidade entre algoritmos
- Explicações detalhadas das previsões via SHAP
- Avaliação de vieses algorítmicos
- Impacto do transfer learning no desempenho

## Autores

Desenvolvido como parte de pesquisa em aprendizado de máquina explicável e justiça algorítmica.

## Licença

Este projeto está sob licença MIT.

## Contato

Para dúvidas ou sugestões, entre em contato através do repositório GitHub.

---

**Última atualização**: Dezembro de 2025
