from config.settings import URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, TEMAS_BUSCA, DISCORD_WEBHOOK_URL
from services.rss_service import buscar_noticias
from templates.newsletter import gerar_html_newsletter
from services.email_service import enviar_email_via_api
from services.discord_service import enviar_newsletter_discord

def main():
    print("Iniciando curadoria de noticias...")
    noticias_copilot = buscar_noticias(TEMAS_BUSCA["copilot"])
    noticias_varejo = buscar_noticias(TEMAS_BUSCA["varejo"])
    
    print("Gerando template HTML e enviando via Power Automate...")
    corpo_html = gerar_html_newsletter(noticias_copilot, noticias_varejo)
    sucesso_email = enviar_email_via_api(URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, corpo_html)
    
    if sucesso_email:
        print("✅ E-mail enviado com sucesso.")
    else:
        print("❌ Erro no envio do E-mail.")

    # 2. Fluxo do Discord (Novo)
    print("Enviando resumo formatado para o Discord...")
    sucesso_discord = enviar_newsletter_discord(DISCORD_WEBHOOK_URL, noticias_copilot, noticias_varejo)
    
    if sucesso_discord:
        print("✅ Discord atualizado com sucesso.")
    else:
        print("❌ Erro no envio para o Discord.")
        
    print("Automação finalizada.")

if __name__ == "__main__":
    main()