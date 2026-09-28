import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

# 1. Configurando as chaves de acesso diretamente no sistema
os.environ["GROQ_API_KEY"] = "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"
os.environ["TAVILY_API_KEY"] = (
    "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"
)

# 2. Criando o agente com o modelo correto da Groq
agent = Agent(
    model=Groq(id="llama-3.3-70b-specdec"), tools=[TavilyTools()], markdown=True
)

# 3. Executando a pergunta e mostrando o resultado no terminal
agent.print_response(
    "Use suas ferramentas para pesquisar a temperatura em Curitiba hoje?", stream=True
)
