from putty import Putty

if __name__ == '__main__':
    putty = Putty(r'G:\koshi8bit\putty',
                  'bnct',
                  '192.168.1.222')
    putty.exec_bash(
"""
rm -rf /home/services/shared-folders/src
mkdir -p /home/services/shared-folders/src/{smb,auto-clear}
""")

    putty.copy_files(r"src\*", "/home/services/dhcp")
    putty.copy_files(r"src\docker-compose.yml", "/home/services/dhcp")

    putty.exec_bash(
"""
cd /home/services/shared-folders/src/smb/
docker-compose down && docker-compose build && docker-compose up -d
""")
