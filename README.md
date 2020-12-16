Container para execução de script python

Para criar a imagem e fazer o upload no github

docker build -t acarlos01/paramiko:tag .
docker push acarlos01/paramiko:tag


Como executar:

docker run --rm -it acarlos01/paramiko:tag script.py