import os
import dotenv
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

# Carrega as chaves de forma segura do arquivo oculto .env
dotenv.load_dotenv()

# Força a injeção caso o sistema operacional mascare as variáveis
if "GROQ_API_KEY" in os.environ:
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
if "TAVILY_API_KEY" in os.environ:
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


# Converter uma temperatura em graus celsius para Fahrenheit.
def celsius_to_fh(temperatura_celsius: float):
    return (temperatura_celsius * 9 / 5) + 32


# Configuração do Agente
agent = Agent(
    model=Groq(id="openai/gpt-oss-20b"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
    ],
    debug_mode=True,
)

agent.print_response(
    "Use suas ferramentas para pesquisar a temperatura de hoje em Curitiba em Fahrenheit"
)
