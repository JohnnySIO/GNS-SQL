#!/usr/bin/python
# -*- coding: utf8 -*-

import mysql.connector

connexionBD = None

def getConnexionBD() :
	global connexionBD
	try :
		if connexionBD == None :
			connexionBD = mysql.connector.connect(
					host = 'localhost' ,
					user = 'root' ,
					password = 'azerty' ,
					database = 'gns'
				)
		return connexionBD
	except :
		return None

def getJoueurs() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select *
					from Joueur;
				'''
		curseur.execute( requete , () )
		
		enregistrements = curseur.fetchall()
		
		lesJoueurs = []
		for unEnregistrement in enregistrements :
			unJoueur = {}
			unJoueur['numeroJoueur'] = unEnregistrement[ 0 ]
			unJoueur['nomJoueur'] = unEnregistrement[ 1 ]
			unJoueur['mdpJoueur'] = unEnregistrement[ 2 ]
		curseur.close
		return lesJoueurs
	except :
		return None
		
def getCouleur() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select *
					from Couleur;
				'''
		curseur.execute( requete , () )
		
		enregistrements = curseur.fetchall()
		
		lesCouleurs = []
		for unEnregistrement in enregistrements :
			uneCouleur = {}
			uneCouleur['numeroCouleur'] = unEnregistrement[ 0 ]
			uneCouleur['nomCouleur'] = unEnregistrement[ 1 ]
		curseur.close
		return lesCouleurs
	except :
		return None
		


def getParties() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select *
					from Partie;
				'''
		curseur.execute( requete , () )
		
		enregistrements = curseur.fetchall()
		
		lesParties = []
		for unEnregistrement in enregistrements :
			unePartie = {}
			unePartie['numeroPartie'] = unEnregistrement[ 0 ]
			unePartie['dateCreation'] = unEnregistrement[ 1 ]
			unePartie['numeroJoueur'] = unEnregistrement[ 2 ]
			unePartie['numeroJoueur_1'] = unEnregistrement[ 3 ]
			unePartie['numeroJoueur_2'] = unEnregistrement[ 4 ]
			unePartie['numeroJoueur_3'] = unEnregistrement[ 5 ]
			unePartie['numeroCouleur'] = unEnregistrement[ 6 ]
			unePartie['numeroCouleur_1'] = unEnregistrement[ 7 ]
			lesJoueurs = getJoueurs()
			for unJoueur in lesJoueurs :
				if unePartie['numeroJoueur'] == unJoueur['numeroJoueur'] :
					unePartie['nomInit'] = unJoueur['nomJoueur']
			for unJoueur in lesJoueurs :
				if unePartie['numeroJoueur_1'] == unJoueur['numeroJoueur'] :
					unePartie['nomAdverse'] = unJoueur['nomJoueur']
			lesCouleurs = getCouleur()
			for uneCouleur in lesCouleurs :
				if unePartie['numeroCouleur'] == uneCouleur['numeroCouleur'] :
					unePartie['couleurInit'] = uneCouleur['nomCouleur']
			for uneCouleur in lesCouleurs :
				if unePartie['numeroCouleur_4'] == uneCouleur['numeroCouleur'] :
					unePartie['couleurAdverse'] = uneCouleur['nomCouleur']
			
		curseur.close
		return lesParties
	except :
		return None
