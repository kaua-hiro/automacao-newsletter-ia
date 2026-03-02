import requests

def enviar_email_via_api(url_webhook, destinatario, assunto, corpo_html):
    payload = {
        "destinatario": destinatario,
        "assunto": assunto,
        "corpo_html": corpo_html
    }
    
    try:
        response = requests.post(url_webhook, json=payload)
        if response.status_code in [200, 202]:
            return True
        return False
    except requests.exceptions.RequestException:
        return False