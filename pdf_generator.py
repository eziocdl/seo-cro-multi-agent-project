#!/usr/bin/env python3

import markdown
from weasyprint import HTML
from datetime import datetime

def markdown_to_pdf(markdown_text: str, url_analisada: str) -> bytes:
    html_content = markdown.markdown(
        markdown_text,
        extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists']
    )

    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <style>
            /* Page Configuration */
            @page {{
                size: A4;
                margin: 2.5cm 2cm 3cm 2cm;

                @top-left {{
                    content: "Growth Engine - Relatório Estratégico";
                    font-size: 9pt;
                    color: #64748b;
                    font-family: 'Segoe UI', Arial, sans-serif;
                }}

                @bottom-center {{
                    content: "Página " counter(page) " de " counter(pages);
                    font-size: 9pt;
                    color: #64748b;
                    font-family: 'Segoe UI', Arial, sans-serif;
                }}

                @bottom-right {{
                    content: "{datetime.now().strftime('%d/%m/%Y')}";
                    font-size: 9pt;
                    color: #64748b;
                    font-family: 'Segoe UI', Arial, sans-serif;
                }}
            }}

            /* Base Typography */
            body {{
                font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.7;
                color: #1e293b;
                font-size: 11pt;
                text-align: justify;
                hyphens: auto;
            }}

            /* Headings Hierarchy */
            h1 {{
                font-size: 24pt;
                font-weight: 900;
                color: #0f172a;
                margin: 0 0 24pt 0;
                padding: 0 0 16pt 0;
                border-bottom: 4px solid #667eea;
                letter-spacing: -0.02em;
                page-break-after: avoid;
                line-height: 1.2;
            }}

            h2 {{
                font-size: 18pt;
                font-weight: 700;
                color: #1e293b;
                margin: 32pt 0 16pt 0;
                padding: 16pt 0 8pt 0;
                border-top: 2px solid #e2e8f0;
                page-break-after: avoid;
                line-height: 1.3;
            }}

            h2:first-of-type {{
                margin-top: 0;
                border-top: none;
                padding-top: 0;
            }}

            h3 {{
                font-size: 14pt;
                font-weight: 700;
                color: #334155;
                margin: 24pt 0 12pt 0;
                page-break-after: avoid;
                line-height: 1.4;
            }}

            h4 {{
                font-size: 12pt;
                font-weight: 600;
                color: #475569;
                margin: 18pt 0 10pt 0;
                page-break-after: avoid;
                line-height: 1.4;
            }}

            h5 {{
                font-size: 11pt;
                font-weight: 600;
                color: #64748b;
                margin: 14pt 0 8pt 0;
                page-break-after: avoid;
            }}

            /* Paragraphs & Text Elements */
            p {{
                margin: 0 0 12pt 0;
                text-align: justify;
                orphans: 3;
                widows: 3;
            }}

            strong {{
                font-weight: 700;
                color: #0f172a;
            }}

            em {{
                font-style: italic;
                color: #334155;
            }}

            /* Lists */
            ul, ol {{
                margin: 12pt 0;
                padding-left: 24pt;
            }}

            li {{
                margin-bottom: 8pt;
                line-height: 1.6;
            }}

            ul li {{
                list-style-type: disc;
            }}

            ul ul li {{
                list-style-type: circle;
            }}

            /* Code Blocks */
            code {{
                font-family: 'SF Mono', 'Consolas', 'Monaco', monospace;
                font-size: 9.5pt;
                background-color: #f1f5f9;
                padding: 2pt 5pt;
                border-radius: 3pt;
                border: 1px solid #e2e8f0;
                color: #667eea;
            }}

            pre {{
                background-color: #f8fafc;
                border: 1px solid #e2e8f0;
                border-left: 4px solid #667eea;
                border-radius: 5pt;
                padding: 14pt;
                margin: 16pt 0;
                overflow-x: auto;
                page-break-inside: avoid;
                line-height: 1.5;
            }}

            pre code {{
                background: none;
                padding: 0;
                border: none;
                color: #334155;
                font-size: 9pt;
            }}

            /* Blockquotes */
            blockquote {{
                margin: 16pt 0;
                padding: 12pt 16pt;
                border-left: 4px solid #667eea;
                background-color: #f8fafc;
                border-radius: 0 5pt 5pt 0;
                font-style: italic;
                color: #475569;
                page-break-inside: avoid;
            }}

            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20pt 0;
                page-break-inside: avoid;
                font-size: 10pt;
            }}

            thead {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}

            th {{
                padding: 10pt 12pt;
                text-align: left;
                font-weight: 700;
                text-transform: uppercase;
                font-size: 9pt;
                letter-spacing: 0.05em;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }}

            td {{
                padding: 10pt 12pt;
                border: 1px solid #e2e8f0;
                vertical-align: top;
            }}

            tbody tr:nth-child(even) {{
                background-color: #f8fafc;
            }}

            tbody tr:nth-child(odd) {{
                background-color: white;
            }}

            /* Horizontal Rules */
            hr {{
                margin: 24pt 0;
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #e2e8f0, transparent);
            }}

            /* Links */
            a {{
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
            }}

            /* Cover Header */
            .pdf-header {{
                text-align: center;
                margin-bottom: 40pt;
                padding: 24pt;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 8pt;
                page-break-after: avoid;
            }}

            .pdf-header h1 {{
                color: white;
                border: none;
                margin: 0 0 16pt 0;
                padding: 0;
                font-size: 26pt;
            }}

            .pdf-header p {{
                margin: 8pt 0;
                font-size: 11pt;
                text-align: center;
                color: rgba(255, 255, 255, 0.95);
            }}

            .pdf-header .url {{
                font-weight: 700;
                font-size: 12pt;
                word-break: break-all;
                background: rgba(255, 255, 255, 0.15);
                padding: 8pt 12pt;
                border-radius: 5pt;
                margin-top: 12pt;
                display: inline-block;
            }}

            /* Footer */
            .pdf-footer {{
                margin-top: 48pt;
                padding-top: 24pt;
                border-top: 2px solid #e2e8f0;
                font-size: 9pt;
                color: #64748b;
                text-align: center;
                page-break-before: avoid;
            }}

            .pdf-footer p {{
                margin: 6pt 0;
                text-align: center;
            }}

            /* Utilities */
            .text-center {{
                text-align: center;
            }}

            .page-break {{
                page-break-before: always;
            }}

            /* Print Optimization */
            @media print {{
                body {{
                    print-color-adjust: exact;
                    -webkit-print-color-adjust: exact;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="pdf-header">
            <h1>Growth Engine</h1>
            <p>Relatório de Auditoria Digital Estratégica</p>
            <p>Análise Completa: SEO + CRO + GEO</p>
            <p class="url">{url_analisada}</p>
            <p>Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}</p>
        </div>

        {html_content}

        <div class="pdf-footer">
            <hr>
            <p><strong>Growth Engine</strong> - Motor de Crescimento Digital</p>
            <p>Relatório Técnico Profissional gerado automaticamente</p>
            <p>Todos os dados são baseados em análise técnica real do website</p>
            <p style="margin-top: 12pt; font-style: italic; color: #94a3b8;">
                Este documento é confidencial e destinado exclusivamente ao proprietário do website analisado.
            </p>
        </div>
    </body>
    </html>
    """

    # Generate PDF with optimized settings
    pdf_bytes = HTML(string=html_template).write_pdf(
        presentational_hints=True,
        optimize_images=True
    )

    return pdf_bytes