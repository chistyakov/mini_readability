.PHONY : build tests minify

minify : build
	docker run --rm --name mini_readability -v ${PWD}/data:/data -u $$(id -u) mini_readability $(url)

tests : build
	docker run --rm --name mini_readability -u $$(id -u) --entrypoint "python" mini_readability -m pytest ../tests/ -vv

build :
	docker build . -t mini_readability
