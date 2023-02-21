import os
import requests
import subprocess
import ctypes

# define function to run subprocess commands with admin privileges
def run_as_admin(command):
    if os.name != 'nt':
        raise RuntimeError("This function only works on Windows.")
    try:
        print("step 1")
        return subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("step2")


    except :
        try:
            print("step 3")
            return subprocess.run(['runas /user:Administrator',command], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("Error: %s" % e.output)
            raise RuntimeError("Command '%s' returned non-zero exit status %d" % (e.cmd, e.returncode))


# download 7-Zip
print("Downloading 7-Zip...")
response = requests.get("https://www.7-zip.org/a/7z2201-x64.exe")

# save 7-Zip to disk
with open("7zip.exe", "wb") as file:
    file.write(response.content)

# install 7-Zip
print("Installing 7-Zip...")
run_as_admin('7zip.exe /S')

# wait for 7-Zip to install
import time

time.sleep(5)


# add 7-Zip to system PATH
print("Adding 7-Zip to system PATH...")
run_as_admin('set PATH=%PATH%;C:\Program Files\7-Zip')
run_as_admin('echo $PATH')
run_as_admin('7z')


# # check if 7-Zip is installed
# try:
#     subprocess.run(['7z --version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print("7-Zip has been installed successfully!")
# except FileNotFoundError:
#     print("Error: 7-Zip was not installed correctly.")
#     exit()


# # download FFmpeg
# print("Downloading FFmpeg...")
# response = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z")

# # save FFmpeg to disk
# with open("ffmpeg.7z", "wb") as file:
#     file.write(response.content)

# # extract FFmpeg
# print("Extracting FFmpeg...")
# subprocess.call('7z x ffmpeg.7z -oC:\\ffmpeg -y', shell=True)

# # add FFmpeg to system PATH
# print("Adding FFmpeg to system PATH...")
# subprocess.call('setx /M PATH "%PATH%;C:\\ffmpeg\\bin"', shell=True)

# # check if FFmpeg is installed
# try:
#     subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print("FFmpeg has been installed successfully!")
# except FileNotFoundError:
#     print("Error: FFmpeg was not installed correctly.")
#     exit()




