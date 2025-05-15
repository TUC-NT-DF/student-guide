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

To support your individual needs, we provide you with the maximum flexibility to configure the computer. At the same time, we kindly ask you to use this freedom responsibly and to follow these guidelines:

- Install a clean Windows 10 or Linux Ubuntu operating system.
- Encrypt the hard disk (HDD/SSD) and all partitions. This is essential to protect both your data and our data in case the computer is lost.
    - Windows: Use Bitlocker or [VeraCrypt](https://www.veracrypt.fr/en/Home.html)
    - Linux: Use [Full disk Encryption](https://help.ubuntu.com/community/Full_Disk_Encryption_Howto_2019)
    - Windows / Ubuntu dual boot: [Bitlocker and encrypted Ubuntu system partition](https://www.mikekasberg.com/blog/2020/04/08/dual-boot-ubuntu-and-windows-with-encryption.html)
- Fully encrypt all USB flash drives and external hard drives.
- Backup your system and data regularly (daily backups recommended).

Setup Bitlocker on Windows 10:

- Go to Control Panel -> System and Security -> BitLocker Drive Encryption.
- Select the drive you want to encrypt.
- Turn on BitLocker and set a strong password.
- **Important: Backup your Recovery Key.**

![sorry, image not available](../assets/Bitlocker.png "")

## Install the following tools

This also applies if you use your own computer.

### Windows

- IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/)
- Install the following extensions in VSCode:
    - Markdownlint to [edit \(.md\) files](https://code.visualstudio.com/Docs/languages/markdown#_editing-markdown)
    - GitHub Pull Requests as [Git client](https://code.visualstudio.com/docs/sourcecontrol/github)
- If you need to write JavaScript code and you don't have a good JS IDE available yet, consider one of the followings:
    - [Visual Studio Ultimate Edition](https://visualstudio.microsoft.com/de/downloads/)
    - [Webstorm](https://www.jetbrains.com/webstorm/)
- Install [CMake](https://cmake.org/)
- Install [Git](https://git-scm.com/)

### Linux

- IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/)
- [Webstorm](https://www.jetbrains.com/webstorm/) (if you need to write JavaScript)
- Editing markup \(.md\) files: [Visual Studio Code](https://code.visualstudio.com/)
- Git client: A console-based Git client should already be on your system. (called `git`)  
  If you want a GUI, you can try installing `git-gui` or use the CLion plugin "Git Integration". (You do *not* need the GitHub or GitLab plugins.)
- Use your system's package manager to install *CMake*. There is a curses based terminal GUI and a Qt based GUI.

### macOS

- IDE for software development and debugging: [Visual Studio Code](https://code.visualstudio.com/).
- [Visual Studio Code](https://code.visualstudio.com/) for editing markdown files (`.md`).
- If you need to write JavaScript: [WebStorm](https://www.jetbrains.com/webstorm/).
- [Git](https://git-scm.com/) is typically pre-installed on macOS. Verify by opening Terminal and typing `git --version`.
    - If not installed, install Xcode Command Line Tools, which includes Git.
- Install [Homebrew](https://brew.sh/) (for package management) and use homebrew to install [CMake](https://cmake.org/).


## Prepare for GitHub access


For a detailed understanding of GitHub access with SSH keys go to this [link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) in the GitHub docs.



### Windows

#### Generate SSH keys


- Open a Windows PowerShell
- Type `ssh-keygen -t ed25519 -C "ssh-key-TUC"`
- The command prompt will ask for a file name and passphrase: Keep it empty and press enter until you see the following statement;
- `Your identification has been saved in C:\Users\...\.ssh\id_ed25519`




#### Configure your SSH


- Open *Windows PowerShell*.
- Navigate to your `.ssh` directory:

    ```powershell
    cd C:\Users\<YourUsername>\.ssh
    ```

#### Create SSH Config File

- Create an empty text file named `config` (**without** any file extension).

    ```powershell
    echo "# This is sample text" > config
    ```

- Open the `config` file using a text editor and add the following content:

    ```
    # github.com account
    Host github.com
        HostName github.com
        User INSERT-YOUR-USERNAME-HERE
        IdentityFile ~/.ssh/id_ed25519
    ```

- Save and close the file (**without** any file extension).

    !!! note Important
        Make sure to use "UTF-8" encoding system when editing the file, this can be done using Notepad++ or in Visual Studio click on the encoding system right bottom > Save with encoding > UTF-8.
    !!! hint
        It is recommended to use [Notepad++](https://notepad-plus-plus.org/), [Visual Studio Code](https://code.visualstudio.com/), or Notepad to view the files. The files contain both the key and the key title.


- For the next steps, see the section *Deploy SSH Public Key to GitHub* below.



### Linux (works for MacOS as well)

#### Generate SSH keys

- Create a public/private key pair using the `ssh-keygen` command-line tool.  
  It is recommended to use the default paths for the keys.
- On Ubuntu, it might be necessary to run `ssh-add` to add your SSH key. For more details, refer to this [Stack Overflow article](https://stackoverflow.com/questions/6167905/git-clone-through-ssh).

### Deploy SSH Public Key to GitHub

- To copy the public key: open a command prompt and type
    - in a Linux shell:

        ```bash
        cat ~/.ssh/id_ed25519.pub
        ```

    - or in a Windows PowerShell:

        ```
        Get-Content ~\.ssh\id_ed25519.pub
        ```
    - Ensure you copy the entire SSH key, which begins with `ssh-ed25519 ...` and ends with `ssh-key-TUC.
- Log in to your GitHub account and go to:  
   *Settings* → *SSH and GPG keys* (https://github.com/settings/keys)
- Click on `New SSH key` button.
    - Enter a descriptive title in the Title field (e.g., "ssh-key-TUC").
    - Set `Key Type` as `Authentication Key`.
    - Paste your public key from the file that was generated (`C:\Users\...\.ssh\id_ed25519.pub`) into the `Key` field.
    - Click on the `Add SSH Key` button.

**Note:** You can ignore the message:  *"Before you can add an SSH key, you need to generate it."*  — You have already created your SSH key.

![Deploy Public SSH Key to GitHub](../assets/deploy-ssh-key.png "Deploy Public SSH Key to GitHub")

#### Test your SSH key setup

- Open Windows Powershell OR Linux terminal bash
- Type `ssh -T git@github.com`
- Agree to add *github.com* to the list of trusted hosts
- Run the above command once more, and you should only receive a *Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.* message.

If the welcome message doesn't appear, run SSH's verbose mode by replacing `-T` with `-vvvT` to understand where the error is.

Guide for test your SSH connection is [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

## Additional Steps

- Install Miniconda \(based on Python 3\) by following the [Conda How-To](https://draive.com/link_dev/guide/01_Conda_Setup/) and install the most important dependencies.
- [Create an avatar](http://avatarmaker.com/) for your GitHub account and add it to your GitHub [profile](https://github.com/settings/profile).

## Prepare for software version control

**Please read and follow the instructions carefully!**

[The GitHub workflow used by our team...](working-with-GitHub.md)

# Meeting and communication with your supervisor

Meet with your supervisor regularly. For each meeting, please adhere to the following guidelines:

- Always bring a paper notebook (as outlined below).
- Always bring your laptop.
- Be well-prepared to explain:
    - What tasks you were assigned.
    - What results you have achieved.
    - How you solved any challenges.
    - What the next steps are.
- Arrive on time. If you anticipate being late, immediately contact your supervisor via phone, a signal message or SMS.

In addition to email, most of our team uses encrypted messaging. Please consult your supervisor which encrypted messaging platform to use, or feel free to install both.

- **Primary:** [Element - Secure communications platform](https://element.io/)
- **Backup:** [Signal messenger](https://whispersystems.org/)

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

- Programming: Principles and Practice Using C++ \(Bjarne Stroustrup\)

**Advanced**

- Effective C++: 55 Specific Ways to Improve Your Programs and Designs \(Scott Meyers\)  
\(read this book *before* you read "Effective Modern C++"\)

- Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14 \(Scott Meyers\)

- Design Patterns \(Erich Gamma\) *and* [here](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Code/Design_Patterns)

# How to do research

You are working in a research lab now. Bill Freeman's very true article describes what that means:

[How to do research, March 6, 2013 Bill Freeman, CSAIL, MIT](http://people.csail.mit.edu/billf/publications/How_To_Do_Research.pdf)

# Cross-Cultural communication

Are you wondering about the German business and working culture? This guide from the *Deutsche Gesellschaft für Internationale Zusammenarbeit \(GIZ\)* provides some insights:

[Cross-Cultural Management: How to Do Business with Germans - A Guide –](https://www.managerprogramm.de/wp-content/uploads/2020/03/Kavalchuk-How_to_do_business_with_Germans-EN.pdf)

# FAQs

**Q:** I have seen that some students do not follow the userguide. For example some do not have an avatar. How should I proceed in that way? Should I follow the userguide or should I do what other students are doing / not doing?

**A:** Please follow the userguide. If you don't understand some contents, ask your supervisor and help to improve the guide.

If other students behave different from the workflow described in the userguide ask them why they do so. If they provide a reasonable explanation, discuss with your supervisor.

Some students do not follow the userguide because they do not know it or they decided to ignore it. Do not worry about it.

In order to become smarter, we do not recommend you to ignore the hints we are providing in the userguide.

The userguide is the only source of truth during the onboarding process.

**Q:** My work follows the *target condition* (TC) method. Since I work very hard, I do not have time to update the target condition. What should I do?

**A:** Updating the target condition is part of your work and the target condition itself. You should take into account the additional time when estimating your due date. The past has shown that successful students need only 5..10 minutes to update their target condition.

**Q:** What should I do when I realize that I will miss the due date of my target condition?

**A:** When you realize that you will miss your due date, please do as follows:

- Describe in the issue why you will miss the due date **before the due date has passed**
    - Why was your estimate wrong, what happened.
        - Pro tip: try to be honest to yourself: if you have bad time management, say it ... and improve it.
    - What will you do to have a better estimate next time.
    - Estimate a new due date and update the TC issue.
    - Inform your supervisor that you will miss the due date and that you have updated the issue.

**Q:** I do not know how to estimate the due date. What should I do?

**A:** Every student in our team should be able to estimate the amount of time he/she needs to reach a target condition (finish a task). If you have problems estimating the time, choose a smaller target condition. A one day duration is a good start.
