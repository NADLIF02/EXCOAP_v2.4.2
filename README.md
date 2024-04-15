clear

docker compose down

git pull

docker-compose build

docker-compose up -d

docker ps

docker ps -a

docker logs v23-web-1

git clone https://github.com/NADLIF02/v2.3.git 

docker stop $(docker ps -aq)  # Arrête tous les conteneurs en cours d'exécution
docker rm $(docker ps -aq)    # Supprime tous les conteneurs

docker rmi $(docker images -aq)  # Supprime toutes les images

docker system prune  # Nettoie tous les composants inutilisés

docker system prune --volumes
