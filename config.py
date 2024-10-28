from dorothy import Dorothy, Dotfile
from packages import GitPkg

conf = Dorothy()

conf.home_dir = "/home/miguel"
conf.dotfiles_dir = conf.home_dir + "/dotfiles"

# zsh configuration
zshrc = Dotfile(conf.dotfiles_dir + "/zshrc", conf.home_dir + "/.zshrc")

# sblocks configuration
sblocks_dir = conf.home_dir + "/.config/sblocks"
sblocks_config = Dotfile(conf.dotfiles_dir + "/sblocks/config.toml", sblocks_dir + "/config.toml")

# Neovim configuration
initvim_dir = conf.home_dir + "/.config/nvim"
initvim = Dotfile(conf.dotfiles_dir + "/init.vim", initvim_dir + "/init.vim")

# Font configuration
font_dir = "/etc/fonts"
fontconf = Dotfile(conf.dotfiles_dir + "/fonts/local.conf", font_dir + "/local.conf")

# Keyboard configuration
keyboard_conf = Dotfile(conf.dotfiles_dir + "/vconsole.conf", "/etc/vconsole.conf")

# xinitrc
xinitrc = Dotfile(conf.dotfiles_dir + "/xinitrc", conf.home_dir + "/.xinitrc")

# dotfiles to install
conf.dotfiles = [ 
                 zshrc, 
                 sblocks_config, 
                 initvim,
                 fontconf,
                 keyboard_conf,
                 xinitrc
                 ]

# projects directory
projects_dir = conf.home_dir + "/dev/projects"

# directories to create
conf.create_dirs = [
                    sblocks_dir, 
                    initvim_dir, 
                    font_dir,
                    projects_dir
                    ]

conf.arch_pkgs = ["git", "base-devel", "xorg", "xorg-xinit", "neovim", "brightnessctl", "neofetch", "alsa-utils", "pcmanfm", "pamixer", "zsh-syntax-highlighting", "zsh", "ripgrep", "noto-fonts"]
conf.aur_pkgs = ["brave-bin", "pfetch"]


ndwm = GitPkg(name="ndwm", link="https://github.com/miguelnto/ndwm", install_dir=projects_dir,) 
libtoml = GitPkg(name="libtoml", link="https://github.com/miguelnto/libtoml", install_dir=projects_dir, )
sah = GitPkg(name="sah", link="https://github.com/miguelnto/sah", install_dir=projects_dir, )
sblocks = GitPkg(name="sblocks", link="https://github.com/miguelnto/sblocks", install_dir=projects_dir, )
st = GitPkg(name="st", link="https://github.com/miguelnto/st", install_dir=projects_dir, )
scripts = GitPkg(name="scripts", link="https://github.com/miguelnto/scripts", install_dir=projects_dir, )

conf.git_pkgs = [
                 sah,
                 libtoml,
                 scripts,
                 sblocks,
                 ndwm,
                 st,
                ] 

dotfs = GitPkg(name="dotfiles", link="https://github.com/miguelnto/dotfiles", install_dir = conf.home_dir, )
conf.git_pkgs_to_clone = [ dotfs ]

