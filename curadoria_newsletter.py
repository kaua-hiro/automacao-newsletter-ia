import feedparser
import urllib.parse
import requests

def buscar_noticias(tema, quantidade=3):
    """Busca notícias recentes no Google News via RSS."""
    tema_codificado = urllib.parse.quote(tema)
    url = f"https://news.google.com/rss/search?q={tema_codificado}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    feed = feedparser.parse(url)
    noticias = []
    
    for entry in feed.entries[:quantidade]:
        noticias.append({
            'titulo': entry.title,
            'link': entry.link
        })
    return noticias

def montar_corpo_email(noticias_copilot, noticias_varejo):
    html = """
    <html>
      <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; max-width: 600px; margin: auto;">
        <h2 style="color: #000000; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px;">
          🤖 Radar IA: Atualizações Copilot & Varejo
        </h2>
        <p>Olá, equipe! Aqui estão as principais movimentações da Inteligência Artificial no mercado para manter todos atualizados.</p>
        
        <h3 style="color: #d9534f; margin-top: 20px;">🔵 Copilot & Produtividade</h3>
        <ul style="list-style-type: square;">
    """
    for n in noticias_copilot:
        html += f"<li style='margin-bottom: 10px;'><a href='{n['link']}' style='color: #0056b3; text-decoration: none;'>{n['titulo']}</a></li>"
        
    html += """
        </ul>
        <h3 style="color: #d9534f; margin-top: 20px;">🛍️ Tecnologia & IA no Varejo de Moda</h3>
        <ul style="list-style-type: square;">
    """
    for n in noticias_varejo:
        html += f"<li style='margin-bottom: 10px;'><a href='{n['link']}' style='color: #0056b3; text-decoration: none;'>{n['titulo']}</a></li>"
        
    html += """
        </ul>
        <br>
        <hr style="border: 0; border-top: 1px solid #e0e0e0;">
        <p style="font-size: 12px; color: #777;"><i>Este rascunho de newsletter foi gerado automaticamente via integração Python.</i></p>
      </body>
    </html>
    """
    return html

def enviar_email_via_api(url_webhook, destinatario, assunto, corpo_html):
    payload = {
        "destinatario": destinatario,
        "assunto": assunto,
        "corpo_html": corpo_html
    }
    
    print("Disparando dados para a API do Power Automate...")
    
    try:
        response = requests.post(url_webhook, json=payload)

        if response.status_code in [200, 202]:
            print(f"✅ Sucesso! E-mail enviado para a caixa de: {destinatario}")
        else:
            print(f"❌ Ocorreu um erro na API. Código: {response.status_code}")
            print(f"Detalhes: {response.text}")
    except Exception as e:
        print(f"❌ Erro de conexão com a rede: {e}")

print("Iniciando coleta de dados (RSS)...")
noticias_copilot = buscar_noticias("Microsoft Copilot novidades produtividade")
noticias_varejo = buscar_noticias("tecnologia inteligência artificial varejo moda")

print("Montando o layout do e-mail...")
corpo_html = montar_corpo_email(noticias_copilot, noticias_varejo)

URL_POWER_AUTOMATE = "https://default1ca382d5f1184c6d8411f8a0da31d5.3b.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/4cd653bb903644a685a43d978ae4c3e0/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=EF1oYQpnD8iSU8zrYwLbeKXLwdO83F4uElnwuXMhgfs" 
EMAIL_DESTINO = "kaua.hiro@hrg3.com.br" 

enviar_email_via_api(URL_POWER_AUTOMATE, EMAIL_DESTINO, "[Rascunho] Radar IA - Guess Brasil", corpo_html)