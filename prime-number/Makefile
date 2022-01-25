run:
	./venv/bin/python3 main.py 

# Esse comando cria o virtualenv 
create-virtualenv:
	virtualenv -p python3 venv 
clean:
	rm -rf venv 

docker-build:
	docker build -t kevin .
docker-run:
	docker run -it --rm kevin 
