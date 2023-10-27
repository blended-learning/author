.PHONY: build

build:
	docker build -t kenpu/llm .

try:
	docker run -it --rm --name try -p 8888:8888 kenpu/uber bash

clean:
	docker rmi kenpu/uber
