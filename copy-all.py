from putty import Putty

if __name__ == '__main__':
    putty = Putty(r'G:\koshi8bit\soft\windows\01-osnovnoe\SSH\putty',
                  'bnct',
                  '192.168.1.222')
    putty.exec_bash(
"""
rm -rf /home/services/shared-folders/src
mkdir -p /home/services/shared-folders/src/{smb,auto-clear}
cp /home/services/shared-folders/{.env,/src/smb/}
""")
    putty.copy_files(r"G:\koshi8bit\prog\linux\github\utils\samba\src\docker-compose.yml",
                     r"/home/services/shared-folders/src/")
    putty.copy_files(r"G:\koshi8bit\prog\linux\github\utils\samba\src\smb\*",
                     r"/home/services/shared-folders/src/smb")
    putty.copy_files(r"G:\koshi8bit\prog\linux\github\utils\samba\src\auto-clear\src\*",
                     r"/home/services/shared-folders/src/auto-clear")
    putty.copy_files(r"G:\koshi8bit\prog\linux\github\utils\samba\src\auto-clear\requirements.txt",
                     r"/home/services/shared-folders/src/auto-clear")
    putty.copy_files(r"G:\koshi8bit\prog\linux\github\utils\samba\src\auto-clear\Dockerfile",
                     r"/home/services/shared-folders/src/auto-clear")
    putty.exec_bash(
"""
cd /home/services/shared-folders/src/smb/
docker-compose down && docker-compose build && docker-compose up -d
""")
