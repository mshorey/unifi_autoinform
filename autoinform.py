import nmap
import paramiko

def ssh_command(ip, username, password, command):
    # create an instance of the SSH client
    client = paramiko.SSHClient()
    # automatically add the remote server's SSH key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # connect to the remote server using the provided credentials
        client.connect(ip, username=username, password=password)
        # execute the provided command on the remote server
        stdin, stdout, stderr = client.exec_command(command)
        # print success message
        print(f'Successful login to {ip}')
        # print the output of the command
        print(stdout.read().decode('utf-8'))
    except paramiko.ssh_exception.AuthenticationException:
        # print error message if authentication failed
        print(f'Failed to login to {ip}')
    except paramiko.ssh_exception.SSHException:
        # print error message if there was an error connecting to the remote server
        print(f'Error connecting to {ip}')
    finally:
        # close the connection to the remote server
        client.close()
# specify the subnet to scan
subnet = "192.168.123.0/24"
# specify the username and password for authentication
username = "ubnt"
password = "ubnt"
# specify the command to be executed on the remote server
command = "mca-cli-op set-inform http://YOURCONTROLLERIPHERE:8080/inform"

# create an instance of the nmap scanner
scanner = nmap.PortScanner()
# scan the specified subnet for open SSH ports
scanner.scan(subnet, arguments='-p 22 --open')

# loop through all the hosts that have open SSH ports
for host in scanner.all_hosts():
    # execute the ssh_command function on each host
    ssh_command(host, username, password, command)