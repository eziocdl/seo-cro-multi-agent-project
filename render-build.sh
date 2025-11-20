#!/usr/bin/env bash
# exit on error
set -o errexit

# Atualizar pip
pip install --upgrade pip

# Instalar dependências Python
pip install -r requirements.txt
