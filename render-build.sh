#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Iniciando build do Render..."

# Atualizar pip
echo "📦 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências Python
echo "📥 Instalando dependências Python..."
pip install -r requirements.txt

echo "✅ Build concluído com sucesso!"
