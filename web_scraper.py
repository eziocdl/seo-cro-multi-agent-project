"""
Módulo de scraping web para coleta de dados REAIS dos sites
Usa apenas ferramentas gratuitas: BeautifulSoup, Requests, Google PageSpeed Insights API
"""

import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urlparse, urljoin
from typing import Dict, List, Optional
import json

class WebScraper:
    """Scraper profissional para análise SEO"""

    def __init__(self, url: str, timeout: int = 10):
        self.url = url
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.soup = None
        self.response = None
        self.load_time = 0

    def fetch_page(self) -> bool:
        """Faz o download da página e mede tempo de resposta"""
        try:
            print(f"[SCRAPER] Baixando página: {self.url}")
            start_time = time.time()

            self.response = requests.get(
                self.url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True
            )

            self.load_time = time.time() - start_time
            self.response.raise_for_status()

            # Parse HTML (usando html.parser nativo do Python)
            self.soup = BeautifulSoup(self.response.content, 'html.parser')

            print(f"[SCRAPER] ✓ Página baixada ({self.load_time:.2f}s, {len(self.response.content)} bytes)")
            return True

        except requests.exceptions.Timeout:
            print(f"[SCRAPER] ✗ Timeout ao acessar {self.url}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"[SCRAPER] ✗ Erro ao acessar página: {e}")
            return False

    def extract_title(self) -> str:
        """Extrai o título REAL da página"""
        if not self.soup:
            return ""

        title_tag = self.soup.find('title')
        return title_tag.get_text(strip=True) if title_tag else ""

    def extract_meta_description(self) -> str:
        """Extrai a meta description REAL"""
        if not self.soup:
            return ""

        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        if not meta_desc:
            meta_desc = self.soup.find('meta', attrs={'property': 'og:description'})

        return meta_desc.get('content', '').strip() if meta_desc else ""

    def extract_headings(self) -> Dict[str, List[str]]:
        """Extrai TODOS os headings (H1-H6)"""
        if not self.soup:
            return {}

        headings = {}
        for i in range(1, 7):
            tag = f'h{i}'
            headings[tag] = [h.get_text(strip=True) for h in self.soup.find_all(tag)]

        return headings

    def count_words(self) -> int:
        """Conta palavras REAIS do conteúdo textual"""
        if not self.soup:
            return 0

        # Remove scripts e styles
        for script in self.soup(["script", "style", "nav", "header", "footer"]):
            script.decompose()

        # Pega todo texto
        text = self.soup.get_text()

        # Conta palavras
        words = re.findall(r'\b\w+\b', text)
        return len(words)

    def count_links(self) -> Dict[str, int]:
        """Conta links internos e externos REAIS"""
        if not self.soup:
            return {'internal': 0, 'external': 0, 'total': 0}

        internal = 0
        external = 0
        domain = urlparse(self.url).netloc

        for link in self.soup.find_all('a', href=True):
            href = link['href']

            # Resolve URLs relativas
            absolute_url = urljoin(self.url, href)
            link_domain = urlparse(absolute_url).netloc

            if link_domain == domain or not link_domain:
                internal += 1
            else:
                external += 1

        return {
            'internal': internal,
            'external': external,
            'total': internal + external
        }

    def extract_images(self) -> Dict[str, any]:
        """Analisa imagens (quantidade, alt tags)"""
        if not self.soup:
            return {'total': 0, 'without_alt': 0}

        images = self.soup.find_all('img')
        without_alt = sum(1 for img in images if not img.get('alt'))

        return {
            'total': len(images),
            'without_alt': without_alt,
            'with_alt': len(images) - without_alt
        }

    def check_mobile_meta(self) -> bool:
        """Verifica se tem meta viewport (mobile-friendly)"""
        if not self.soup:
            return False

        viewport = self.soup.find('meta', attrs={'name': 'viewport'})
        return bool(viewport)

    def check_ssl(self) -> bool:
        """Verifica se o site usa HTTPS"""
        return self.url.startswith('https://')

    def extract_schema_org(self) -> List[str]:
        """Extrai tipos de Schema.org encontrados"""
        if not self.soup:
            return []

        schemas = []

        # JSON-LD
        for script in self.soup.find_all('script', type='application/ld+json'):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict) and '@type' in data:
                    schemas.append(data['@type'])
                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict) and '@type' in item:
                            schemas.append(item['@type'])
            except:
                pass

        # Microdata
        for tag in self.soup.find_all(attrs={'itemtype': True}):
            itemtype = tag['itemtype']
            schema_type = itemtype.split('/')[-1]
            schemas.append(schema_type)

        return list(set(schemas))

    def get_status_code(self) -> int:
        """Retorna código HTTP"""
        return self.response.status_code if self.response else 0

    def analyze_page(self) -> Dict:
        """Executa análise COMPLETA e REAL da página"""

        if not self.fetch_page():
            return {
                'success': False,
                'error': 'Não foi possível acessar a página'
            }

        print(f"[SCRAPER] Extraindo dados reais da página...")

        data = {
            'success': True,
            'url': self.url,
            'final_url': self.response.url,  # URL após redirects
            'status_code': self.get_status_code(),
            'load_time': round(self.load_time, 2),

            # SEO Básico
            'title': self.extract_title(),
            'meta_description': self.extract_meta_description(),
            'headings': self.extract_headings(),

            # Conteúdo
            'word_count': self.count_words(),
            'links': self.count_links(),
            'images': self.extract_images(),

            # Técnico
            'has_ssl': self.check_ssl(),
            'mobile_friendly': self.check_mobile_meta(),
            'schema_types': self.extract_schema_org(),

            # Metadados
            'content_length': len(self.response.content),
            'response_headers': dict(self.response.headers)
        }

        print(f"[SCRAPER] ✓ Análise completa realizada")
        print(f"[SCRAPER]   - Título: {data['title'][:50]}...")
        print(f"[SCRAPER]   - Palavras: {data['word_count']}")
        print(f"[SCRAPER]   - Links: {data['links']['total']} (int: {data['links']['internal']}, ext: {data['links']['external']})")
        print(f"[SCRAPER]   - Imagens: {data['images']['total']}")

        return data


