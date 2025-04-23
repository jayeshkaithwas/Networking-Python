# Networking-Python

This repository contains Python scripts related to networking, demonstrating various concepts and practical applications.

## Available Scripts

- [UDP Client](#1-udp_clientpy)
- [TCP Client](#2-tcp_clientpy)
- [TCP Server](#3-tcp_serverpy)
- [SSH Server](#4-ssh_serverpy)
- [SSH Command Executor](#5-ssh_cmdpy)
- [SSH Remote Command Executor](#6-ssh_rcmdpy)
- [Packet Sniffer (IP Header Decoder)](#7-sniffer_ip_header_decoderpy)
- [TCP Proxy](#8-proxypy)
- [Netcat Clone](#9-netcatpy)
- [Traceroute Script](#10-traceroutepy)
- [Email Validator](#11-email_validatorpy)

## Scripts

### 1. `udp_client.py`

A simple UDP client script that:
- Sends a message (`AAABBBCCC`) to a target host and port.
- Receives a response from the server.

#### Code Highlights:
- Utilizes the `socket` library for UDP communication.
- Configures the target host (`127.0.0.1`) and port (`9997`).
- Demonstrates basic send and receive operations in UDP.

#### How to Use:
1. Make sure a corresponding UDP server is running on the target host and port.
2. Run the script:
   ```bash
   python udp_client.py
   ```
3. View the server's response in the console.

#### Example Output:
```
Response from server: Hello, Client!
```

---

### 2. `tcp_client.py`

A simple TCP client script that:
- Connects to a specified host and port.
- Sends a message (`ABCDEF`) to the server.
- Receives and prints the server's response.

#### Code Highlights:
- Utilizes the `socket` library for TCP communication.
- Configures the target host (`0.0.0.0`) and port (`9998`).
- Demonstrates basic connect, send, and receive operations in TCP.

#### How to Use:
1. Ensure a corresponding TCP server is running on the target host and port.
2. Run the script:
   ```bash
   python tcp_client.py
   ```
3. View the server's response in the console.

#### Example Output:
```
Response from server: Welcome to the server!
```

---

### 3. `tcp_server.py`

A multi-threaded TCP server script that:
- Listens for incoming connections on a specified host and port.
- Accepts connections from multiple clients.
- Receives messages from clients and sends an acknowledgment (`ACK`).

#### Code Highlights:
- Utilizes the `socket` library for TCP communication.
- Employs the `threading` module to handle multiple client connections concurrently.
- Configures the server to listen on `0.0.0.0` and port `9998`.

#### How to Use:
1. Run the script to start the server:
   ```bash
   python tcp_server.py
   ```
2. The server will listen for incoming connections and log connection details.
3. Connect to the server using a TCP client (e.g., `tcp_client.py`).

#### Example Output:
```
[*] Listening on 0.0.0.0:9998
[*] Accepted connection from 127.0.0.1:12345
[*] Received: ABCDEF
```

---

### 4. `ssh_server.py`

A custom SSH server script that:
- Implements SSH server functionalities using the `paramiko` library.
- Authenticates users based on predefined credentials (`username: kali`, `password: root`).
- Listens for incoming SSH connections on a specified host and port.
- Accepts commands from authenticated clients and sends responses.

#### Code Highlights:
- Utilizes `paramiko` for SSH transport and authentication.
- Configures the server to listen on `192.168.0.108` and port `2222`.
- Employs threading to handle multiple client connections concurrently.

#### How to Use:
1. Generate an RSA private key file (e.g., `test_rsa.key`) and place it in the same directory as the script.
   ```bash
   ssh-keygen -t rsa -f test_rsa.key
   ```
2. Run the script to start the SSH server:
   ```bash
   python ssh_server.py
   ```
3. Connect to the server using an SSH client (e.g., `ssh` command-line tool):
   ```bash
   ssh kali@192.168.0.108 -p 2222
   ```
4. Authenticate with the password `root` and interact with the server.

#### Example Output:
```
[+] Listening for connection ...
[+] Got a connection! <socket object> ('192.168.0.105', 56789)
[+] Authenticated!
Welcome to bh_ssh
```

---

### 5. `ssh_cmd.py`

A script for executing commands on a remote SSH server:
- Connects to an SSH server using provided credentials.
- Executes a specified command and prints the output.

#### Code Highlights:
- Utilizes the `paramiko` library for SSH communication.
- Prompts the user for server IP, port, username, password, and command.
- Handles authentication and command execution over SSH.

#### How to Use:
1. Run the script:
   ```bash
   python ssh_cmd.py
   ```
2. Enter the required details when prompted (IP, port, username, password, command).
3. View the command output in the console.

#### Example Interaction:
```
Username: kali
Password: 
Enter server IP: 192.168.0.106
Enter port or <CR>: 2222
Enter command or <CR>: id
 --- Output ---
uid=1000(kali) gid=1000(kali) groups=1000(kali)
```

---

### 6. `ssh_rcmd.py`

A script for executing remote commands via SSH and receiving their output:
- Connects to a remote SSH server using provided credentials.
- Sends and receives commands interactively.

#### Code Highlights:
- Utilizes the `paramiko` library for SSH communication.
- Handles interactive command execution through a custom SSH session.
- Uses `subprocess` and `shlex` to execute commands on the server.

#### How to Use:
1. Run the script:
   ```bash
   python ssh_rcmd.py
   ```
2. Enter the required details when prompted (IP, port, username, password).
3. Interact with the server by sending commands and receiving their output.

#### Example Interaction:
```
Enter User: kali
Password: 
Enter server IP: 192.168.0.106
Enter port: 2222
 --- Output ---
ClientConnected
ls
file1.txt file2.txt
exit
```

---

### 7. `sniffer_ip_header_decoder.py`

A script for sniffing and decoding IP headers from network packets:
- Captures raw network packets.
- Extracts and decodes IP header information such as source and destination addresses, protocol type, etc.

#### Code Highlights:
- Utilizes the `socket` library for raw packet capture.
- Handles IP header parsing using the `struct` library.
- Maps common protocol numbers to protocol names (e.g., TCP, UDP, ICMP).

#### How to Use:
1. Run the script:
   ```bash
   python sniffer_ip_header_decoder.py <host>
   ```
   If no host is specified, the default is `192.168.0.103`.
2. The script will continuously sniff packets on the specified host and display their IP header details.
3. Press `Ctrl+C` to stop the script.

#### Example Output:
```
Protocol: TCP 192.168.0.105 -> 192.168.0.1
Protocol: UDP 192.168.0.106 -> 192.168.0.2
```

#### Notes:
- Requires administrative/root privileges to run.
- Behavior may differ on Windows vs. Unix-based systems due to socket options.

---

### 8. `proxy.py`

A flexible TCP proxy script that:
- Forwards traffic between a local and a remote host.
- Logs and modifies traffic in both directions.

#### Code Highlights:
- Uses `socket` for low-level network operations.
- Implements `hexdump` to inspect data streams.
- Includes customizable `request_handler` and `response_handler` for traffic manipulation.

#### How to Use:
1. Run the script with the required arguments:
   ```bash
   python proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]
   ```
   Example:
   ```bash
   python proxy.py 127.0.0.1 9000 10.12.132.1 9000 True
   ```
2. The proxy will listen on `localhost:localport` and forward traffic to `remotehost:remoteport`.
3. Use the `receive_first` flag (`True` or `False`) to control whether the proxy waits for data from the remote host before forwarding traffic.

#### Example Interaction:
- Traffic logging and hexdumping in both directions.
- Traffic modification using `request_handler` and `response_handler` functions.

#### Notes:
- Useful for testing and debugging network applications.
- Requires basic Python and networking knowledge to customize effectively.

---

### 9. `netcat.py`

A Python-based Netcat clone that:
- Supports both client and server modes for TCP communication.
- Provides functionalities to send and receive files, execute commands, and create reverse shells.

#### Code Highlights:
- Uses `argparse` for command-line argument parsing.
- Utilizes `socket` for TCP communication.
- Implements threading for concurrent server operations.
- Handles different modes of operation: `send`, `receive`, `execute`, and `shell`.

#### How to Use:
1. Run the script with the appropriate arguments:
   ```bash
   python netcat.py -t <target_host> -p <port> -l -c
   ```
   - `-l`: Listen mode (server mode).
   - `-c`: Command shell.
   - `-t`: Target host.
   - `-p`: Port number.

2. Example Usage:
   - Start a Netcat server:
     ```bash
     python netcat.py -t 0.0.0.0 -p 5555 -l -c
     ```
   - Connect to the server as a client:
     ```bash
     python netcat.py -t 127.0.0.1 -p 5555
     ```

3. Additional options can be used for file transfers or command execution.

#### Notes:
- Requires Python 3 and basic networking knowledge to operate.
- Ensure proper firewall settings to allow communication.

---

Here's the README section for `traceroute.py`:  

---

### 10. `traceroute.py`

A Python script that replicates the functionality of the `traceroute` network diagnostic tool:
- Determines the route packets take to a specified destination.
- Reports the IP address, hostname, and round-trip time (RTT) for each hop along the path.

#### Code Highlights:
- Uses `socket` for sending and receiving packets.
- Implements a `create_socket` function to configure ICMP and UDP sockets with varying TTL values.
- Calculates RTT for each hop and handles host resolution.
- Provides an option to save traceroute results to a file.

#### How to Use:
1. Run the script:
   ```bash
   python traceroute.py
   ```
2. Enter the required parameters when prompted:
   - **Destination**: Hostname or IP address of the target.
   - **Maximum Hops**: Maximum number of hops to trace (default is 30).
   - **Timeout**: Timeout in seconds for each hop (default is 2 seconds).

3. Example Input:
   ```
   Enter destination host/IP: google.com
   Enter maximum hops (default 30): 20
   Enter timeout in seconds (default 2): 1
   ```

4. Example Output:
   ```
   Traceroute to google.com
   Hop     IP                  Hostname             Time
   ------------------------------------------------------------
   1       192.168.1.1         myrouter.home        1.23ms
   2       10.0.0.1            -                    2.45ms
   ...
   10      142.250.72.14       fra15s30-in-f14.1e100.net  20.31ms
   ```

5. Optionally, save the results to a file:
   - When prompted, type `y` and provide a filename, or leave it blank to auto-generate.

#### Features:
- Displays hop-by-hop details with RTT.
- Resolves IP addresses to hostnames when possible.
- Saves results to a timestamped text file for later reference.

#### Notes:
- Requires administrative/root privileges to run.
- May behave differently depending on network and operating system configurations.

---

### 11. `email_validator.py`

A Python script that checks the validity of an email address through multiple verification steps. This script helps ensure that an email address is properly formatted, belongs to a valid domain, and actually exists.

#### Features
- **Email Format Validation**: Ensures the email address is in the correct format.
- **Domain Validation**: Verifies that the domain name is valid and not from a disposable email provider.
- **MX Record Check**: Retrieves and checks the domain's MX (Mail Exchange) records.
- **Mailbox Verification**: Attempts to connect to the email server to verify the existence of the email address.
   
#### How It Works

The script follows these steps to validate an email address:

1. **Check for Email Format**: Uses a regular expression to ensure the email address is formatted correctly.
2. **Validate Domain**: Checks if the domain name is valid and not from a known disposable email provider.
3. **Check MX Records**: Resolves the MX records for the domain.
4. **Simulate Email Delivery**: Connects to the email server and simulates sending an email to verify if the email address exists.

#### Example

   ```bash
   python email_validator.py user@example.com
   ```

   Output:

   ```
   Valid email address
   ```
---

More Scripts are Comming soon!!!
