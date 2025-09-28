import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
      texto = soup.get_text(separator= ' ')
      #limpar texto
      lines = (line.strip() for line in texto.splitlines())
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
      texto_limpo = '\n'.join(chunk for chunk in chunks if chunk)
      return texto_limpo
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        return None

    
    text = soup.get_text()
    return text

extract_text_from_url('link do artigo aqui')


from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint= "O seu ponto de extremidade aqui",
    api_key= "sua chave aqui",
    api_version= "sua versao aqui",
    deployment_name= "sua implantação aqui",
    max_retries=0
)

def translate_article(text, lang):
  massages = [
      ("system", "Você atua como tradutor de textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
  ]

  response = client.invoke(massages)
  print(response.content)
  return response.content



url = 'o seu link aqui'
text = extract_text_from_url(url)
article = translate_article(text, "pt-br")
print(article)