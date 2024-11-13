


On a copié le fichier json vers le conteneur routeur 1:

docker cp ./Abooks.json routeur_1:/Abooks.json

Il faut ensuite initialiser mongo en faisant:

mongod

On se connecte au routeur 1 

Puis importé le fichier json dans mango depuis le conteneur:

docker exec -it routeur_1 mongoimport --db books --collection books --file /Abooks.json


Installation du package pymongo pour le fichier de config en python pour MongoDB

pip install pymongo

On teste quelques requêtes pour voir si la base fonctionne:

db.books.find()
db.books.exists()
