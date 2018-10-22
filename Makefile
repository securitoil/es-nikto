.PHONY: build push test

build: template
	faas build -f es_nikto.yml --build-arg "ADDITIONAL_PACKAGE=nikto"

template:
	faas template pull https://github.com/securitoil/faas-templates.git


push:
	docker push kulinacs/es_nikto

test:
	tox
