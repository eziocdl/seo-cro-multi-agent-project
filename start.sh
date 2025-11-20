#!/bin/bash

# Script de inicialização do AI SEO Audit Team
# ==============================================

echo "🚀 AI SEO Audit Team - Iniciando servidor..."
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Caminho do projeto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# 1. Verificar se o virtual environment existe
echo "📦 Verificando ambiente virtual..."
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment não encontrado. Criando...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment criado${NC}"
fi

# 2. Ativar virtual environment
echo "🔧 Ativando virtual environment..."
source venv/bin/activate

# 3. Verificar/Instalar dependências Python
echo "📚 Verificando dependências Python..."
if ! pip show flask > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Dependências não instaladas. Instalando...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependências instaladas${NC}"
else
    echo -e "${GREEN}✅ Dependências já instaladas${NC}"
fi

# 4. Verificar arquivo .env
echo "🔑 Verificando configurações..."
if [ ! -f ".env" ]; then
    echo -e "${RED}❌ Arquivo .env não encontrado!${NC}"
    echo -e "${YELLOW}Criando .env de exemplo...${NC}"
    cat > .env << 'EOF'
# Configurações do AI SEO Audit Team
GOOGLE_API_KEY=sua-chave-aqui

# Opcional: Firecrawl para scraping real
# FIRECRAWL_API_KEY=sua-chave-aqui
EOF
    echo -e "${RED}⚠️  Configure a GOOGLE_API_KEY no arquivo .env antes de continuar!${NC}"
    exit 1
fi

# Verificar se a API key está configurada
if ! grep -q "GOOGLE_API_KEY=AIza" .env && ! grep -q "GOOGLE_API_KEY=\"AIza" .env; then
    echo -e "${RED}❌ GOOGLE_API_KEY não configurada no arquivo .env!${NC}"
    echo -e "${YELLOW}Por favor, adicione sua chave da API do Google no arquivo .env${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configurações OK${NC}"

# 5. Verificar se a porta 8000 está disponível
echo "🌐 Verificando porta 8000..."
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo -e "${RED}❌ Porta 8000 já está em uso!${NC}"
    echo -e "${YELLOW}Matando processo existente...${NC}"
    kill -9 $(lsof -ti:8000)
    sleep 2
fi

# 6. Iniciar servidor
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✨ Iniciando servidor Flask...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "📱 Frontend: ${GREEN}http://localhost:8000${NC}"
echo -e "🔍 Health Check: ${GREEN}http://localhost:8000/health${NC}"
echo -e "🛑 Para parar: ${YELLOW}Ctrl+C${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Executar o servidor
python app.py
