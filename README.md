# 🌯 iFood SmartOps: Multi-Agent System para Resolução de Logística

## 🚀 Visão do Projeto
O **iFood SmartOps** é um ecossistema de Inteligência Artificial projetado para resolver exceções logísticas e de atendimento em tempo real. Utilizando uma arquitetura de **Multi-Agentes**, o sistema coordena especialistas em Logística, Fintech (iFood Pago) e Customer Experience para transformar problemas complexos em resoluções automatizadas e empáticas.

> ⚠️ **Disclaimer:** Este é um projeto de estudo independente para fins de portfólio. Não possui vínculo oficial com o iFood. Os dados utilizados são sintéticos e as regras de negócio foram baseadas em informações públicas da plataforma.

---

## 🎯 Desafios de Engenharia Atendidos
Este projeto foi desenvolvido com foco nos padrões de alta escala exigidos pelo iFood:

| Desafio | Solução Implementada |
| :--- | :--- |
| **Orquestração Complexa** | Implementação de **Multi-Agents** usando **LangGraph** para fluxos cíclicos e controle de estado. |
| **Qualidade de Dados** | Pipeline de **Data Profiling** e limpeza simulando o ambiente **Spark SQL**. |
| **Validação de Modelos** | Framework de **Evals** (RAGAS/DeepEval) para medir a precisão das resoluções. |
| **Escalabilidade** | Arquitetura de microserviços com **FastAPI** e pronta para **Kubernetes**. |

---

## 🏛️ Arquitetura do Sistema

O SmartOps opera através de um **Agente Supervisor** que atua como o cérebro da operação, distribuindo tarefas para agentes especializados:



### 🧩 Os Agentes:
1.  **Logistics Agent:** Especialista em rastreamento, cálculos de tempo estimado (ETA) e identificação de gargalos na última milha.
2.  **Fintech Agent (iFood Pago):** Avalia elegibilidade de estornos, vouchers e crédito em conta baseado em regras de negócio.
3.  **CX Agent:** Responsável pela síntese da solução em linguagem natural, garantindo a satisfação do cliente (NPS).

---

## 🛠️ Tech Stack
* **AI Engine:** LangGraph, LangChain, OpenAI/Claude.
* **Backend:** Python 3.11+, FastAPI, Pydantic (Data Validation).
* **Data Science:** PySpark (simulação), Pandas, NumPy.
* **Infra/MLOps:** Docker, Terraform, CI/CD via GitHub Actions.
* **Evaluation:** DeepEval (Unit testing para LLMs).

---

## 📊 Pipeline de Dados & Experimentos

### 1. Curadoria de Corpora & Dados Sintéticos
Para garantir a cobertura de casos raros (edge cases), desenvolvemos um motor de **geração de dados sintéticos** que simula logs de pedidos com diversas anomalias logísticas.

### 2. Rigorosa Avaliação (Evals)
Não apenas geramos respostas; nós as medimos. O sistema passa por testes automatizados de:
* **Faithfulness:** A resposta é baseada nos logs reais?
* **Relevancy:** A solução resolve a dor do cliente?
* **Answer Correctness:** O cálculo do estorno está correto?

---

## 💻 Como Rodar o Projeto

### Pré-requisitos
* Python 3.11+
* Docker e Docker Compose
* Chave de API da OpenAI

### Instalação
```bash
# Clone o repositório
git clone [https://github.com/CarlosLivius/ifood-smartops.git](https://github.com/CarlosLivius/ifood-smartops.git)
cd ifood-smartops

# Instale dependências
pip install -r requirements.txt

# Inicie o servidor de Agentes
python src/main.py
