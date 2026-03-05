from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv()

CAMINHO_DB = "db"

prompt_template = """
Responda a pergunta do usuário:
{pergunta}

Utilize os seguintes documentos para responder a pergunta:

{base_conhecimento}

Se não encontrar a resposta nos documentos, responda 
"Desculpe, não sei a resposta para essa pergunta."
"""

def perguntar():
    pergunta = input("Escreva sua pergunta: ")

    funcao_embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embeddings)

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)
    if len(resultados) == 0 or resultados[0][1] < 0.5:
        print("Desculpe, não sei a resposta para essa pergunta.")
        return
    
    textos_resultado = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.append(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultado)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"pergunta": pergunta, "base_conhecimento": base_conhecimento})
    
    modelo = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.2)
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta: ", texto_resposta)

perguntar()