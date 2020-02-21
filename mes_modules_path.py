#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: mes_modules_path.py
# Auteur: Marc COATANHAY

"""
    Ajout du path nécessaire à l'importation de modules personnels.
    Changer la valeur de "repertoire" avec l'adresse à laquelle se trouvent
    les modules perso.
"""

# Import des modules
import sys

# Définitions constantes et variables globales
repertoire = 'c:\\users\\mc\\mu_code\\_mes_modules\\'
sys.path.append(repertoire)
print('mes modules path :', repertoire)

# Définitions fonctions et classes
