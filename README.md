# Chatbot FAQ - Projeto IoT e IA

Este projeto consiste em um chatbot interativo que responde a perguntas frequentes relacionadas à Internet das Coisas (IoT) e Inteligência Artificial (IA). Desenvolvido com Flask para o backend e uma interface web intuitiva, o chatbot permite aos usuários selecionar perguntas e visualizar respostas de forma rápida e prática.

## Demonstração

Para ver uma demonstração, acesse o vídeo no [YouTube](https://youtu.be/mDb0ekMa7ig).

## Estrutura do Projeto

- **app.py**: Arquivo principal do servidor Flask, que gerencia as rotas e serve o conteúdo do chatbot.
- **chatbot.py**: Lida com a lógica das perguntas e respostas do chatbot.
- **templates/index.html**: Página HTML principal para a interface do chatbot.
- **static/styles.css**: Arquivo CSS para estilizar a interface.
- **faq.json**: Arquivo JSON com uma coleção de perguntas e respostas frequentes.

## Instalação

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/lucasrabd/Sprint-4---IA-IOT
   ```

2. **Instalar dependências:**

   Recomendamos usar um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install flask
   ```

3. **Executar o servidor:**

   ```bash
   python app.py
   ```

   O servidor estará disponível em `http://127.0.0.1:5000`.

## Uso

1. Abra o navegador e vá para `http://127.0.0.1:5000`.
2. Escolha uma pergunta na lista suspensa.
3. Clique em "Ver Resposta" para visualizar a resposta correspondente.

## Funcionalidades

- **Respostas Automatizadas**: O chatbot oferece respostas a perguntas frequentes de IoT e IA.
- **Interface Responsiva**: Interface com design limpo e interativo, permitindo fácil navegação para o usuário.

## Tecnologias Utilizadas

- **Python (Flask)**: Servidor backend.
- **HTML, CSS**: Interface frontend.
- **JavaScript**: Requisições assíncronas para exibir respostas em tempo real.


