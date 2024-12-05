import pandas as pd 
import requests
import os 
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

key = "aa0bc3fbc6a64efb8b042c2296b7bc1c"

url = f"https://newsapi.org/v2/top-headlines?category=sports&apiKey={key}"

#response = requests.get(url)

# Configuração do servidor SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "gustavohqpasciano@gmail.com"
PASSWORD = "sepf rmmm gopd osoz"

# Função para enviar o e-mail
def enviar_email(destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(mensagem, "plain"))
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

# Função principal
def enviar_noticias():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        
        if articles:
            mensagem = "Aqui estão as notícias da semana sobre esportes no Brasil:\n\n"
            for article in articles:
                title = article.get("title", "Sem título")
                description = article.get("description", "Sem descrição")
                link = article.get("url", "Sem link")
                mensagem += f"Título: {title}\nDescrição: {description}\nLink: {link}\n{'-' * 40}\n"
            
            try:
                enviar_email("gustavohqpasciano@gmail.com", "Notícias Semanais - Esportes", mensagem)
                print("E-mail com notícias enviado com sucesso!")
            except Exception as e:
                print("Erro ao enviar o e-mail:", e)
        else:
            print("Nenhuma notícia encontrada para o filtro atual.")
    else:
        print(f"Erro na API. Status code: {response.status_code}")

# Executar
enviar_noticias()