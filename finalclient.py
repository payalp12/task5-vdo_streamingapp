import socket as s
import cv2
import pickle
import struct

client_s = s.socket(s.AF_INET,s.SOCK_STREAM)
host_ip = '192.168.43.168' 
port = 1234



client_s.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")



while True:
    while len(data) < payload_size:
        packet = client_s.recv(2160) 
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_s.recv(2160)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("client side",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_s.close()

