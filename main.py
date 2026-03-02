from config.settings import URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, TEMAS_BUSCA
from services.rss_service import buscar_noticias
from templates.newsletter import gerar_html_newsletter
from services.email_service import enviar_email_via_api

def main():
    print("Iniciando curadoria de noticias...")
    noticias_copilot = buscar_noticias(TEMAS_BUSCA["copilot"])
    noticias_varejo = buscar_noticias(TEMAS_BUSCA["varejo"])
    
    print("Gerando template HTML...")
    corpo_html = gerar_html_newsletter(noticias_copilot, noticias_varejo)
    
    print("Enviando via API Power Automate...")
    sucesso = enviar_email_via_api(URL_POWER_AUTOMATE, EMAIL_DESTINO, ASSUNTO_EMAIL, corpo_html)
    
    if sucesso:
        print("Finalizado: Rascunho enviado com sucesso.")
    else:
        print("Erro: Falha na comunicacao com a API.")

if __name__ == "__main__":
    main()