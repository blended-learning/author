.PHONY: all prepare check


ifdef recipe
env_file = $(recipe)/env
name = $(notdir $(recipe))
-include $(env_file)
export
endif

ifdef cpus
cpus_args = --cpus $(cpus)
endif

ifdef memory
memory_args = --memory $(memory)
endif

ifdef ssh
ssh_args = -p $(ssh):22
endif

ifdef web
web_args = -p $(web):8000
endif

ifdef home
home_args = -v `realpath $(home)`:/home
endif

ifndef network
network="network_$(name)"
endif

path=$(realpath $(recipe))

docker_cmd = docker run --rm -d \
		--name $(name) \
		--network $(network) \
		$(memory_args) $(cpus_args) \
		$(ssh_args) $(web_args) \
		-e site_name='$(note)' \
		-v $(path)/users:/etc/users.default \
		$(home_args) \
		$(expose_ports_args) \
		$(extra_args) \
		$(image)

all:
	python ls_dockers.py
	@echo "Usage: make recipe=<...> start | stop | check"

check:
	@echo ---------------------------------
	@[ "${recipe}" ] \
		|| (echo "[Error] recipe is not specified from command line"; exit 1) \
		&& (echo "recipe = ${recipe}")
	@[ -d ${recipe} ] || (echo "[Error] Recipe ${recipe} does not exist"; exit 1)
	@[ -f ${recipe}/env ] || (echo "[Error] ${recipe}/env does not exist"; exit 1)
	@[ -f ${recipe}/users ] || (echo "[Error] ${recipe}/users does not exist"; exit 1)
	@[ "${name}" ] \
		|| (echo "[Warning] name is not set") \
		&& (echo "name = ${name}")
	@[ "${note}" ] \
		|| (echo "[Error] note is not set"; exit 1) \
		&& (echo "note = ${note}")
	@[ "${image}" ] \
		|| (echo "[Error] image is not set"; exit 1) \
		&& (echo "image = ${image}")
	@echo "port_base ${port_base}"
	@[ "${ssh}"  ] \
		|| (echo "[Note] ssh is not enabled") \
		&& (echo "ssh = ${ssh}")
	@[ "${web}"  ] \
		|| (echo "[Error] web is not set"; exit 1) \
		&& (echo "web = ${web}")
	@[ "${cpus}" ] \
		|| (echo "[Warning] cpus is not set") \
		&& (echo "cpus = ${cpus}")
	@[ "${memory}" ] \
		|| (echo "[Warning] memory is not set") \
		&& (echo "memory = ${memory}")
	@[ "${home}" ] \
		|| (echo "[Warning] home is not set") \
		&& (echo "home = ${home}")
	@echo "Extra args: ${extra_args}"
	@echo ---------------------------------
	@echo $(docker_cmd)

network:
	docker network inspect $(network) >/dev/null 2>&1 || \
		docker network create --driver bridge $(network)

start: check network
ifdef home
	@mkdir -p `realpath $(home)`
endif
	$(docker_cmd)

stop:
	docker rm -f $(name)
