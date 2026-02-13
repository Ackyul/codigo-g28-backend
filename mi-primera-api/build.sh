#!/usr/bin/env bash

set -o errexit

# instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# ejecutar migracion
flask db upgrade

