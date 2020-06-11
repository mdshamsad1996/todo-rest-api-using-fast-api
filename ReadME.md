Assignment:

Create a basic todo rest Api and ability to add/delete/update/modify todo. 

Note: Use FastAPI as framework <https://fastapi.tiangolo.com/> and Motor <https://motor.readthedocs.io/en/stable/index.html> as MongoDb Driver. Also it’s better if you can dockerized the whole application

Steps:

Make sure python (preferred python3.6) is added to path.

python --version or python3.6 --version 

#### First install docker and start service on amazon linux machine using below command

     sudo yum install docker -y
     sudo service docker start
#### Install docker compose using below command

   a. Install docker compose
   ```
   sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
   ```
   b. For Permission

   ```
   sudo chmod +x /usr/local/bin/docker-compose
   ```
   c. Create a symbolic link
   ```
   ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
   ```
  check docker-compose --version
  ```
  docker-compose --version
  ```
 Steps:
 run below command
```docker-compose up```

After executing, we will have two containers on our host one for our Mongo db and my-app-container .

For running web application open the brwoser and goto EC2-ip-address:8000/items

To destroy the container run below command

```docker-compose down --rmi all```
