def gerar_html_newsletter(noticias_copilot, noticias_varejo):
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