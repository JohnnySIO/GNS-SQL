#!/usr/bin/python
# -*- coding: utf8 -*-

import mysql.connector
import datetime
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
		
def getCouleurs() :
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
					
			lesCouleurs = getCouleurs()
			
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
		
def getPartie(numeroPartie) :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select *
					from Partie
					where numeroPartie = %s
				'''
		curseur.execute( requete , (numeroPartie , ) )
		
		enregistrement = curseur.fetchone()
		
		numPartie = {}
		if enregistrement != None :
			numPartie['numeroPartie'] = enregistrement[0]
			numPartie['dateCreation'] = str(enregistrement[1])
			numPartie['Initiateur'] = enregistrement[2]
			numPartie['Adversaire'] = enregistrement[3]
			numPartie['Vainqueur'] = enregistrement[4]
			numPartie['Suivant'] = enregistrement[5]
			numPartie['CouleurInit'] = enregistrement[6]
			numPartie['CouleurAdverse'] = enregistrement[7]
		curseur.close()
		return numPartie
	
	except :
		return None
		
def supprimerPartie(numeroPartie) :
	try:
		if getPartie(numeroPartie) == {} :
			return False
		curseur = getConnexionBD().cursor()

		requete = '''
			delete from Partie
			where numeroPartie = %s
			'''
		curseur.execute(requete, ( numeroPartie , ) )
		
		connexionBD.commit()
		curseur.close()
		
		return True
	except:
		return None

def creerPartie( numeroInitiateur , numeroCouleurInitiateur ) :
	try :
		numPartie = len(getParties())+1
		dateCreation = datetime.date.today()
		curseur = getConnexionBD().cursor()
		
		requete = '''
			insert into Partie values(%s,%s,%s,null,null,%s,%s,null)
			'''
		curseur.execute(requete, ( numPartie , dateCreation , numeroInitiateur , numeroInitiateur , numeroCouleurInitiateur ) )
		
		connexionBD.commit()
		curseur.close
		if getPartie(numPartie)['numeroPartie'] == {} :
			return -1
		else :
			return numPartie
	except :
		return None
