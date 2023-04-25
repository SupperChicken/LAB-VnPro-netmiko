#netmiko : Multi-vendor library to simplify legacy CLI connections to network devices
#import netmiko
from netmiko import ConnectHandler  

#ConnectHandle(device_type = "cisco_ios", ) -> không khuyến nghị
# khai báo kiểu dictionary

#khai báo biến router
Router = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.5",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321", #password enable for router cisco
}

#ConnectHandler(**Router)  # truyền biến vào hàm connecthandler theo kiểu unpack
connect=ConnectHandler(**Router)
#user, privileges, config

#send lệnh cho router
show_int=connect.send_command("show ip interface brief")
print("show interface")
print(show_int)

#enable mode privileges
connect.enable()
show_run=connect.send_command("show run")
print("show running configuration")
print(show_run)

#send_config_set function : lệnh cấu hình cho thiết bị
#cấu hình host name:
host_name=connect.send_config_set("hostname R1-Netmiko-Python")
print ("lệnh cấu hình")
print(host_name)

#cấu hình ip, no shutdown
config_ip=connect.send_config_set(["int e0/2","no shut","ip add 192.168.2.1 255.255.255.0"])
print ("lệnh cấu hình")
print(config_ip)

#cấu hình hàng loạt:
#dùng vòng lập for: lấy từ điểm 1 đến điểm 3
for i in range(1, 4):
    config_ip_loop=connect.send_config_set(["int e0/"+ str(i),"no shut","ip add 192.168."+ str(i)+".1 255.255.255.0"])
    print ("lệnh cấu hình hàng loạt")
    print(config_ip_loop)

#in các dữ liệu vừa đẩy vào:
print (show_int)
#do kiểu biến i là srting nên mình phải chuyển i sang srt bằng srt(i)
#w3school
#string, interger, float (1,2; 8,4;...)
#concatenate (nối chuỗi)

#đối với trường hợp thực tế ip và cổng không thể tự tăng thi mình phải tạo biến theo ý:

"""
e0/1: 192.168.12.1
e0/1: 192.168.15.5
e0/2: 192.168.21.3
"""
#khai báo biến dictionary cho các interface:
interfaces ={
    "e0/1": "192.168.12.1",
    "e0/2": "192.168.15.5",
    "e0/3": "192.168.21.3"
}

print("---------------------------------")
for i in interfaces:
    config_int_loop2=connect.send_config_set(["int " +i, "ip address " + interfaces[i] +" 255.255.255.0", "no shut"])
    print(config_int_loop2)
print(show_int)


#thoát khỏi thiết bị
connect.disconnect()