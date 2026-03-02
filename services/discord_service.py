import requests

def enviar_newsletter_discord(webhook_url, noticias_copilot, noticias_varejo):

    texto_copilot = ""
    for n in noticias_copilot:
        texto_copilot += f"• [{n['titulo']}]({n['link']})\n\n"
        
    texto_varejo = ""
    for n in noticias_varejo:
        texto_varejo += f"• [{n['titulo']}]({n['link']})\n\n"

    descricao = "Olá, equipe! Aqui estão as principais movimentações da Inteligência Artificial no mercado nesta semana.\n\n"
    
    descricao += "**🔵 Copilot & Produtividade**\n"
    descricao += texto_copilot if texto_copilot else "Nenhuma atualização relevante encontrada.\n\n"
    
    descricao += "**🛍️ Tecnologia & IA no Varejo de Moda**\n"
    descricao += texto_varejo if texto_varejo else "Nenhuma atualização relevante encontrada."

    embed = {
        "title": "🤖 Radar IA: Atualizações Copilot & Varejo",
        "description": descricao,
        "color": 14242639,
        "footer": {
            "text": "Automação de Curadoria via Python - Guess Brasil"
        }
    }

    payload = {
        "content": "Novo resumo de tecnologia e inteligência artificial disponível! 🚀",
        "embeds": [embed]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code in [200, 204]:
            return True
        else:
            print(f"\n[DEBUG DISCORD] Status Code: {response.status_code}")
            print(f"[DEBUG DISCORD] Resposta da API: {response.text}\n")
            return False
    except Exception as e:
        print(f"\n[DEBUG DISCORD] Falha de conexão: {e}\n")
        return False