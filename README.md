# ejass-duckietown-view

## Запуск

1. Скачиваете репозиторий и заходите в корень проекта
2. `bash docker/build.sh`
3. `bash docker/start.sh`
4. Перейти на http://localhost:9000/video

> Наружу торчит только 9000 порт 

> Сейчас конфиг использует тестовый rtsp -  rtsp://5.19.248.97:8554/mystream


## Конфиг для 3501

**docker-compose.yaml**

```yaml
version: "3"

services:
  web:
    build: .
    expose:
      - "5000"
    container_name: ejass
  camera_0:
    image: eroji/rtsp2mjpg
    restart: always
    expose:
      - "8090"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      RTSP_URL: rtsp://admin:@10.135.4.240/trackID=1
      FFSERVER_LOG_LEVEL: error
      FFMPEG_LOG_LEVEL: warning
      FFMPEG_INPUT_OPTS: -use_wallclock_as_timestamps 1
      FFMPEG_OUTPUT_OPTS: -async 1 -vsync 1
    container_name: camera_0
  camera_1:
    image: eroji/rtsp2mjpg
    restart: always
    expose:
      - "8090"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      RTSP_URL: rtsp://admin:@10.135.4.239/trackID=1
      FFSERVER_LOG_LEVEL: error
      FFMPEG_LOG_LEVEL: warning
      FFMPEG_INPUT_OPTS: -use_wallclock_as_timestamps 1
      FFMPEG_OUTPUT_OPTS: -async 1 -vsync 1
    container_name: camera_1
  camera_2:
    image: eroji/rtsp2mjpg
    restart: always
    expose:
      - "8090"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      RTSP_URL: rtsp://admin:@10.135.4.238/trackID=1
      FFSERVER_LOG_LEVEL: error
      FFMPEG_LOG_LEVEL: warning
      FFMPEG_INPUT_OPTS: -use_wallclock_as_timestamps 1
      FFMPEG_OUTPUT_OPTS: -async 1 -vsync 1
    container_name: camera_2
  camera_3:
    image: eroji/rtsp2mjpg
    restart: always
    expose:
      - "8090"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      RTSP_URL: rtsp://admin:@10.135.4.237/trackID=1
      FFSERVER_LOG_LEVEL: error
      FFMPEG_LOG_LEVEL: warning
      FFMPEG_INPUT_OPTS: -use_wallclock_as_timestamps 1
      FFMPEG_OUTPUT_OPTS: -async 1 -vsync 1
    container_name: camera_3
  camera_4:
    image: eroji/rtsp2mjpg
    restart: always
    expose:
      - "8090"
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      RTSP_URL: rtsp://admin:@10.135.4.236/trackID=1
      FFSERVER_LOG_LEVEL: error
      FFMPEG_LOG_LEVEL: warning
      FFMPEG_INPUT_OPTS: -use_wallclock_as_timestamps 1
      FFMPEG_OUTPUT_OPTS: -async 1 -vsync 1
    container_name: camera_4

  nginx:
    image: nginx:alpine
    restart: always
    links:
      - camera_0
      - camera_1
      - camera_2
      - camera_3
      - camera_4
      - web
    ports:
      - "9000:80"
    volumes:
      - ./rtsp2mjpg/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
    container_name: nginx_ejass
```


### IP камер

 ```yaml
  - rtsp://admin:@10.135.4.240/trackID=1
  - rtsp://admin:@10.135.4.239/trackID=1
  - rtsp://admin:@10.135.4.238/trackID=1
  - rtsp://admin:@10.135.4.237/trackID=1
  - rtsp://admin:@10.135.4.236/trackID=1

```