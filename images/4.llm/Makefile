.PHONY: build

name = llm

build:
	docker build -t kenpu/$(name) .

test:
	@docker run -it --rm --name test \
		-p 8888:8888 \
		-v $(PWD)/test.py:/tmp/test.py \
		--gpus all \
		kenpu/$(name) python /tmp/test.py

try:
	@docker run -it --rm --name test \
		-p 8888:8888 \
		-v $(PWD)/test.py:/tmp/test.py \
		--gpus all \
		kenpu/$(name) bash


clean:
	docker rmi kenpu/$(name)
