import commands
import os

class GitPkg:
    def __init__(self, name: str, link: str, install_dir: str, check_if_exists: bool) -> None:
        self.name = name
        self.link = link
        self.install_dir = install_dir
        self.prg_location = f"{self.install_dir}/{self.name}"
        self.check_if_exists = check_if_exists
        self.dir_exists: bool = os.path.isdir(self.prg_location)

    def git_clone(self) -> None:
        if self.check_if_exists and self.dir_exists:
            return
        git_cmd = ["git", "clone"]
        git_cmd.append(self.link)
        git_cmd.append(self.prg_location)
        print(f"Cloning package {self.name}...")
        commands.execute(cmd=git_cmd)

    def install(self) -> None:
        if self.check_if_exists and self.dir_exists:
            return
        self.git_clone()
        make_cmd = ["sudo", "make", "-C", self.prg_location, "install"]
        print(f"Installing package {self.name}...")
        commands.execute(cmd=make_cmd)

def install_arch_packages(pkgs: list[str]) -> None:
    pacman_cmd = ["sudo", "pacman", "-S"]
    pacman_cmd += pkgs
    commands.execute(cmd=pacman_cmd)

def install_aur_packages(pkgs: list[str]) -> None:
    aur_cmd = ["sah", "-i"]
    aur_cmd += pkgs
    commands.execute(cmd=aur_cmd)

def install_git_packages(pkgs: list[GitPkg]) -> None:
    for pkg in pkgs:
        pkg.install()


