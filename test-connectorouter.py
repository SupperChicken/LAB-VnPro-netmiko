from netmiko import ConnectHandler  

Router = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.5",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321", #password enable for router cisco
}


connect=ConnectHandler(**Router)
show_int=connect.send_command("show ip interface brief")
print("show interface")
print(show_int)