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
			unJoueur['numeroJoueur'] = unEnregistrement[0]
			unJoueur['nomJoueur'] = unEnregistrement[1]
			unJoueur['mdpJoueur'] = unEnregistrement[2]
			lesJoueurs.append(unJoueur)
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
			uneCouleur['numeroCouleur'] = unEnregistrement[0]
			uneCouleur['nomCouleur'] = unEnregistrement[1]
			lesCouleurs.append(uneCouleur)
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
			unePartie['numeroPartie'] = unEnregistrement[0]
			unePartie['dateCreation'] = unEnregistrement[1]
			unePartie['Initiateur'] = unEnregistrement[2]
			unePartie['Adversaire'] = unEnregistrement[3]
			unePartie['Vainqueur'] = unEnregistrement[4]
			unePartie['Suivant'] = unEnregistrement[5]
			unePartie['CouleurInit'] = unEnregistrement[6]
			unePartie['CouleurAdverse'] = unEnregistrement[7]
			
			lesJoueurs = getJoueurs()
			
			for unJoueur in lesJoueurs :
				if unePartie['Initiateur'] == unJoueur['numeroJoueur'] :
					unePartie['nomInit'] = unJoueur['nomJoueur']
					
			for unJoueur in lesJoueurs :
				if unePartie['Adversaire'] == unJoueur['numeroJoueur'] :
					unePartie['nomAdverse'] = unJoueur['nomJoueur']
					
			lesCouleurs = getCouleur()
			
			for uneCouleur in lesCouleurs :
				if unePartie['CouleurInit'] == uneCouleur['numeroCouleur'] :
					unePartie['couleurInit'] = uneCouleur['nomCouleur']
			for uneCouleur in lesCouleurs :
				if unePartie['CouleurAdverse'] == uneCouleur['numeroCouleur'] :
					unePartie['couleurAdverse'] = uneCouleur['nomCouleur']
			lesParties.append( unePartie )
			
		curseur.close
		return lesParties
	except :
		return None
