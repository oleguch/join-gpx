# join_gpx
Объединение gpx файлов
Аналог https://github.com/oleguch/join_gpx_java, только на Python

## Описание
Обединение двух и более gpx файлов

## Использование
```
python join-gpx 01.gpx 02.gpx 03.gpx
```
на выходе будет один файл full.gpx.

## Как объединяет
Берет первый файл, и добавляет в него в тэг trkseg все элементы trkpt из других файлов
