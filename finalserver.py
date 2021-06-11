import socket as s
import cv2
import pickle
import struct


server_s = s.socket(s.AF_INET,s.SOCK_STREAM)
host_name  = s.gethostname()
host_ip = s.gethostbyname(host_name)


port = 1234
s_address = ('192.168.43.168',port)



server_s.bind(s_address)




server_s.listen(5)




while True:
    client_s,addr = server_s.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_s:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_s.sendall(message)
            
		
            cv2.imshow('Server side',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_s.close()

