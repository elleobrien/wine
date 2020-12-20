build:
	docker build -t wine .

run:
	docker run -v data:/app/data wine
