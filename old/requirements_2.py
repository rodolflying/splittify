import subprocess as sp
import getpass

# Get the user's password for authentication
password = getpass.getpass(prompt='Enter your password: ')

# Run the program with admin privileges
prog = sp.Popen(['runas', '/user:Administrator', '7zip.exe'], stdin=sp.PIPE)
prog.stdin.write(f'{password}\n'.encode())
prog.communicate()

DESKTOP-AK2KHCL