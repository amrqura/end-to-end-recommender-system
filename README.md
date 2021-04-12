# activate Virtual env:

```
virtualenv venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
```
# install and open notebook from the virtual environment:
```
python -m pip install ipykernel
ipython kernel install --user --name=RecommederSystem
jupyter lab &
```
# Build docker image
cd service
docker build -t content-base-recommender .
# run docker container
docker run -d --publish 7777:5000 content-base-recommender

# make sure that the docker run locally (from docker):
http://localhost:7777/recommend/-1479311724257856983


aws configure set region eu-west-1 --profile personal
aws ecr  --region eu-west-1 create-repository --repository-name ecs-recommener-system/home

$(aws ecr get-login  --region eu-west-1 --no-include-email)

docker tag content-base-recommender:latest 477557400504.dkr.ecr.eu-west-1.amazonaws.com/ecs-recommener-system/home:latest

docker push 477557400504.dkr.ecr.eu-west-1.amazonaws.com/ecs-recommener-system/home:latest
