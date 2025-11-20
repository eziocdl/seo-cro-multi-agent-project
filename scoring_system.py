"""
Scoring system for site analysis.
Calculates SEO, CRO, and GEO scores based ONLY on real extracted data.
"""

from typing import Dict, Tuple
from datetime import datetime

TITLE_OPTIMAL_MIN = 50
TITLE_OPTIMAL_MAX = 60
TITLE_GOOD_MIN = 40
TITLE_GOOD_MAX = 70

META_DESC_OPTIMAL_MIN = 150
META_DESC_OPTIMAL_MAX = 160
META_DESC_GOOD_MIN = 140
META_DESC_GOOD_MAX = 170

WORD_COUNT_EXCELLENT = 1000
WORD_COUNT_GOOD = 300
WORD_COUNT_BASIC = 100

LOAD_TIME_EXCELLENT = 1.5
LOAD_TIME_GOOD = 2.5
LOAD_TIME_MEDIUM = 4.0
LOAD_TIME_BAD = 6.0

LOAD_TIME_CRO_EXCELLENT = 2.0
LOAD_TIME_CRO_GOOD = 3.5
LOAD_TIME_CRO_MEDIUM = 5.0

WORD_COUNT_CRO_MIN = 500
WORD_COUNT_CRO_MAX = 3000
WORD_COUNT_CRO_ADEQUATE = 300

WORD_COUNT_GEO_EXCELLENT = 800
WORD_COUNT_GEO_GOOD = 400
WORD_COUNT_GEO_BASIC = 200

MAX_POINTS_PER_CATEGORY = 25
MAX_POINTS_CRO_CATEGORY = 20

SCORE_EXCELLENT = 80
SCORE_GOOD = 60
SCORE_REQUIRES_OPTIMIZATION = 40

SEO_WEIGHT = 0.4
CRO_WEIGHT = 0.3
GEO_WEIGHT = 0.3


