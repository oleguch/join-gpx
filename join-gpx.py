import sys
import xml.etree.ElementTree as ET

argv = sys.argv[2:]
first_file_name = sys.argv[1]
# читаем первый файл, берем его за основу
tree = ET.parse(first_file_name)
root = tree.getroot()

# используемые namespace в файле
ns = {'xmlns': 'http://www.topografix.com/GPX/1/1'}
# список всех координат
all_tracks = root.find('xmlns:trk/xmlns:trkseg', ns)

#читаем оставшиеся файлы
for file_name in argv:
	file = ET.parse(file_name)
	for item in file.findall('xmlns:trk/xmlns:trkseg/xmlns:trkpt', ns):
		# добавляем в список всех координат координаты из файлов
		all_tracks.append(item)	

# добавляем namespace в итоговый файл и сохраняем
ET.register_namespace("", "http://www.topografix.com/GPX/1/1")
tree.write('full.gpx')
print('Файл сохранен как full.gpx')
