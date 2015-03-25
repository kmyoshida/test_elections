#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# u'Code du département',
# u'Libellé du département',
# u'Code du canton',
# u'Libellé du canton',
# u'Code de la commune',
# u'Libellé de la commune',
# u'Inscrits',
# u'Abstentions',
# u'% Abs/Ins',
# u'Votants',
# u'% Vot/Ins',
# u'Blancs',
# u'% Blancs/Ins',
# u'% Blancs/Vot',
# u'Nuls',
# u'% Nuls/Ins',
# u'% Nuls/Vot',


# u'Exprimés',
# u'% Exp/Ins',
# u'% Exp/Vot',
# 
# u'N°Panneau',
# u'Nuance',
# u'Binôme',
# u'Voix',
# u'% Voix/Ins',
# u'% Voix/Exp',

df = pd.read_excel("Dep_15_Resultats_com_T1_c.xlsx", skiprows=2)


# Build the list of suffixes
# ['', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9', '.10']
suffixes = ["", ] + ["." + str(i) for i in xrange(1,11)]

df = df.drop([
"Date de l'export",
u'% Abs/Ins',
u'% Vot/Ins',
u'% Blancs/Ins',
u'% Blancs/Vot',
u'% Nuls/Ins',
u'% Nuls/Vot',
u'% Exp/Ins',
u'% Exp/Vot',
], axis=1)





df.rename(columns={
u'Code du département':'dpt_code',
u'Libellé du département': 'dpt_name',
u'Code du canton': 'canton_code',
u'Libellé du canton': 'canton_name',
u'Code de la commune': 'commune_code',
u'Libellé de la commune': 'commune_name',
u'Inscrits': 'inscr',
u'Abstentions': 'abst',
# u'% Abs/Ins',
u'Votants': 'vot',
# u'% Vot/Ins',
u'Blancs':'blcs',
# u'% Blancs/Ins',
# u'% Blancs/Vot',
u'Nuls': 'nuls',
# u'% Nuls/Ins',
# u'% Nuls/Vot',
u'Exprimés': 'expr',
# u'% Exp/Ins',
# u'% Exp/Vot',
}, inplace=True)



# Retrieve the list of nuances
# ['BC-XXX', ...]
nuances = set()
for s in suffixes:
	nuances = nuances.union(df['Nuance'+s].unique())
nuances = list(nuances)
nuances = [x for x in nuances if str(x) != 'nan']

# Normalize
for s in suffixes:
	for  nu in nuances:
		df[nu]=df[df['Nuance'+s]==nu]['Voix']

for s in suffixes:
	df = df.drop([
		u'N°Panneau'+s,
		u'Nuance'+s,
		u'Binôme'+s,
		u'Voix'+s,
		u'% Voix/Ins'+s,
		u'% Voix/Exp'+s], axis=1)