class SiteScoreCalculator:
    """Calculate objective scores based on real data."""

    def __init__(self, real_data: Dict):
        """
        Initialize calculator with real scraped data.

        Args:
            real_data: Real data extracted from web_scraper.py
        """
        self.data = real_data
        self.timestamp = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    def calculate_seo_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calculate SEO Health Score (0-100).

        Components:
        - On-Page SEO (25 points)
        - Technical SEO (25 points)
        - Content Quality (25 points)
        - Core Web Vitals (25 points)

        Returns:
            Tuple of (total_score, breakdown_dict)
        """
        scores = {}

        scores['on_page_seo'] = self._calculate_on_page_seo()
        scores['technical_seo'] = self._calculate_technical_seo()
        scores['content_quality'] = self._calculate_content_quality()
        scores['core_web_vitals'] = self._calculate_core_web_vitals()

        total_seo = sum(scores.values())
        return total_seo, scores

    def _calculate_on_page_seo(self) -> int:
        """Calculate on-page SEO score (max 25 points)."""
        score = 0

        title_len = len(self.data.get('title', ''))
        if TITLE_OPTIMAL_MIN <= title_len <= TITLE_OPTIMAL_MAX:
            score += 8
        elif TITLE_GOOD_MIN <= title_len <= TITLE_GOOD_MAX:
            score += 5
        elif title_len > 0:
            score += 2

        meta_len = len(self.data.get('meta_description', ''))
        if META_DESC_OPTIMAL_MIN <= meta_len <= META_DESC_OPTIMAL_MAX:
            score += 8
        elif META_DESC_GOOD_MIN <= meta_len <= META_DESC_GOOD_MAX:
            score += 5
        elif meta_len > 0:
            score += 2

        h1_count = len(self.data.get('headings', {}).get('h1', []))
        if h1_count == 1:
            score += 9
        elif h1_count > 0:
            score += 4

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_technical_seo(self) -> int:
        """Calculate technical SEO score (max 25 points)."""
        score = 0

        if self.data.get('has_ssl', False):
            score += 10

        if self.data.get('mobile_friendly', False):
            score += 10

        schema_count = len(self.data.get('schema_types', []))
        if schema_count >= 3:
            score += 5
        elif schema_count >= 1:
            score += 3

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_content_quality(self) -> int:
        """Calculate content quality score (max 25 points)."""
        score = 0

        word_count = self.data.get('word_count', 0)
        if word_count >= WORD_COUNT_EXCELLENT:
            score += 10
        elif word_count >= WORD_COUNT_GOOD:
            score += 7
        elif word_count >= WORD_COUNT_BASIC:
            score += 4

        images_total = self.data.get('images', {}).get('total', 0)
        images_without_alt = self.data.get('images', {}).get('without_alt', 0)

        if images_total > 0:
            alt_coverage = ((images_total - images_without_alt) / images_total) * 100
            if alt_coverage >= 90:
                score += 10
            elif alt_coverage >= 70:
                score += 7
            elif alt_coverage >= 50:
                score += 4

        internal_links = self.data.get('links', {}).get('internal', 0)
        if internal_links >= 10:
            score += 5
        elif internal_links >= 5:
            score += 3
        elif internal_links >= 1:
            score += 1

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_core_web_vitals(self) -> int:
        """Calculate core web vitals / performance score (max 25 points)."""
        load_time = self.data.get('load_time', 999)

        if load_time <= LOAD_TIME_EXCELLENT:
            return 25
        elif load_time <= LOAD_TIME_GOOD:
            return 20
        elif load_time <= LOAD_TIME_MEDIUM:
            return 12
        elif load_time <= LOAD_TIME_BAD:
            return 6
        else:
            return 2

    def calculate_cro_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calculate CRO Readiness Score (0-100).

        Components:
        - CTA Effectiveness (20 points)
        - Form Optimization (20 points)
        - Trust & Credibility (20 points)
        - Page Experience (20 points)
        - Mobile Readiness (20 points)

        Returns:
            Tuple of (total_score, breakdown_dict)
        """
        scores = {}

        scores['cta_effectiveness'] = self._calculate_cta_effectiveness()
        scores['form_optimization'] = 0
        scores['trust_credibility'] = self._calculate_trust_credibility()
        scores['page_experience'] = self._calculate_page_experience()
        scores['mobile_readiness'] = self._calculate_mobile_readiness()

        total_cro = sum(scores.values())
        return total_cro, scores

    def _calculate_cta_effectiveness(self) -> int:
        """Calculate CTA effectiveness score (max 20 points)."""
        score = 0
        total_links = self.data.get('links', {}).get('total', 0)
        internal_links = self.data.get('links', {}).get('internal', 0)
        external_links = self.data.get('links', {}).get('external', 0)

        if total_links >= 5:
            score += 10
        elif total_links >= 2:
            score += 5

        if internal_links > external_links and internal_links > 0:
            score += 10

        return min(score, MAX_POINTS_CRO_CATEGORY)

    def _calculate_trust_credibility(self) -> int:
        """Calculate trust & credibility score (max 20 points)."""
        score = 0

        if self.data.get('has_ssl', False):
            score += 15

        if len(self.data.get('schema_types', [])) > 0:
            score += 5

        return min(score, MAX_POINTS_CRO_CATEGORY)

    def _calculate_page_experience(self) -> int:
        """Calculate page experience score (max 20 points)."""
        score = 0

        load_time = self.data.get('load_time', 999)
        if load_time <= LOAD_TIME_CRO_EXCELLENT:
            score += 10
        elif load_time <= LOAD_TIME_CRO_GOOD:
            score += 6
        elif load_time <= LOAD_TIME_CRO_MEDIUM:
            score += 3

        word_count = self.data.get('word_count', 0)
        if WORD_COUNT_CRO_MIN <= word_count <= WORD_COUNT_CRO_MAX:
            score += 10
        elif word_count >= WORD_COUNT_CRO_ADEQUATE:
            score += 6

        return min(score, MAX_POINTS_CRO_CATEGORY)

    def _calculate_mobile_readiness(self) -> int:
        """Calculate mobile readiness score (max 20 points)."""
        score = 0

        if self.data.get('mobile_friendly', False):
            score += 15

        load_time = self.data.get('load_time', 999)
        if load_time <= 3.0:
            score += 5
        elif load_time <= 5.0:
            score += 2

        return min(score, MAX_POINTS_CRO_CATEGORY)

    def calculate_geo_score(self) -> Tuple[int, Dict[str, int]]:
        """
        Calculate GEO Readiness Score (0-100).

        Components:
        - Structured Data Quality (25 points)
        - AI Content Format (25 points)
        - Knowledge Graph Signals (25 points)
        - Hallucination Risk Management (25 points)

        Returns:
            Tuple of (total_score, breakdown_dict)
        """
        scores = {}

        scores['structured_data_quality'] = self._calculate_structured_data_quality()
        scores['ai_content_format'] = self._calculate_ai_content_format()
        scores['knowledge_graph_signals'] = self._calculate_knowledge_graph_signals()
        scores['hallucination_risk_mgmt'] = self._calculate_hallucination_risk_mgmt()

        total_geo = sum(scores.values())
        return total_geo, scores

    def _calculate_structured_data_quality(self) -> int:
        """Calculate structured data quality score (max 25 points)."""
        score = 0
        schema_types = self.data.get('schema_types', [])
        schema_count = len(schema_types)

        if schema_count >= 5:
            score += 15
        elif schema_count >= 3:
            score += 12
        elif schema_count >= 1:
            score += 8

        important_schemas = ['Organization', 'Article', 'LocalBusiness', 'Product', 'FAQPage']
        matches = sum(1 for schema in schema_types if any(imp in schema for imp in important_schemas))

        if matches >= 3:
            score += 10
        elif matches >= 2:
            score += 6
        elif matches >= 1:
            score += 3

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_ai_content_format(self) -> int:
        """Calculate AI content format score (max 25 points)."""
        score = 0

        headings = self.data.get('headings', {})
        h1_count = len(headings.get('h1', []))
        h2_count = len(headings.get('h2', []))

        if h1_count == 1 and h2_count >= 2:
            score += 15
        elif h1_count == 1:
            score += 10
        elif h2_count >= 2:
            score += 8

        word_count = self.data.get('word_count', 0)
        if word_count >= WORD_COUNT_GEO_EXCELLENT:
            score += 10
        elif word_count >= WORD_COUNT_GEO_GOOD:
            score += 6
        elif word_count >= WORD_COUNT_GEO_BASIC:
            score += 3

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_knowledge_graph_signals(self) -> int:
        """Calculate knowledge graph signals score (max 25 points)."""
        score = 0
        schema_types = self.data.get('schema_types', [])

        if any('Organization' in s or 'LocalBusiness' in s for s in schema_types):
            score += 10

        if len(self.data.get('meta_description', '')) >= 100:
            score += 5

        title = self.data.get('title', '')
        if len(title) >= 40 and (' | ' in title or ' - ' in title):
            score += 5

        internal_links = self.data.get('links', {}).get('internal', 0)
        if internal_links >= 15:
            score += 5
        elif internal_links >= 8:
            score += 3

        return min(score, MAX_POINTS_PER_CATEGORY)

    def _calculate_hallucination_risk_mgmt(self) -> int:
        """Calculate hallucination risk management score (max 25 points)."""
        score = 0
        schema_count = len(self.data.get('schema_types', []))
        h1_count = len(self.data.get('headings', {}).get('h1', []))
        word_count = self.data.get('word_count', 0)

        if schema_count >= 2:
            score += 10
        elif schema_count >= 1:
            score += 5

        if h1_count == 1 and word_count >= 300:
            score += 10
        elif word_count >= 150:
            score += 5

        if len(self.data.get('title', '')) >= 30 and len(self.data.get('meta_description', '')) >= 100:
            score += 5

        return min(score, MAX_POINTS_PER_CATEGORY)

    def get_overall_score(self) -> int:
        """
        Calculate weighted overall score.

        Weights: SEO 40%, CRO 30%, GEO 30%

        Returns:
            Overall score (0-100)
        """
        seo_score, _ = self.calculate_seo_score()
        cro_score, _ = self.calculate_cro_score()
        geo_score, _ = self.calculate_geo_score()

        overall = int((seo_score * SEO_WEIGHT) + (cro_score * CRO_WEIGHT) + (geo_score * GEO_WEIGHT))
        return overall

    def get_classification(self, score: int) -> Tuple[str, str]:
        """
        Return textual classification of score.

        Args:
            score: Score value (0-100)

        Returns:
            Tuple of (classification, status_code)
        """
        if score >= SCORE_EXCELLENT:
            return ("Excelente", "A")
        elif score >= SCORE_GOOD:
            return ("Bom", "B")
        elif score >= SCORE_REQUIRES_OPTIMIZATION:
            return ("Requer Otimização", "C")
        else:
            return ("Crítico", "D")

    def generate_progress_bar(self, score: int, max_width: int = 20) -> str:
        """
        Generate visual ASCII progress bar.

        Args:
            score: Score value (0-100)
            max_width: Maximum width of progress bar

        Returns:
            ASCII progress bar string
        """
        filled = int((score / 100) * max_width)
        empty = max_width - filled
        return "█" * filled + "░" * empty

    def get_full_report_data(self) -> Dict:
        """
        Return all scoring data for report use.

        Returns:
            Dictionary with all scores, breakdowns, and classifications
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
    Helper function to calculate all scores in simplified way.

    Args:
        real_data: Data extracted from web_scraper

    Returns:
        Complete dictionary with all scores and analysis
    """
    calculator = SiteScoreCalculator(real_data)
    return calculator.get_full_report_data()
