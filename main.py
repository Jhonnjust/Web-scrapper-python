import requests
from bs4 import BeautifulSoup

def scrape_g1_news():
    """
    Coleta os títulos e links das notícias mais recentes do G1 e salva em um arquivo.
    """
    url = "https://g1.globo.com/"
    
    try:
        # Adicionando headers para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança um erro para status de erro (4xx ou 5xx)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Classes atualizadas para o G1 (podem variar dependendo da região)
        noticias = soup.find_all('div', class_='bastian-feed-item')
        
        with open('g1_noticias.txt', 'w', encoding='utf-8') as f:
            for noticia in noticias:
                # Encontra o título e o link
                titulo_tag = noticia.find('a', class_='feed-post-link')
                if not titulo_tag:
                    # Tentando um padrão alternativo
                    titulo_tag = noticia.find('a', class_='gui-color-primary')
                
                if titulo_tag:
                    titulo = titulo_tag.get_text(strip=True)
                    link = titulo_tag['href']
                    
                    f.write(f"Título: {titulo}\n")
                    f.write(f"Link: {link}\n")
                    f.write("-" * 50 + "\n")
        
        print("Dados coletados com sucesso e salvos em 'g1_noticias.txt'.")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    scrape_g1_news()