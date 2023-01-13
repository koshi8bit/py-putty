from putty import Putty

if __name__ == '__main__':
    putty = Putty(r'G:\koshi8bit\soft\windows\01-osnovnoe\SSH\putty',
                  'bnct',
                  '192.168.1.222')

    dst = "/dst/path"

    putty.exec_bash(
f"""
docker-compose down
rm -rf {dst}
mkdir -p {dst}
""")

    putty.copy_files(r"src\docker-compose.yml", dst)
    putty.copy_files(r"src\Dockerfile", dst)
    putty.copy_files(r"src\*", dst)

    putty.exec_bash(
f"""
cd {dst}
docker-compose build && docker-compose up -d
""")
