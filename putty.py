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

    def exec_bash(self, cmd: str) -> int:
        """
        Run bash command remotely
        :param cmd:
        :return: Error code. Check plink man
        """
        file_name = "cmd.tmp"
        with open(file_name, "w") as f:
            f.write(cmd)
        result = os.system(f'{self.plink} -no-antispoof {self.user}@{self.ip} -pw {self.password} -m {file_name}')
        os.remove(file_name)
        return result

    def copy_files(self, src: str, dst: str) -> int:
        """
        Copy file or files from Windows to Linux via SSH
        :param src: Source could be both directions. Examples:
            putty.copy_files(r"G:\\koshi8bit\\*", r"/home/koshi8bit")
            putty.copy_files(r"G:\\koshi8bit\\requirements.txt", r"/home/koshi8bit")
            putty.copy_files(r"G:\\koshi8bit\\requirements.txt", r"/home/koshi8bit/some.file")
        :param dst: Destination could be both directions
        :return: Error code. Check pscp man
        """
        return os.system(f'{self.pscp} -r -pw {self.password} "{src}" {self.user}@{self.ip}:{dst}')
