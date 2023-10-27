.PHONY: build

build:
	docker build -t kenpu/uber .

try:
	docker run -it --rm --name try -p 8888:8888 kenpu/uber bash

clean:
	docker rmi kenpu/uber
