# List All containers
docker ps -a

# Stop and remove all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Remove all networks
# docker network prune --force
docker network rm $(docker network ls -q)

# Remove all volumes
# docker volume prune --force
docker volume rm $(docker volume ls -q)

# List All containers
docker ps -a
