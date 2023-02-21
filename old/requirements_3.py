import sys
import os
import traceback
import types

def isUserAdmin():
    if os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))

def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")

    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (tuple, list):

        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None

    return rc


def test():
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.")
        rc = runAsAdmin()
    else:
        print("You are an admin!")
        rc = 0

        # Install 7zip
        install_7zip = 'choco install 7zip -y'
        subprocess.run(install_7zip, shell=True, check=True)

        # Install ffmpeg
        install_ffmpeg = 'choco install ffmpeg -y'
        subprocess.run(install_ffmpeg, shell=True, check=True)

        # Add 7zip and ffmpeg to the system path
        add_to_path = f'setx /M PATH "%PATH%;C:\\Program Files\\7-Zip;C:\\Program Files\\ffmpeg\\bin"'
        subprocess.run(add_to_path, shell=True, check=True)

    x = input('Press Enter to exit.')
    return rc


if __name__ == '__main__':
    test()

