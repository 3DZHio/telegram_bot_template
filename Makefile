build:
	sudo docker compose build

up:
	sudo docker compose up -d

down:
	sudo docker compose down

clear_storage:
	sudo rm -rf data/storage/

clear_database:
	sudo rm -rf data/database/
