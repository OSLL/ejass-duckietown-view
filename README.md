# ejass-duckietown-view

## Запуск

1. Скачиваете репозиторий и заходите в корень проекта
2. `bash docker/build.sh`
3. `bash docker/start.sh`
4. Перейти на http://localhost:9000/video

> Наружу торчит только 9000 порт 

> В обычном docker-compose(для теста) используется тестовый rtsp -  rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov


## Конфиг для 3501

**docker-compose-3501.yaml**

### IP камер

 ```yaml
  - rtsp://admin:@10.135.4.240/trackID=1
  - rtsp://admin:@10.135.4.239/trackID=1
  - rtsp://admin:@10.135.4.238/trackID=1
  - rtsp://admin:@10.135.4.237/trackID=1
  - rtsp://admin:@10.135.4.236/trackID=1

```