def scrape_url(url: str) -> Dict:
    """
    Função helper para scraping rápido

    Args:
        url: URL do site a ser analisado

    Returns:
        Dict com todos os dados extraídos ou erro
    """
    scraper = WebScraper(url)
    return scraper.analyze_page()


# Google PageSpeed Insights API (GRATUITA)
def get_pagespeed_insights(url: str, api_key: Optional[str] = None) -> Dict:
    """
    Obtém dados de performance do Google PageSpeed Insights API
    API GRATUITA com limite de 25,000 requisições/dia

    Args:
        url: URL a ser analisada
        api_key: Opcional. Se não fornecida, usa quota anônima (mais limitada)

    Returns:
        Dict com métricas de performance
    """
    try:
        api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

        params = {
            'url': url,
            'category': 'performance',
            'category': 'seo',
            'strategy': 'mobile'
        }

        if api_key:
            params['key'] = api_key

        print(f"[PAGESPEED] Consultando API do Google PageSpeed Insights...")
        response = requests.get(api_url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Extrair métricas principais
        lighthouse_result = data.get('lighthouseResult', {})
        audits = lighthouse_result.get('audits', {})

        metrics = {
            'performance_score': lighthouse_result.get('categories', {}).get('performance', {}).get('score', 0) * 100,
            'seo_score': lighthouse_result.get('categories', {}).get('seo', {}).get('score', 0) * 100,
            'first_contentful_paint': audits.get('first-contentful-paint', {}).get('displayValue', 'N/A'),
            'speed_index': audits.get('speed-index', {}).get('displayValue', 'N/A'),
            'largest_contentful_paint': audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A'),
            'time_to_interactive': audits.get('interactive', {}).get('displayValue', 'N/A'),
            'total_blocking_time': audits.get('total-blocking-time', {}).get('displayValue', 'N/A'),
            'cumulative_layout_shift': audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A'),
        }

        print(f"[PAGESPEED] ✓ Dados obtidos - Performance: {metrics['performance_score']:.0f}/100")
        return metrics

    except Exception as e:
        print(f"[PAGESPEED] ✗ Erro ao consultar API: {e}")
        return {
            'error': str(e),
            'note': 'PageSpeed Insights indisponível no momento'
        }
