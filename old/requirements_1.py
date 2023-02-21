import subprocess as sp

# run a program that does not require admin privileges
# sp.check_call(['7zip.exe'])

# run a program that requires admin privileges
prog = sp.Popen(['runas', '/noprofile', '/user:DESKTOP-AK2KHCL\domainadmin', '7zip.exe'], stdin=sp.PIPE)
# DESKTOP-AK2KHCL

# enter the password for the admin user
prog.stdin.write('111111')

# communicate with the program
prog.communicate()