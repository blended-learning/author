.PHONY: all prepare
name = "debug"
note = Blah blah
ssh_port = 8022
web_port = 8088
cpus = 8
memory = 8G
home_path = $(PWD)/data/home/$(name)
user_file = $(PWD)/data/users.$(name)

start: prepare
	docker run --rm -d \
		--name $(name) \
		--cpus $(cpus) \
		--memory $(memory) \
		-p $(ssh_port):22 \
		-p $(web_port):8000 \
		kenpu/uber

stop:
	docker rm -f $(name)

prepare:
	mkdir -p $(home_path)
