#!/usr/bin/env python3
"""
Script de teste para verificar se o app.py inicia corretamente
"""

import sys
import os

# Adicionar diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🔍 Testando inicialização do app...")

try:
    print("1. Importando Flask...")
    from flask import Flask
    print("   ✅ Flask OK")

    print("2. Importando dotenv...")
    from dotenv import load_dotenv
    print("   ✅ dotenv OK")

    print("3. Importando google-genai...")
    from google import genai
    print("   ✅ google-genai OK")

    print("4. Importando BeautifulSoup...")
    from bs4 import BeautifulSoup
    print("   ✅ BeautifulSoup OK")

    print("5. Importando app principal...")
    import app
    print("   ✅ app.py OK")

    print("6. Verificando se app Flask foi criado...")
    if hasattr(app, 'app'):
        print("   ✅ Flask app criado")
    else:
        print("   ❌ Flask app NÃO encontrado")
        sys.exit(1)

    print("7. Verificando rotas...")
    routes = [rule.rule for rule in app.app.url_map.iter_rules()]
    print(f"   ✅ {len(routes)} rotas encontradas: {routes}")

    print("\n✅ TODOS OS TESTES PASSARAM!")
    print("O app deveria funcionar no Render.\n")

except ImportError as e:
    print(f"\n❌ ERRO DE IMPORTAÇÃO: {e}")
    print("Instale as dependências: pip install -r requirements.txt\n")
    sys.exit(1)

except Exception as e:
    print(f"\n❌ ERRO INESPERADO: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
