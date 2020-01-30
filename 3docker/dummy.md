```bash
# 런시작부터 사고치기 전까지 
(base) C:\Users\admin>docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes y0ngma/eda
73379f1b33b92ec792b8d6b3091d7bcdfc70f76481e40b1cd06847dc4e16cc09

(base) C:\Users\admin>docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                    PORTS                                                                                    NAMES
73379f1b33b9        y0ngma/eda            "/usr/local/bin/entr…"   6 seconds ago       Up 4 seconds              4444/tcp, 0.0.0.0:6006-6015->6006-6015/tcp, 8080/tcp, 0.0.0.0:8888-8889->8888-8889/tcp   eda
15192982cae8        mongo                 "docker-entrypoint.s…"   2 weeks ago         Exited (0) 8 days ago                                                                                              mongodb
7054253e8c8e        truevoly/oracle-12c   "/entrypoint.sh "        2 weeks ago         Exited (137) 2 days ago                                                                                            oracle12c

(base) C:\Users\admin>docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
y0ngma/eda            latest              f2d1aa6daa08        3 hours ago         6.85GB
y0ngma/eda            <none>              9ef721f2dd23        26 hours ago        6.76GB
mongo                 latest              a0e2e64ac939        6 weeks ago         364MB
truevoly/oracle-12c   latest              21789d4d876f        11 months ago       5.7GB

(base) C:\Users\admin>docker commit eda
sha256:dc2eb973d0f6aa61c23c3573857347e9b9cbe1cd1ecead782abef1d99cac2bc9

(base) C:\Users\admin>docker commit eda y0ngma/eda
sha256:f2302667879070a4572c7ee20d34112fe46469af844026993ec32c3b7eafa28b

(base) C:\Users\admin>docker pull y0ngma/eda
Using default tag: latest
latest: Pulling from y0ngma/eda
Digest: sha256:c377bed0b4ee9529e83836db83e5cc39814d24e09be741761370bf6afb429c9c
Status: Downloaded newer image for y0ngma/eda:latest
docker.io/y0ngma/eda:latest

(base) C:\Users\admin>docker images
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
<none>                <none>              f23026678790        37 seconds ago      6.86GB
<none>                <none>              dc2eb973d0f6        51 seconds ago      6.86GB
y0ngma/eda            latest              9ef721f2dd23        26 hours ago        6.76GB
mongo                 latest              a0e2e64ac939        6 weeks ago         364MB
truevoly/oracle-12c   latest              21789d4d876f        11 months ago       5.7GB


```