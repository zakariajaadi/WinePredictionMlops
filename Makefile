#buid flow image command
build-flow-image:
	docker build -t flow-image -f Dockerfile .

#docker compose commands
compose-up-core:
	docker-compose --profile core up -d
compose-up-serving:
	docker-compose --profile serving up -d
compose-up-app:
	docker-compose --profile app up -d
compose-down:
	docker-compose --profile app down

# Deploy all pipelines in prefect server ( important! : app profile docker compose must be up)
deploy-all-flows:
	python src/main.py



