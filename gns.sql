#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------

drop database if exists gns;
create database gns default character set utf8 default collate utf8_general_ci ;
use gns;
#------------------------------------------------------------
# Table: Joueur
#------------------------------------------------------------

CREATE TABLE Joueur(
        numeroJoueur Int NOT NULL ,
        nomJoueur    Varchar (25) NOT NULL ,
        mdpJoueur    Varchar (25) NOT NULL ,
        PRIMARY KEY (numeroJoueur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Couleur
#------------------------------------------------------------

CREATE TABLE Couleur(
        numeroCouleur Int NOT NULL ,
        nomCouleur    Varchar (25) NOT NULL ,
        PRIMARY KEY (numeroCouleur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Partie
#------------------------------------------------------------

CREATE TABLE Partie(
        numeroPartie    Int NOT NULL ,
        dateCreation    Date NOT NULL ,
        numeroJoueur    Int ,
        numeroJoueur_1  Int ,
        numeroJoueur_2  Int ,
        numeroJoueur_3  Int ,
        numeroCouleur   Int ,
        numeroCouleur_4 Int ,
        PRIMARY KEY (numeroPartie )
)ENGINE=InnoDB;

ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur FOREIGN KEY (numeroJoueur) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_1 FOREIGN KEY (numeroJoueur_1) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_2 FOREIGN KEY (numeroJoueur_2) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroJoueur_3 FOREIGN KEY (numeroJoueur_3) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroCouleur FOREIGN KEY (numeroCouleur) REFERENCES Couleur(numeroCouleur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_numeroCouleur_4 FOREIGN KEY (numeroCouleur_4) REFERENCES Couleur(numeroCouleur);


# Insertion des joueurs

insert into Joueur values (1,"Nicolas","azerty");
insert into Joueur values (2,"Ilona","azerty");
insert into Joueur values (3,"George","azerty");
insert into Joueur values (4,"Aïcha","azerty");
insert into Joueur values (5,"Cody","azerty");

#Insertion des couleurs

insert into Couleur values (1,"Blanc");
insert into Couleur values (2,"Noir");

#Insertion des parties

insert into Partie values(1,"01/05/18",5,2,2,null,1,2);
insert into Partie values(2,"01/05/18",5,2,5,null,2,1);
insert into Partie values(3,"01/05/18",5,null,null,5,1,null);
insert into Partie values(4,"01/05/18",2,null,null,null,2,null);
insert into Partie values(5,"02/05/18",5,1,null,1,1,2);
insert into Partie values(6,"02/05/18",5,1,null,5,1,2);
insert into Partie values(7,"02/05/18",1,null,null,null,null,2);
insert into Partie values(8,"02/05/18",1,null,null,null,null,2);
insert into Partie values(9,"03/05/18",5,2,null,2,1,2);
insert into Partie values(10,"03/05/18",2,1,2,null,2,1);
