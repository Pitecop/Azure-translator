# 💻 Projeto: Tradutor com Azure AI & OpenAI  

<div align="center">  
  <img src="https://hermes.digitalinnovation.one/assets/diome/logo.png" alt="DIO Logo" width="200"/>  
</div>  

---

## 🎯 Finalidade do Projeto  

Este projeto foi desenvolvido como parte do meu portfólio, com o objetivo de **implementar na prática as teorias aprendidas no curso de Azure**, utilizando os serviços de **Azure AI Translator** e **OpenAI (gpt-4o-mini)**.  

A proposta foi colocar em prática conceitos como:  
- Criação e gerenciamento de **Grupos de Recursos** no Azure.  
- Configuração e uso do **Azure Translator Service**.  
- Integração do **OpenAI Service** com GPT-4o-mini.  
- Manipulação de textos e documentos para tradução automática.  
- Implementação de **endpoints** e utilização segura da **chave de API**.  

---

## 🛠️ Detalhes Técnicos  

### 🔑 Autenticação e Segurança  
- A comunicação com os serviços é feita via **chave de API** e **endpoint** do Azure.  
- Esses parâmetros são essenciais para garantir o acesso seguro e autenticado aos recursos provisionados.  

### 📄 Leitura e Tradução de Documentos  
- Foi implementado um código capaz de **ler todos os textos de um artigo** e **traduzir automaticamente**.  
- O resultado é exportado para um **novo arquivo README.md**, permitindo visualizar a tradução já formatada em **Markdown** (ex.: no VS Code).  

### 🖥️ Interface com Stakeholders  
Durante as conversas com os stakeholders do projeto, surgiu a ideia de criar uma interface própria.  
- Essa sugestão foi acatada e resultou na construção de uma interface conectada ao backend.  
- O **ChatGPT auxiliou na criação de rotas e integração dos templates** ao servidor, tornando a experiência mais completa e intuitiva.  

---

## 🚀 Como Executar o Projeto  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Configure as variáveis de ambiente no arquivo `.env`:  
   ```bash
   AZURE_TRANSLATE_KEY=your_key_here
   AZURE_TRANSLATE_ENDPOINT=your_endpoint_here
   OPENAI_KEY=your_openai_key_here
   ```

3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:  
   ```bash
   python app.py
   ```

---

## 🌟 Tecnologias Utilizadas  

- [Microsoft Azure Translator](https://azure.microsoft.com/services/cognitive-services/translator/)  
- [Azure OpenAI Service (gpt-4o-mini)](https://learn.microsoft.com/azure/cognitive-services/openai/)  
- Python  
- Flask (para backend e rotas)  
- HTML + Templates (para interface)  
- Markdown (para documentação)  

---

## 🎨 Identidade Visual  

Este projeto foi inspirado na paleta de cores da **DIO (Digital Innovation One)**:  

- **Roxo (#7C3AED)** – Representa tecnologia e inovação.  
- **Azul (#2563EB)** – Confiabilidade e segurança.  
- **Cinza (#F3F4F6)** – Clareza e organização.  

---

## 🤝 Contribuição  

Contribuições são sempre bem-vindas!  
Sinta-se à vontade para abrir issues, sugerir melhorias ou propor novas funcionalidades.  

---

  


```  

