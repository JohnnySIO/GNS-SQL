# Liste des parties terminées

select *
from Partie
where numeroJoueur_2 is not null; # numeroJoueur_2 = Vainqueur

# Liste des parties actuellment en cours

select *
from Partie
where numeroJoueur_3 is not null; # numeroJoueur_3 = Suivant

# Liste des parties en attente d un joueur

select *
from Partie
where numeroJoueur is null # numeroJoueur = Initiateur
or numeroJoueur_1 is null; # numeroJoueur_1 = Adversaire

# Liste des parties terminées de Cody

select *
from Partie
where numeroJoueur_2 is not null # numeroJoueur_2 = Vainqueur
and numeroJoueur = 5 # numeroJoueur = Initiateur
or numeroJoueur_1 = 5; # numeroJoueur_1 = Adversaire

# Liste des parties gagnées par Cody

select *
from Partie
where numeroJoueur_2 = 5 # numeroJoueur_2 = Vainqueur
and numeroJoueur = 5 # numeroJoueur = Initiateur
or numeroJoueur_1 = 5; # numeroJoueur_1 = Adversaire

# Liste des parties initiées par Cody en attente d un adversaire

select *
from Partie
where numeroJoueur = 5 # numeroJoueur = Initiateur
and numeroJoueur_1 is null; # numeroJoueur_1 = Adversaire

# Liste des parties de Cody actuellement en cours

select *
from Partie
where numeroJoueur_3 is not null # numeroJoueur_3 = Suivant
and numeroJoueur = 5 # numeroJoueur = Initiateur
or numeroJoueur_1 = 5; # numeroJoueur_1 = Adversaire

# Liste des parties pour lesquelles Cody doit jouer son tour

select *
from Partie
where numeroJoueur_3 = 5; # numeroJoueur_3 = Suivant

# Liste des parties en attente d un adversaire non initiées par Cody

select *
from Partie
where numeroJoueur != 5 # numeroJoueur = Initiateur
and numeroJoueur_1 is null; # numeroJoueur_1 = Adversaire

