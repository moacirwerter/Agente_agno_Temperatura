import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

# O Agno vai ler automaticamente as variáveis GROQ_API_KEY e TAVILY_API_KEY do arquivo .env

# Criando o agente sem expor textos de chaves aqui
agent = Agent(model=Groq(id="llama3-70b-8192"), tools=[TavilyTools()], markdown=True)

agent.print_response(
    "Use suas ferramentas para pesquisar a temperatura em Curitiba hoje?", stream=True
)
