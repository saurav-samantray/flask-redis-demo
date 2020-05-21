# flask-redis-demo
Demo web application that will use flask microframwork and redis as cache. flask and redis has been dockerized using compose and redis data been mounted on a volume to retain data even on restart or failure.

## To build the docker image and run the application
`
cd flask-demo-redis
docker-compose up --build
`

## To run the already built docker image
`
cd flask-demo-redis
docker-compose up
`

## Access the demo application
`
http://localhost:8000/
`

## Retaining redis data
docker compose has been written to mount redis data on a disk volume which would mean redis data is retained even when application and redis server is restarted. You can remove the volume mount logic in docker compose if you don't want to retain the redis data on restart.