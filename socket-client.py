wordlist = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']
text = []
import socket
import random

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.connect(('104.248.39.146', 27617)) #ip number uncle engineer, server port

while len(text) != 8000: #list ที่ให้มามี 20 คำ ต้องหาคำตอบ w1-w2-w3 จะได้ 20*20*20 จึงกำหนดให้ random ผลไม้ใน list ไปเรื่อยๆ จนกว่าจะครบ 8000 ความเป็นไปได้
    w1 = random.choice(wordlist)
    w2 = random.choice(wordlist)
    w3 = random.choice(wordlist)

    t = '{}-{}-{}'.format(w1,w2,w3)
    server.send(t.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print(t) #print result ที่ส่งค่าไป
    print('Data from Server: ', data_server) #print คำตอบหรือค่าที่ server ส่งกลับมา


server.close()
