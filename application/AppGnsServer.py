#!/usr/bin/python
# -*- coding: utf8 -*-
from flask import *
from modeles import modeleGns

app = Flask(__name__)
app.secret_key = 'gns'

@app.route( '/parties' , methods = ['GET'] )
def getLesParties() :
	lesParties = modeleGns.getParties()
	corpsReponse = json.dumps( lesParties )
	reponse = make_response( corpsReponse )
	reponse.mimetype = 'application/json'
	reponse.status_code = 200
	return reponse
	
@app.route( '/parties/<numeroPartie>' , methods = ['GET'] )
def consulterPartie(numeroPartie) :
	laPartie = modeleGns.getPartie(numeroPartie)
	corpsReponse = json.dumps( laPartie )
	reponse = make_response( corpsReponse )
	reponse.mimetype = 'application/json'
	reponse.status_code = 200
	return reponse
	
@app.route( '/parties/<numeroPartie>' , methods = ['DELETE'] )
def annulerPartie(numeroPartie) :
	laPartie = modeleGns.supprimerPartie(numeroPartie)
	corpsReponse = json.dumps( laPartie )
	reponse = make_response( corpsReponse )
	reponse.mimetype = 'application/json'
	reponse.status_code = 200
	return reponse
	
@app.route( '/parties' , methods = ['POST'] )
def initierPartie() :
	laPartie = modeleGns.creerPartie( numeroInitiateur , numeroCouleurInitiateur )
	corpsReponse = json.dumps( laPartie )
	reponse = make_response( corpsReponse )
	reponse.mimetype = 'application/json'
	reponse.status_code = 200
	return reponse
if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )
