build:
	docker build -t wine .

run:
	docker run \
	--mount type=bind,source=${PWD}/data,target=/home/trainer/app/data \
	--mount type=bind,source=${PWD}/metrics,target=/home/trainer/app/metrics \
	 wine 
