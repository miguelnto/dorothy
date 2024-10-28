from config import conf

def main():
    # Install arch packages
    conf.install_arch_packages()
    # Install git packages
    conf.install_git_packages()
    # Install aur packages
    conf.install_aur_packages()
    # Create directories for dotfiles
    conf.create_dirs_if_not_exists()
    # Clone git packages
    conf.clone_git_packages()
    # Install the dotfiles 
    conf.install_dotfiles()

    
main()
