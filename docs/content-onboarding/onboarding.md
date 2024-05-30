# Prepare your work environment

Help us to improve this guide. Practice the GitHub workflow by improving or by adding something to this [guide](https://github.com/TUC-NT-DF/student-guide).

!!! hint
    Every student of our team should contribute with at least **two commits** to this guide to make it better and to extend it. The easiest way is to look for problems **you** have with our onboarding process. Identify missing or incomplete pieces in this guide and improve it using the forking workflow. **Additionally**, choose one issue from the issue tracker of this project and solve it. Thank you 👍


# System requirements

In order to install and use our tools, you need one of the following platforms:
- Windows 10 (Intel 64-bit) or higher
- Ubuntu 22.04 (Intel 64-bit) or higher

# Secure your laptop or notebook computer

Some of you will be provided with a notebook computer. This happens if you are an experienced member of the student team or if you are working remotely.

We give you the maximum of flexibility to configure the computer to your needs. So please act responsibly and:

- Install a clean Windows 10 or Linux Ubuntu operating system.
- Encrypt the HDD and/or all partitions. This is necessary to protect our and your work in the case of computer loss.
  - Windows: use Bitlocker or [VeraCrypt](https://www.veracrypt.fr/en/Home.html)
  - Linux: use [full harddrive encyption](https://help.ubuntu.com/community/Full_Disk_Encryption_Howto_2019)
  - Windows / Ubuntu dual boot: [Bitlocker and encrypted Ubuntu system partition](https://www.mikekasberg.com/blog/2020/04/08/dual-boot-ubuntu-and-windows-with-encryption.html)
- fully encrypt your USB flash drives and external USB harddisks as well
- backup your system and data regularly (daily)

Setup Bitlocker on Windows 10:

* go to control Panel -> system and security -> BitLocker Drive Encryption
* select the drive you want to encrypt
* enter a password
* <b>important: backup your recovery key</b>

![sorry, image not available](../assets/Bitlocker.png "")

## Install the following tools

This also applies if your use your own computer.

### Windows

* IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/)
* install the following extensions in VSCode:
    * markdownlint to [edit \(.md\) files](https://code.visualstudio.com/Docs/languages/markdown#_editing-markdown)
    * GitHub Pull Requests as [Git client](https://code.visualstudio.com/docs/sourcecontrol/github)
* if you need to write JavaScript code and you don't have a good JS IDE available yet, consider one of the followings:
    * [Visual Studio Ultimate Edition](https://visualstudio.microsoft.com/de/downloads/)
    * [Webstorm](https://www.jetbrains.com/webstorm/)
* Install [CMake](https://cmake.org/)
* Install [Git](https://git-scm.com/)

### Linux
* IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/)
* [Webstorm](https://www.jetbrains.com/webstorm/) (if you need to write JavaScript)
* editing markup \(.md\) files: [Visual Studio Code](https://code.visualstudio.com/)
* Git client: A console-based Git client should already be on your system. (called `git`)  
  If you want a GUI, you can try installing `git-gui` or use the CLion plugin "Git Integration". (You do *not* need the GitHub or GitLab plugins.)
* Use your system's package manager to install *CMake*. There is a curses based terminal GUI and a Qt based GUI.

### macOS
* IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/)
* [Visual Studio Code](https://code.visualstudio.com/) for editing markdown files (`.md`)
* If you need to write JavaScript: [WebStorm](https://www.jetbrains.com/webstorm/)

* [Git](https://git-scm.com/) is typically pre-installed on macOS. Verify by opening Terminal and typing `git --version`.
    - If not installed, install Xcode Command Line Tools, which includes Git.

* Install [Homebrew](https://brew.sh/) (for package management) and use homebrew to install [CMake](https://cmake.org/).


## Prepare for GitHub access


For a detailed understanding of GitHub access with SSH keys go to this [link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) in the GitHub docs.



### Windows

#### Generate SSH keys


* open a windows powershell
* type `ssh-keygen -t ed25519 -C "ssh-key-TUC"`
* the command prompt will ask for a file name and passphrase: keep it empty and press enter until you see the following statement;
* `Your identification has been saved in C:\Users\...\.ssh\id_ed25519`




#### Configure your SSH


* open a Windows PowerShell
* cd into the `.ssh` folder (was at `C:\Users\...\.ssh`)
* create an empty text file `config` (**without** a file extension) and this can done via

```
echo "This is sample text" > config
```
* open the file with a text editor and type

```
# github.com account
Host github.com
 HostName github.com
 User INSERT-YOUR-USERNAME-HERE
 IdentityFile ~/.ssh/id_ed25519
```

* save and close the file (**without** a file extension). Make sure to use "UTF-8" encoding system when editing the file, this can be done using Notepad++ or in Visual Studio click on the encoding system right bottom > Save with encoding > UTF-8 . 

!!! hint
    1. Prefer [Notepad++](https://notepad-plus-plus.org/), [Visual Studio Code](https://code.visualstudio.com/), or Notepad to view the files. The files contain both the key and the key title. 
    2. Next login to Github > setting > SSH and GPG keys > New SSH key. Make sure to paste the key under key section and title under title section. (Look for steps under the 'Deploy SSH Public Key to GitHub' heading below.)

**Ignore** the statement "Before you can add an SSH key you need to generate it." You just created this key.


### Linux (works for MacOS as well)


#### Generate SSH keys

* Create a public/private key pair using the ssh-keygen commandline tool.  
  It is recommended to use the default paths for the keys.
* Deploy your public SSH key \(usually stored in ~/.ssh/id\_rsa.pub\) [here](https://github.com/settings/keys).
* Additionally, specifically on Ubuntu, it might be necessary to do `ssh-add`. Look [here](https://stackoverflow.com/questions/6167905/git-clone-through-ssh).

### Deploy SSH Public Key to GitHub

* Go to [SSH keys](https://github.com/settings/keys) settings in GitHub.
* Click on `New SSH key` button.
* Enter `Title` of your choice (e.g. `ssh-key-TUC`).
* Set `Key Type` as `Authentication Key`.
* Paste your public key from the file that was generated (`C:\Users\...\.ssh\id_ed25519.pub`) into the `Key` field.
* Incase you are not sure what the key is, open a command prompt and type
```
cat ~/.ssh/id_ed25519.pub
```
* You will see ssh-ed25519 ... .. . ssh-key-TUC, make sure to copy paste the entire thing to the key field.
* Click on `Add SSH Key` button.
![Deploy Public SSH Key to GitHub](../assets/deploy-ssh-key.png "Deploy Public SSH Key to GitHub")

#### Test your SSH key setup

* open Windows Powershell OR Linux terminal bash
* type `ssh -T git@github.com`
* agree to add *github.com* to the list of trusted hosts
* Run the above command once more, and you should only receive a *Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.* message.

If the welcome message doesn’t appear, run SSH’s verbose mode by replacing `-T` with `-vvvT` to understand where the error is.

Guide for test your SSH connection is [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

## Additional Steps
* Install Miniconda \(based on Python 3\) by following the [Conda How-To](https://draive.com/link_dev/guide/01_Conda_Setup/) and install the most important dependencies.
* [Create an avatar](http://avatarmaker.com/) for your GitHub account. Add it to your GitHub [profile](https://github.com/settings/profile).

## Prepare for software version control

**please read and follow the instructions carefully!**

[The GitHub workflow used by our team...](working-with-GitHub.md)

# Meeting and communication with your supervisor

Meet your supervisor regularly. If you have a meeting,

* Always bring your paper notebook. (see below)
* Always bring your laptop.
* Be well prepared to explain what you were supposed to do, what the results are, how you solved problems and what the next steps are.
* Do not be late. If you realise that you will be late, call your supervisor immediately and/or send a signal message or SMS \(see below\).

In addition to email most of our team uses encrypted messaging. Please consult your supervisor which encryped messenger to use - or just install both :)

- Primary: [element - a secure communications platform](https://element.io/)
- Backup: [Signal messenger](https://whispersystems.org/)

## Write down all your findings

Please use an old-school paper notebook \(minimum size: DIN A5\) to write down your tasks, findings, ideas, results. Do not use notebooks where sheets can easily come off nor single sheets of paper. They get lost easily. Have this notebook ready during your work and in our meetings.

![sorry, image not available](../assets/student-onboarding-notebook.png "paper notebook for your notes")


# How to develop software with less pain

Read the [PC3](../content-ops/PC3.md) file which describes the rules of software development our team chose to follow.

# Recommended programming books

We are a polyglot programming team. We are OK with using multiple languages and we try to use the right tool for the job.

Since we focus on algorithm development, the C++ language is our primary choice for fast and powerful code.

Just "googling" is not enough to become a good programmer! Read some good books:

**Basic**

* Programming: Principles and Practice Using C++ \(Bjarne Stroustrup\)

**Advanced**

* Effective C++: 55 Specific Ways to Improve Your Programs and Designs \(Scott Meyers\)  
\(read this book _before_ you read "Effective Modern C++"\)

* Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14 \(Scott Meyers\)

* Design Patterns \(Erich Gamma\) _and_ [here](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Code/Design_Patterns)

# How to do research

You are working in a research lab now. Bill Freeman's very true article describes what that means:

[How to do research, March 6, 2013 Bill Freeman, CSAIL, MIT](http://people.csail.mit.edu/billf/publications/How_To_Do_Research.pdf)

# Cross-Cultural communication

Are you wondering about the German business and working culture? This guide from the _Deutsche Gesellschaft für Internationale Zusammenarbeit \(GIZ\)_ provides some insights:

[Cross-Cultural Management: How to Do Business with Germans - A Guide –](https://www.managerprogramm.de/wp-content/uploads/2020/03/Kavalchuk-How_to_do_business_with_Germans-EN.pdf)

# FAQ

**Q:** I have seen that some students do not follow the userguide. For example some do not have an avatar. How should I proceed in that way? Should I follow the userguide or should I do what other students are doing / not doing?

**A:** Please follow the userguide. If you don't understand some contents, ask your supervisor and help to improve the guide.

If other students behave different from the workflow described in the userguide ask them why they do so. If they provide a reasonable explanation, discuss with your supervisor.

Some students do not follow the userguide because they do not know it or they decided to ignore it. Do not worry about it.

In order to become smarter, we do not recommend you to ignore the hints we are providing in the userguide ;)

The userguide is the only source of truth during the onboarding process.

**Q:** My work follows the *target condition* (TC) method. Since I work very hard, I do not have time to update the target condition. What should I do?

**A:** Updating the target condition is part of your work and the target condition itself. You should take into account the additional time when estimating your due date. The past has shown that successful students need only 5..10 minutes to update their target condition.

**Q:** What should I do when I realize that I will miss the due date of my target condition?

**A:** When you realize that you will miss your due date, please do as follows:

- describe in the issue why you will miss the due date **before the due date has passed**
  - why was your estimate wrong, what happened
    - pro tip: try to be honest to yourself: if you have bad time management, say it ... and improve it ;)
  - what will you do to have a better estimate next time
  - estimate a new due date and update the TC issue
  - inform your supervisor that you will miss the due date and that you have updated the issue

**Q:** I do not know how to estimate the due date. What should I do?

**A:** Every student in our team should be able to estimate the amount of time he/she needs to reach a target condition (finish a task). If you have problems estimating the time, choose a smaller target condition. A one day duration is a good start.
