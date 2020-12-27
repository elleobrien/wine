build:
	docker build -t wine .

run:
	docker run \
		--mount type=bind,source=${HOME}/.config/gcloud/application_default_credentials.json,target=/etc/gcp.json \
		-e GOOGLE_APPLICATION_CREDENTIALS=/etc/gcp.json \
		wine 

copy-report:
	docker cp wine:/home/trainer/app/report.md ./report.md
