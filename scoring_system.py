"""
Sistema de Pontuação para Análise de Sites
Calcula scores de SEO, CRO e GEO baseado APENAS em dados reais extraídos
Seguindo metodologia do documents.md - SEM ALUCINAÇÕES
"""

from typing import Dict, Tuple
from datetime import datetime


class SiteScoreCalculator:
    """Calcula scores objetivos baseados em dados reais"""

    def __init__(self, real_data: Dict):
        """
        Args:
            real_data: Dados reais extraídos do web_scraper.py
        """
        self.data = real_data
        self.timestamp = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    def calculate_seo_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calcula SEO Health Score (0-100)

        Componentes:
        - On-Page SEO (25 pontos)
        - Technical SEO (25 pontos)
        - Content Quality (25 pontos)
        - Core Web Vitals (25 pontos)

        Returns:
            (score_total, breakdown_dict)
        """
        scores = {}

        # 1. ON-PAGE SEO (25 pontos)
        on_page = 0

        # Title tag (8 pontos)
        title_len = len(self.data.get('title', ''))
        if 50 <= title_len <= 60:
            on_page += 8
        elif 40 <= title_len <= 70:
            on_page += 5
        elif title_len > 0:
            on_page += 2

        # Meta description (8 pontos)
        meta_len = len(self.data.get('meta_description', ''))
        if 150 <= meta_len <= 160:
            on_page += 8
        elif 140 <= meta_len <= 170:
            on_page += 5
        elif meta_len > 0:
            on_page += 2

        # H1 tags - deve ter exatamente 1 (9 pontos)
        h1_count = len(self.data.get('headings', {}).get('h1', []))
        if h1_count == 1:
            on_page += 9
        elif h1_count > 0:
            on_page += 4

        scores['on_page_seo'] = min(on_page, 25)

        # 2. TECHNICAL SEO (25 pontos)
        technical = 0

        # HTTPS/SSL (10 pontos)
        if self.data.get('has_ssl', False):
            technical += 10

        # Mobile-friendly (10 pontos)
        if self.data.get('mobile_friendly', False):
            technical += 10

        # Schema.org structured data (5 pontos)
        schema_count = len(self.data.get('schema_types', []))
        if schema_count >= 3:
            technical += 5
        elif schema_count >= 1:
            technical += 3

        scores['technical_seo'] = min(technical, 25)

        # 3. CONTENT QUALITY (25 pontos)
        content = 0

        # Word count (10 pontos)
        word_count = self.data.get('word_count', 0)
        if word_count >= 1000:
            content += 10
        elif word_count >= 300:
            content += 7
        elif word_count >= 100:
            content += 4

        # Images with alt text (10 pontos)
        images_total = self.data.get('images', {}).get('total', 0)
        images_without_alt = self.data.get('images', {}).get('without_alt', 0)

        if images_total > 0:
            alt_coverage = ((images_total - images_without_alt) / images_total) * 100
            if alt_coverage >= 90:
                content += 10
            elif alt_coverage >= 70:
                content += 7
            elif alt_coverage >= 50:
                content += 4

        # Internal links (5 pontos)
        internal_links = self.data.get('links', {}).get('internal', 0)
        if internal_links >= 10:
            content += 5
        elif internal_links >= 5:
            content += 3
        elif internal_links >= 1:
            content += 1

        scores['content_quality'] = min(content, 25)

        # 4. CORE WEB VITALS / PERFORMANCE (25 pontos)
        performance = 0

        # Load time (25 pontos) - proxy para Core Web Vitals
        load_time = self.data.get('load_time', 999)
        if load_time <= 1.5:
            performance += 25  # Excelente
        elif load_time <= 2.5:
            performance += 20  # Bom
        elif load_time <= 4.0:
            performance += 12  # Médio
        elif load_time <= 6.0:
            performance += 6   # Ruim
        else:
            performance += 2   # Crítico

        scores['core_web_vitals'] = min(performance, 25)

        # TOTAL SEO SCORE
        total_seo = sum(scores.values())

        return total_seo, scores

    def calculate_cro_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calcula CRO Readiness Score (0-100)

        Componentes:
        - CTA Effectiveness (20 pontos) - inferido de links
        - Form Optimization (20 pontos) - não disponível
        - Trust & Credibility (20 pontos)
        - Page Experience (20 pontos)
        - Mobile Readiness (20 pontos)

        Returns:
            (score_total, breakdown_dict)
        """
        scores = {}

        # 1. CTA EFFECTIVENESS (20 pontos) - inferido de links externos como potencial CTA
        cta = 0
        external_links = self.data.get('links', {}).get('external', 0)
        total_links = self.data.get('links', {}).get('total', 0)

        # Presença de links pode indicar CTAs
        if total_links >= 5:
            cta += 10
        elif total_links >= 2:
            cta += 5

        # Balance entre links internos e externos
        internal_links = self.data.get('links', {}).get('internal', 0)
        if internal_links > external_links and internal_links > 0:
            cta += 10  # Boa navegação interna

        scores['cta_effectiveness'] = min(cta, 20)

        # 2. FORM OPTIMIZATION (20 pontos) - DADOS NÃO DISPONÍVEIS
        # Não temos dados de formulários ainda
        scores['form_optimization'] = 0

        # 3. TRUST & CREDIBILITY (20 pontos)
        trust = 0

        # HTTPS (15 pontos)
        if self.data.get('has_ssl', False):
            trust += 15

        # Schema.org (indica profissionalismo) (5 pontos)
        if len(self.data.get('schema_types', [])) > 0:
            trust += 5

        scores['trust_credibility'] = min(trust, 20)

        # 4. PAGE EXPERIENCE (20 pontos)
        experience = 0

        # Load time (10 pontos)
        load_time = self.data.get('load_time', 999)
        if load_time <= 2.0:
            experience += 10
        elif load_time <= 3.5:
            experience += 6
        elif load_time <= 5.0:
            experience += 3

        # Conteúdo adequado (10 pontos)
        word_count = self.data.get('word_count', 0)
        if 500 <= word_count <= 3000:
            experience += 10
        elif word_count >= 300:
            experience += 6

        scores['page_experience'] = min(experience, 20)

        # 5. MOBILE READINESS (20 pontos)
        mobile = 0

        # Mobile-friendly meta tag (15 pontos)
        if self.data.get('mobile_friendly', False):
            mobile += 15

        # Performance em mobile (load time) (5 pontos)
        if load_time <= 3.0:
            mobile += 5
        elif load_time <= 5.0:
            mobile += 2

        scores['mobile_readiness'] = min(mobile, 20)

        # TOTAL CRO SCORE
        total_cro = sum(scores.values())

        return total_cro, scores

    def calculate_geo_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calcula GEO Readiness Score (0-100)

        Componentes:
        - Structured Data Quality (25 pontos)
        - AI Content Format (25 pontos)
        - Knowledge Graph Signals (25 pontos)
        - Hallucination Risk Management (25 pontos)

        Returns:
            (score_total, breakdown_dict)
        """
        scores = {}

        # 1. STRUCTURED DATA QUALITY (25 pontos)
        structured = 0

        schema_types = self.data.get('schema_types', [])
        schema_count = len(schema_types)

        # Quantidade de schemas implementados (15 pontos)
        if schema_count >= 5:
            structured += 15
        elif schema_count >= 3:
            structured += 12
        elif schema_count >= 1:
            structured += 8

        # Tipos específicos importantes (10 pontos)
        important_schemas = ['Organization', 'Article', 'LocalBusiness', 'Product', 'FAQPage']
        matches = sum(1 for schema in schema_types if any(imp in schema for imp in important_schemas))

        if matches >= 3:
            structured += 10
        elif matches >= 2:
            structured += 6
        elif matches >= 1:
            structured += 3

        scores['structured_data_quality'] = min(structured, 25)

        # 2. AI CONTENT FORMAT (25 pontos)
        ai_format = 0

        # Hierarquia de headings clara (H1-H6) (15 pontos)
        headings = self.data.get('headings', {})
        h1_count = len(headings.get('h1', []))
        h2_count = len(headings.get('h2', []))
        h3_count = len(headings.get('h3', []))

        # H1 único e hierarquia presente
        if h1_count == 1 and h2_count >= 2:
            ai_format += 15
        elif h1_count == 1:
            ai_format += 10
        elif h2_count >= 2:
            ai_format += 8

        # Word count adequado para IA extrair informações (10 pontos)
        word_count = self.data.get('word_count', 0)
        if word_count >= 800:
            ai_format += 10
        elif word_count >= 400:
            ai_format += 6
        elif word_count >= 200:
            ai_format += 3

        scores['ai_content_format'] = min(ai_format, 25)

        # 3. KNOWLEDGE GRAPH SIGNALS (25 pontos)
        knowledge = 0

        # Schema Organization/LocalBusiness (10 pontos)
        if any('Organization' in s or 'LocalBusiness' in s for s in schema_types):
            knowledge += 10

        # Meta description (entidades mencionadas) (5 pontos)
        if len(self.data.get('meta_description', '')) >= 100:
            knowledge += 5

        # Title tag bem estruturado (5 pontos)
        title = self.data.get('title', '')
        if len(title) >= 40 and ' | ' in title or ' - ' in title:
            knowledge += 5

        # Internal linking (sinaliza estrutura de conhecimento) (5 pontos)
        internal_links = self.data.get('links', {}).get('internal', 0)
        if internal_links >= 15:
            knowledge += 5
        elif internal_links >= 8:
            knowledge += 3

        scores['knowledge_graph_signals'] = min(knowledge, 25)

        # 4. HALLUCINATION RISK MANAGEMENT (25 pontos)
        hallucination = 0

        # Structured data presente (reduz alucinações) (10 pontos)
        if schema_count >= 2:
            hallucination += 10
        elif schema_count >= 1:
            hallucination += 5

        # Conteúdo bem estruturado (10 pontos)
        if h1_count == 1 and word_count >= 300:
            hallucination += 10
        elif word_count >= 150:
            hallucination += 5

        # Meta tags completos (IA tem contexto claro) (5 pontos)
        if len(self.data.get('title', '')) >= 30 and len(self.data.get('meta_description', '')) >= 100:
            hallucination += 5

        scores['hallucination_risk_mgmt'] = min(hallucination, 25)

        # TOTAL GEO SCORE
        total_geo = sum(scores.values())

        return total_geo, scores

    def get_overall_score(self) -> int:
        """Calcula score geral médio ponderado"""
        seo_score, _ = self.calculate_seo_score()
        cro_score, _ = self.calculate_cro_score()
        geo_score, _ = self.calculate_geo_score()

        # Peso: SEO 40%, CRO 30%, GEO 30%
        overall = int((seo_score * 0.4) + (cro_score * 0.3) + (geo_score * 0.3))
        return overall

    def get_classification(self, score: int) -> Tuple[str, str]:
        """
        Retorna classificação textual do score

        Returns:
            (classificação, status_code)
        """
        if score >= 80:
            return ("Excelente", "A")
        elif score >= 60:
            return ("Bom", "B")
        elif score >= 40:
            return ("Requer Otimização", "C")
        else:
            return ("Crítico", "D")

    def generate_progress_bar(self, score: int, max_width: int = 20) -> str:
        """Gera barra de progresso visual ASCII"""
        filled = int((score / 100) * max_width)
        empty = max_width - filled
        return "█" * filled + "░" * empty

    def get_full_report_data(self) -> Dict:
        """
        Retorna todos os dados de scoring para uso no relatório

        Returns:
            Dict com todos os scores, breakdowns e classificações
        """
        seo_score, seo_breakdown = self.calculate_seo_score()
        cro_score, cro_breakdown = self.calculate_cro_score()
        geo_score, geo_breakdown = self.calculate_geo_score()
        overall_score = self.get_overall_score()

        return {
            'timestamp': self.timestamp,
            'overall': {
                'score': overall_score,
                'classification': self.get_classification(overall_score)[0],
                'emoji': self.get_classification(overall_score)[1],
                'progress_bar': self.generate_progress_bar(overall_score)
            },
            'seo': {
                'score': seo_score,
                'classification': self.get_classification(seo_score)[0],
                'emoji': self.get_classification(seo_score)[1],
                'progress_bar': self.generate_progress_bar(seo_score),
                'breakdown': seo_breakdown
            },
            'cro': {
                'score': cro_score,
                'classification': self.get_classification(cro_score)[0],
                'emoji': self.get_classification(cro_score)[1],
                'progress_bar': self.generate_progress_bar(cro_score),
                'breakdown': cro_breakdown
            },
            'geo': {
                'score': geo_score,
                'classification': self.get_classification(geo_score)[0],
                'emoji': self.get_classification(geo_score)[1],
                'progress_bar': self.generate_progress_bar(geo_score),
                'breakdown': geo_breakdown
            }
        }


def calculate_scores(real_data: Dict) -> Dict:
    """
    Função helper para calcular todos os scores de forma simplificada

    Args:
        real_data: Dados extraídos do web_scraper

    Returns:
        Dict completo com todos os scores e análises
    """
    calculator = SiteScoreCalculator(real_data)
    return calculator.get_full_report_data()
