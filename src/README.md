# Passos de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código completo
Todo o código fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar a aplicação
streamlit run .\src\app.py
```
## Evidência de Execução
<img width="767" height="585" alt="image" src="https://github.com/user-attachments/assets/1b0baa4c-6f1f-4dd4-9201-53d2773d56f4" />
