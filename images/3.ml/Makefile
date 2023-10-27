.PHONY: build

name = ml

build:
	docker build -t kenpu/$(name) .

try:
	docker run -it --rm --name try -p 8888:8888 kenpu/$(name) bash

clean:
	docker rmi kenpu/$(name)
