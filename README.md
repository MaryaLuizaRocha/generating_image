# OCR e Geração de Cenários no Formato Gherkin

## 📋 O que é?

Este projeto é uma aplicação web desenvolvida com **Flask**, que usa **Reconhecimento Óptico de Caracteres (OCR)** e **Inteligência Artificial** para facilitar a criação automatizada de cenários de teste no formato **Gherkin** (Given, When, Then). A ferramenta processa capturas de tela de interfaces e cria cenários estruturados com base no conteúdo textual extraído e em regras de negócio fornecidas pelo usuário.

---

## 🔍 Como Funciona?

1️⃣ **Upload de imagens**:  
   O usuário pode fazer upload de uma ou mais imagens, como capturas de tela de interfaces de sistemas.  

2️⃣ **Extração de texto via OCR**:  
   O sistema utiliza **EasyOCR** para extrair todo o texto detectável nas imagens enviadas.  

3️⃣ **Adição de regras de negócio** *(opcional)*:  
   O usuário pode fornecer regras específicas, como "A senha deve conter pelo menos 8 caracteres".  

4️⃣ **Geração de cenários**:  
   O texto extraído e as regras de negócio são enviados para a **IA Gemini**, que retorna cenários de teste no formato Gherkin.  

5️⃣ **Exibição dos cenários gerados**:  
   Os cenários criados são exibidos diretamente na interface da web, prontos para uso.

---

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web usado para criar a interface da aplicação.  
- **EasyOCR**: Biblioteca de OCR usada para extrair texto das imagens enviadas.  
- **Google Generative AI (Gemini)**: Responsável por gerar cenários inteligentes no formato Gherkin.  
- **HTML/CSS**: Para criar uma interface limpa, moderna e responsiva.  

---

## 📥 Como Instalar

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

### 1️⃣ Pré-requisitos
Certifique-se de ter o **Python 3.7 ou superior** instalado na sua máquina. Se não tiver, você pode baixá-lo em [python.org](https://www.python.org/).

### 2️⃣ Instale as dependências do projeto
1. Clone este repositório (ou baixe os arquivos diretamente):
   ```bash
   git clone https://github.com/MaryaLuizaRocha/generating_image.git
   cd seu-repositorio
   ```text

   OU

   Baixe o arquivo #Se possuir o zip

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```text

3. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```text

### 3️⃣ Configure sua chave da API Gemini
1. Crie um arquivo `.env` na raiz do projeto:
   ```bash
   touch .env
   ```text

2. Adicione sua chave da API ao arquivo `.env` no seguinte formato:
   ```plaintext
   GEMINI_API_KEY=SUA_CHAVE_DE_API
   ```text
   ❗ **Nota:** Você pode obter sua chave de API do Google Generative AI no [Google Cloud Console](https://console.cloud.google.com/).

### 4️⃣ Inicie o servidor
Execute o seguinte comando para iniciar o servidor Flask:
```bash
python app.py #python3 app.py
```text

A aplicação estará disponível no seu navegador no endereço:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Como Usar?

1️⃣ **Acesse a aplicação:**  
   Abra o link http://127.0.0.1:5000 em seu navegador.  

2️⃣ **Faça upload das imagens:**  
   Use o formulário para enviar uma ou mais imagens que contenham a interface a ser processada.  

3️⃣ **Adicione regras de negócio (opcional):**  
   Insira quaisquer regras adicionais no campo "Regras de Negócio (opcional)".  

4️⃣ **Gere os cenários:**  
   Clique no botão "Enviar" e aguarde os cenários serem gerados.

5️⃣ **Visualize os resultados:**  
   Veja os cenários gerados no formato Gherkin diretamente na página.

---

## Exemplo de Entrada e Saída

### Entrada:
- **Imagens:**
  Capturas de tela com botões, campos e mensagens de erro.
- **Regras de negócio (opcional):**
  ```plaintext
  A senha deve conter pelo menos 8 caracteres.
  ```text

### Saída (cenários gerados):
```gherkin
Feature: Tela de Login

  Scenario: Login bem-sucedido
    Given o usuário insere um e-mail válido
    And insere uma senha com pelo menos 8 caracteres
    When clica no botão "Entrar"
    Then o sistema redireciona para a página inicial

  Scenario: Login falha devido a senha incorreta
    Given o usuário insere um e-mail válido
    And insere uma senha com menos de 8 caracteres
    When clica no botão "Entrar"
    Then o sistema exibe "Senha inválida. Tente novamente."
    And o login deve ser bloqueado
```text

---
