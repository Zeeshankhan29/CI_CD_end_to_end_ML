# CI_CD_end_to_end_ML


First we need to create virtual env

```
conda create -p myenv2 python=3.10 -y

```

Activate the environment

```
conda activate myenv2

```

Install the packages from requirements.txt

```
pip install -r requirements.txt

```

Now we use dockers and create a docker image

```
docker build . -t ci-cd

```

In github Action add the details

```
HEROKU_EMAIL
HEROKU_API_KEY
HEROKU_APP_NAME
```
Push the code to github then automatically it gets uploaded in Heroku platform

```
git init 
git add .
git commit -m "first commit"
git push origin main

```

