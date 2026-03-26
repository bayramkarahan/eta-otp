project('eta-otp-lock')

subdir('po')

install_subdir('src', install_dir: '/usr/share/etap/eta-otp', strip_directory: true)
install_data('pam/pam_otp.py', install_dir: '/usr/libexec/')
install_data('pam/pam-auth-update', install_dir: '/usr/share/pam-configs/', rename: 'totp')
install_data('data/tr.org.etap.otp-settings.policy', install_dir: '/usr/share/polkit-1/actions/')
install_data('data/eta-otp.svg', install_dir: '/usr/share/icons/hicolor/scalable/apps/')
install_data('data/tr.org.etap.otp-settings.desktop', install_dir: '/usr/share/applications')
