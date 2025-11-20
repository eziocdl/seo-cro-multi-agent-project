#!/usr/bin/env bash
set -o errexit

echo "🔧 Iniciando build..."

# Atualizar pip para versão mais recente
pip install --upgrade pip

# Instalar dependências (apenas wheels pré-compilados)
pip install --no-cache-dir -r requirements.txt

echo "✅ Build concluído!"
