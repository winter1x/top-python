# tcp/ip udp http
"""
сокеты sockets
tcp transmission control protocol
протокол управления передачей
клиент - серверная архитектура

особенности:
установка соединения
гарантирует доставку данных
управление потоком
контроль ошибок

особенности2:
может быть медленнее чем udp или другие протоколы
поток байтов
соединение нужно закрыть

сокеты (sockets)
сервер - слушаем
клиент - подключение

try:
    clint_sock.connect(('localhost', 8000))
except ConnectionRefusedError:
    print('сервер не отвечает')

enconde - кодировка
decode - декодирование

методы socket:
bind - связать
listen - слушать
accept - принять
connect - подключиться
send - отправить
recv - получить

трехстороннее рукопожатие
клиент послыает SYN
сервер отвечает SYN+ACK
клиент получает ACK
"""


#задание 1:
"""
клиент сначала отправляет команду "UPLOAD" или "DOWNLOAD"
если UPLOAD - передает файл
если DOWNLOAD - сервер ищет файл и возвращает его содержимое
"""

# tcp/ip
"""
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip-address
port
dns
"""

"""
ConnectionRefusedError - не отвечает
NetworkUnreachableError - ip недоступен
GetHostByNameError - dns не может преобразовать ip

ping <ip>
tracert / traceroute
netstat
telnet <ip> <port>
"""

# задание 2:
"""
сервер - вывод ip каждого клиента (слушает ip port), одновременные подключения 
клиент - узнает ip по dns (получает и выводит ответ от сервера)
tcp передача
логирование ip + port входящих клиентов
только socket