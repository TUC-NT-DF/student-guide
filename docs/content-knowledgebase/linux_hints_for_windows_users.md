# Linux hints for Windows users

Our colleague Peter Küffner shares a few notes about avoiding issues that Windows users have, when trying out Ubuntu (e.g. by setting up a Ubuntu VM):

## SSH/SFTP access

- In order to be able to use PuTTY and FileZilla with Ubuntu, you need to install the `openssh-server` package via apt-get. This can be done via

    ```bash
    sudo apt-get install openssh-server
    ```

- No adjustments to the Firewall should be required after the installation. (Just note that you can't log in as *root* user.)
- You can connect to the Ubuntu using FileZilla via SFTP with the username/password you use to log in there.  
    You need to explicitly specify that in the URL.
    e.g. with `sftp://10.0.0.1/`

## Getting GitHub access working

- You need your private SSH key on the machine.
- Then SSH key needs to be in OpenSSH format (*not* PuTTY's ppk).
    You can use PuTTYgen to convert your PPK key into OpenSSH format (`Conversions` menu).  
    Note: OpenSSH "private key" files don't have an extension. "Public key" files end with .pub.
- You can transfer the key to the Ubuntu system. Copy it into `/home/<user>/.ssh/`.
    The file should be named `id_rsa` (for "ssh-rsa" keys) if you don't want to do additional configuration.
- The `id_rsa` file *MUST* have the its file permissions set to `-rw-------` (i.e. only the user itself is allowed to access the file).
    You can use the command `chmod 600 id_rsa` while in the `.ssh` folder in order to set the permissions.  

    !!! warning
        The SSH agent will refuse to accept the key when its file permissions are not set properly!
