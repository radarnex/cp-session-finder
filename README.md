Check Point Session Finder
==========

This script helps find a session in Check Point firewalls in order to drop it 
individually without needing to restart CP services or rebooting the entire 
firewall.

Connection table description and values are explained on the sk65133.

As stated on the SK, most connections will create the following four entries in conns table:
	<0, Client_IP, Client_Port, Server_IP, Server_Port, Protocol_Number> = Client side, inbound
	<1, Client_IP, Client_Port, Server_IP, Server_Port, Protocol_Number> = Server side, outbound
	<0, Server_IP, Server_Port, Client_IP, Client_Port, Protocol_Number> = Server side, inbound
	<1, Server_IP, Server_Port, Client_IP, Client_Port, Protocol_Number> = Client side, outbound

Problem is the values of a connection are in hex so grep is not possible without
doing a conversion.


Example
----------
Want to find sessions that match IP 192.168.1.50 and port 22:

	python cp_session_finder.py 192.168.1.50 22

The script will return a grep'able string which we will use in a expert session. Then
we have to look for a string that ends at '<session_timeout>/<ttl>, e.g.:

	<00000000, c0a80122, 0000d444, c0a80132, 00000016, 00000006; 0001c001, 00044000, 00000000, 
	00000e10, 00000000, 563c438f, 00000000, 3201a8c0, c0000000, 00000001, 00000001, ffffffff, 
	ffffffff, 00000000, 00000000, 00000004, 00000000, 00000000, 00000000, 00000000, 00000000, 
	00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 00000000, 
	8701c800, 00000000, 00000000; 3598/3600>

So our individual session will be:
	
	00000000, c0a80122, 0000d444, c0a80132, 00000016, 00000006

In order to kill it (you need to delete the leading 0s for the direction and 
for the protocol number):
	
	fw tab -t connections -x -e "0,c0a80122,0000d49b,c0a80132,00000016,6" 


ToDo
----------
- Specific session find utilities
- Direct interaction with firewall 
- Unit testing
