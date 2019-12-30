name = input("Enter name file (ex. hack.txt): ") # получение названия файла
name_1 = input("Enter name file where ip will be saved (ex. clean.txt): ") # получение названия файла с очисткой
ip_file = open(name, 'r+') # открытие файла 
ip_file_read = ip_file.read() # чтение файла
def write_clean(info): # функция записи очистки
	file = open(name_1 ,'x') # создать и открыть файл для записи очистки
	file.seek(0) # курсор в файле на 0 положение
	file.write(info) # запись
clean_host = ip_file_read.replace('Host: ', ' ') # очистка хоста
clean_status = clean_host.replace('Status: Up', ' ') # очистка статуса хоста
clean_port = clean_status.replace('Ports: 80/closed/tcp//http///, 8080/closed/tcp//http-proxy///', ' ') # очистка инфы о портах
clean_close_port = clean_port.replace('Ports: 80/open/tcp//http///, 8080/closed/tcp//http-proxy///', ' ') # очистка инфы о закрытых портах
clean_other_port = clean_close_port.replace('Ports: 80/filtered/tcp//http///, 8080/filtered/tcp//http-proxy///', ' ') # очистка инфы о других портах
clean_other = clean_other_port.replace('Ports: 80/filtered/tcp//http///, 8080/closed/tcp//http-proxy///', ' ') # очистка другой информации
clean_skob = clean_other.replace('()', ' ') # замена скобок на пробел
clean_up = clean_skob.replace('Up', '') # замена up на пустоту
clean_prob = clean_up.replace(' ', '') # замена проблема на пустоту
clean_f = clean_prob.replace('Ports: 80/closed/tcp//http///, 8080/filtered/tcp//http-proxy///', '')
clean_f2 = clean_f.replace('Ports: 80/open/tcp//http///, 8080/filtered/tcp//http-proxy///', '')
ip_file.close() # закрытие файла после очистки 
print(clean_f2) # вывод очищенного файла
write_clean(clean_f2) # вызов функции записи в файл очищенной инфы
print("Successful!") # удача
