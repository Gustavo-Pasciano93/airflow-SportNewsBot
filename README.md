# Sports News Email Sender 📰⚽🏀

## Sobre o projeto

Este projeto foi criado para coletar as **principais notícias de esportes do mundo** utilizando a **NewsAPI** e enviá-las semanalmente por e-mail. O envio é **automatizado** e ocorre todas as segundas-feiras, com a ajuda do **Apache Airflow** para orquestrar o processo. O objetivo é manter os usuários **sempre atualizados** sobre as últimas notícias do mundo dos esportes, com uma entrega prática e eficiente.

## Funcionalidades

- **Coleta de Notícias:** O projeto utiliza a **NewsAPI** para buscar as últimas notícias de esportes globalmente.
- **Envio Semanal de E-mails:** A cada segunda-feira, as notícias são enviadas por e-mail, mantendo os usuários sempre informados.
- **Automatização com Apache Airflow:** O fluxo de trabalho é orquestrado com **Airflow**, garantindo a execução de forma automatizada e escalável.
- **Personalização no Envio:** O corpo do e-mail é formatado de forma amigável, com título, descrição e link das notícias.
- **Python e Bibliotecas:** O projeto foi desenvolvido em **Python** e utiliza bibliotecas como **requests**, **smtplib**, e **email.mime** para as operações de coleta e envio.

## Tecnologias Utilizadas

- **NewsAPI** - API para coletar notícias de fontes confiáveis e bem estabelecidas.
- **Python 3.12** - Linguagem utilizada para desenvolver a lógica do projeto.
- **Apache Airflow** - Ferramenta para orquestrar e agendar o envio automático das notícias.
- **SMPT (Gmail)** - Envio de e-mails utilizando servidor SMTP do Gmail.
- **Bibliotecas Python:** `requests`, `smtplib`, `email.mime`, entre outras.

