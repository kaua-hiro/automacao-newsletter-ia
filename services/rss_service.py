import feedparser
import urllib.parse
from config.settings import QUANTIDADE_NOTICIAS

def buscar_noticias(tema):
    tema_codificado = urllib.parse.quote(tema)
    url = f"https://news.google.com/rss/search?q={tema_codificado}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    feed = feedparser.parse(url)
    noticias = []
    
    for entry in feed.entries[:QUANTIDADE_NOTICIAS]:
        noticias.append({
            'titulo': entry.title,
            'link': entry.link
        })
        
    return noticias