Container para execução de script python com a lib paramiko

Para criar a imagem:

docker build -t acarlos01/paramiko:tag .

Como executar:

docker run --rm -it -v "$PWD:/app" acarlos01/paramiko:tag python /app/script.py

Para visualizar as libraries instaladas no container execute:

docker run --rm -it acarlos01/paramiko:tag pip list