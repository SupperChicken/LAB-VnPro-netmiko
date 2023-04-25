# LAB-VnPro-netmiko

configure terminal
hostname R1
interface e0/0
ip address dhcp
no shut
exit
username vnpro password vnpro#123
ip domain-name vnpro.net
crypto key generate rsa
768
ip ssh version 2
line vty 0 4
transport input ssh
login local
exit
enable password vnpro#321
do wr


Router>
Router>enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname R1
R1(config)#interface e0/0
R1(config-if)#ip address dhcp
R1(config-if)#no shut
R1(config-if)#exit
R1(config)#username vnpro password vnpro#123
R1(config)#ip domain-name vnpro.net
R1(config)#crypto key generate rsa
The name for the keys will be: R1.vnpro.net
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 768
% Generating 768 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

R1(config)#ip ssh version 2
R1(config)#line vty 0 4
R1(config-line)#transport input ssh
R1(config-line)#login local
R1(config-line)#exit
R1(config)#enable password vnpro#321
R1(config)#do wr
Building configuration...
[OK]
R1(config)#
*Apr 25 17:15:02.507: %SSH-5-ENABLED: SSH 1.99 has been enabled
R1(config)#
*Apr 25 17:15:11.356: %DHCP-6-ADDRESS_ASSIGN: Interface Ethernet0/0 assigned DHCP address 192.168.100.4, mask 255.255.255.0, hostname R1

R1(config)#


Nên để ip tĩnh, bo domain đi

enable
configure terminal
hostname R1
interface e0/0
ip address 192.168.100.5 255.255.255.0
no shut
exit
username vnpro privilege 15 password vnpro@123
crypto key generate rsa
768
line vty 0 4
transport input ssh
login local
exit
enable password vnpro@123
do wr
