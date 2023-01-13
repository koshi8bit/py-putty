from putty import Putty

if __name__ == '__main__':
    putty = Putty(r'G:\koshi8bit\soft\windows\01-osnovnoe\SSH\putty',
                  'bnct',
                  '192.168.1.222')

    dst = "/dst/path"
    putty.copy_files(r"src\docker-compose.yml", dst)
    putty.copy_files(r"src\Dockerfile", dst)
    putty.copy_files(r"src\*", dst)

    putty.exec_bash(
"""
cd "/dst/path"
docker-compose down && docker-compose build && docker-compose up -d
""")
