#!/bin/bash  

#####  APP specific variables  #######
DOCKER_USER=linuxep
IMAGE_NAME=lepv
IMAGE_TAG=latest

CONTAINER_NAME=lepv
CONTAINER_PORT=80
HOST_BIND_PORT=80
######################################

echo "running containers:"
docker ps
echo ""

echo "stop and remove existing container below:"
docker rm -f ${CONTAINER_NAME}

echo ""
echo "port mapping:"
echo "host:container = "${HOST_BIND_PORT}":"${CONTAINER_PORT}
echo ""

docker run -p ${HOST_BIND_PORT}:${CONTAINER_PORT} --name ${CONTAINER_NAME} -t ${DOCKER_USER}/${IMAGE_NAME}':'${IMAGE_TAG}
