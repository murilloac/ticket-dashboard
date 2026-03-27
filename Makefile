install:
	pip install -r app/requirements.txt

run:
	streamlit run app/main.py

test:
	pytest -v

docker-build:
	docker build -t ticket-dashboard-devops .

docker-run:
	docker run -p 8501:8501 ticket-dashboard-devops
docker-compose-up:
	docker compose up --build