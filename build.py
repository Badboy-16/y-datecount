'''

This script will complete the following actions - 

Install dependency.
Build the programme from source.
Make the build binary executable.
'''

import subprocess

def install_dep():
    subprocess.call("pip3 install pyinstaller", shell=True)

def build_from_src():
    subprocess.call("pyinstaller -F -n ydatecount __main__.py", shell=True)

def make_executable():
    subprocess.call("cd dist && chmod +x ydatecount", shell=True)

def main_build():
    install_dep()
    build_from_src()
    make_executable()

main_build()
