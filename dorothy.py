from dataclasses import dataclass
import subprocess
import packages

@dataclass
class Dotfile:
    name: str = ""
    real_location: str = ""

@dataclass
class Directory:
    src: str
    root_access: bool

def cp_cmd(dotf: Dotfile) -> list[str]:
    return ["sudo", "cp", "-vf", dotf.name, dotf.real_location]

def cp(dotf: Dotfile) -> None:
    subprocess.run(cp_cmd(dotf), capture_output=False, check=True)

def mkdir_cmd(direc: str) -> list[str]:
    return ["sudo", "mkdir", "-vp", direc]

def mkdir(direc: Directory) -> None:
    mk_cmd = mkdir_cmd(direc.src)
    if not direc.root_access:
        mk_cmd.pop(0)
    subprocess.run(mk_cmd, capture_output=False, check=True)

class Dorothy:
    def __init__(self, dotfiles_dir: str = "", home_dir: str = "") -> None:
        self.dotfiles: list[Dotfile] = []
        self.dotfiles_dir: str = dotfiles_dir
        self.home_dir: str = home_dir
        self.create_dirs: list[Directory] = []
        self.aur_pkgs: list[str] = []
        self.arch_pkgs: list[str] = []
        self.git_pkgs: list[packages.GitPkg] = []
        self.git_pkgs_to_clone: list[packages.GitPkg] = []

    def install_dotfiles(self) -> None:
        for dotfile in self.dotfiles:
            cp(dotfile)

    def create_dirs_if_not_exists(self) -> None:
        if len(self.create_dirs) > 0:
            for direc in self.create_dirs:
                mkdir(direc)

    def install_arch_packages(self) -> None:
        packages.install_arch_packages(self.arch_pkgs)

    def install_aur_packages(self) -> None:
        packages.install_aur_packages(self.aur_pkgs)

    def clone_git_packages(self) -> None:
        for pkg in self.git_pkgs_to_clone:
            pkg.git_clone()

    def install_git_packages(self) -> None:
        packages.install_git_packages(self.git_pkgs)


