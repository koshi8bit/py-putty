from getpass import getpass
import os


class Putty:
    def __init__(self, putty_path: str, user: str, ip: str):
        self.user = user
        self.ip = ip
        self.plink = os.path.join(putty_path, "plink.exe")
        self.pscp = os.path.join(putty_path, "pscp.exe")

        self.password = getpass(f"Enter '{self.user}' pass: ")
        print(f"user: '{self.user}'; IP: {self.ip}; putty_path: '{putty_path}'")

    def exec_plink(self, cmd: str) -> int:
        file_name = "cmd.tmp"
        with open(file_name, "w") as f:
            f.write(cmd)
        result = os.system(f'{self.plink} -no-antispoof {self.user}@{self.ip} -pw {self.password} -m {file_name}')
        os.remove(file_name)
        return result

    def exec_pscp(self, src: str, dst: str) -> int:
        return os.system(f'{self.pscp} -r -pw {self.password} "{src}" {self.user}@{self.ip}:{dst}')
