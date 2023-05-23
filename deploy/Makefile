.PHONY: all prepare check
env_file = $(recipe)/env
-include $(env_file)
export

help:
	@echo "Usage: make recipe=<...> start | stop | check"

check:
	@[ "${recipe}" ] \
		|| (echo "[Error] recipe is not specified from command line"; exit 1) \
		&& (echo "recipe = ${recipe}")
	@[ "${name}" ] \
		|| (echo "[Error] name is not set"; exit 1) \
		&& (echo "name = ${name}")
	@[ "${note}" ] \
		|| (echo "[Warning] note is not set") \
		&& (echo "note = ${note}")
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

ifeq ($(note),)
note = "$(recipe) runtime environment"
endif

path=$(realpath $(recipe))

start: check
	docker run --rm -d \
		--name $(name) \
		$(memory_args) $(cpus_args) \
		$(ssh_args) $(web_args) \
		-e site_name="$(note)" \
		-v $(path)/repos.json:/etc/repos.json \
		-v $(path)/users.default:/etc/users.default \
		kenpu/uber

stop:
	docker rm -f $(name)
