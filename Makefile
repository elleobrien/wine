build:
	docker build -t wine .

run:
	docker run --mount type=bind,source=${PWD}/data,target=/home/trainer/app/data wine 
