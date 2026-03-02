from config.settings import URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, TEMAS_BUSCA, DISCORD_WEBHOOK_URL
from services.rss_service import buscar_noticias
from templates.newsletter import gerar_html_newsletter
from services.email_service import enviar_email_via_api
from services.discord_service import enviar_newsletter_discord

# ==========================================
# 🎛️ PAINEL DE CONTROLE (FEATURE FLAGS)
# Mude para True (Ligado) ou False (Desligado)
# ==========================================
ENVIAR_EMAIL = False
ENVIAR_DISCORD = True
# ==========================================

def main():
    print("Iniciando curadoria de noticias...")
    noticias_copilot = buscar_noticias(TEMAS_BUSCA["copilot"])
    noticias_varejo = buscar_noticias(TEMAS_BUSCA["varejo"])
    
    # 1. FLUXO DE E-MAIL
    if ENVIAR_EMAIL:
        print("\n[EMAIL] Gerando template e enviando via Power Automate...")
        corpo_html = gerar_html_newsletter(noticias_copilot, noticias_varejo)
        sucesso_email = enviar_email_via_api(URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, corpo_html)
        
        if sucesso_email:
            print("✅ [EMAIL] Enviado com sucesso.")
        else:
            print("❌ [EMAIL] Erro no envio.")
    else:
        print("\n[EMAIL] Envio desativado no painel de controle.")

    # 2. FLUXO DO DISCORD
    if ENVIAR_DISCORD:
        print("\n[DISCORD] Enviando resumo formatado...")
        sucesso_discord = enviar_newsletter_discord(DISCORD_WEBHOOK_URL, noticias_copilot, noticias_varejo)
        
        if sucesso_discord:
            print("✅ [DISCORD] Atualizado com sucesso.")
        else:
            print("❌ [DISCORD] Erro no envio.")
    else:
        print("\n[DISCORD] Envio desativado no painel de controle.")
        
    print("\nAutomação finalizada.")

if __name__ == "__main__":
    main()