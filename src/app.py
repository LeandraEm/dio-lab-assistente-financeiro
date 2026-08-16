import json
import pandas as pd
import requests
import streamlit as st


#  ====================== CONFIGURAÇÃO  ============================= #
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

#  ===================== CARREGAR DADOS ============================= #
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ===================== MONTAR CONTEXTO ============================ # 
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ATERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ===================== SYSTEM PROMPT ============================ # 
SYSTEM_PROMPT = """ Você é o Agente Patinhas, um educador financeiro inteligente e bem-humorado.

OBJETIVO: Ajudar iniciantes a organizar gastos mensais e aprender possibilidades para investimento usando dados do cliente como exemplos práticos.

REGRAS: 
- Sempre baseie suas respostas nos dados fornecidos pelo cliente, utilizando para dar exemplos personalizados.
- Linguagem simples e didática, como se explicasse para um amigo.
- Não faça recomendações de investimento específicas, somente explique como funciona.
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...".
- Critique com bom humor gastos supérfluos relatados pelo cliente, sem julgamento.
- Nunca solicite ou armazene dados sensíveis (senhas, contas bancárias, etc.).
- Sempre pergunte se o cliente entendeu.
- Valorize o esforço diário e planejamento a longo prazo.
- Responda de forma sucinta, com no máximo 2 parágrafos.
- Jamais responta a perguntas fora do tema de ensino de finanças pessoais.

"""

# ===================== CHAMAR OLLAMA ============================ # 
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ===================== INTERFACE ============================ # 
st.title("Patinhas, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças ..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
