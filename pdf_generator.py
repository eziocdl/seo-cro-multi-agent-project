#!/usr/bin/env python3
# pdf_generator.py

import markdown
from weasyprint import HTML, CSS
from datetime import datetime
import io

def markdown_to_pdf(markdown_text: str, url_analisada: str) -> bytes:
    """Converte markdown para PDF com estilo"""
    
    html_content = markdown.markdown(
        markdown_text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )
    
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-right {{
                    content: "Página " counter(page) " de " counter(pages);
                }}
            }}
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                color: #2563eb;
                border-bottom: 3px solid #2563eb;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #1e40af;
                margin-top: 30px;
            }}
            h3 {{
                color: #3730a3;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #f3f4f6;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
                padding: 20px;
                background: #f8fafc;
                border-radius: 8px;
            }}
            .footer {{
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                font-size: 12px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>SiteScore - Análise Estratégica Digital</h1>
            <p><strong>URL Analisada:</strong> {url_analisada}</p>
            <p><strong>Data:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        </div>
        {html_content}
        <div class="footer">
            <p>Relatório gerado automaticamente por SiteScore</p>
        </div>
    </body>
    </html>
    """
    
    pdf_bytes = HTML(string=html_template).write_pdf()
    return pdf_bytes