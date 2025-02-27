# simple_chat

docker save -o backend_twin2.tar backend_twin2

docker save -o frontend_twin2.tar frontend_twin2

docker load -i backend_twin2.tar


docker load -i frontend_twin2.tar

docker-compose up -d