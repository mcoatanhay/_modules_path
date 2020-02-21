#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: help_mes_modules_path_compose.py
# Auteur: Marc COATANHAY

"""
    Module pour écrire un fichier d'aide du module.
"""

# Import des modules
import mes_modules_path
from repertoire import filerep
import sys

# Définitions constantes et variables globales
filerep()
file = open('help.txt', 'w')
sys.stdout = file
help(mes_modules_path)
file.close()
sys.stdout = sys.__stdout__

# Définitions fonctions et classes

