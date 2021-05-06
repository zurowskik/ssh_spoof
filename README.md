# ssh_spoof

This program spoofs an ssh connection in order to waste an attacker's time once they have a foothold in the system on a single machine.

How this program works:

## Architecture Diagram

![name-of-you-image](https://github.com/zurowskik/Images_for_README/blob/main/ssh_spoof.png)

-In this system, the system owner replaces the default ssh executable with the spoofed version.

-The Spoof version simply loops back to the current machine and logs all information into a loggin file in order to waste an attacker's time in the system

-Meanwhile, the actual ssh executable is moved to a different directory where it can be properly executed by a user who knows that the system is in place (i.e., an legitimate user)


## Installation

1. First move the legitimate copy of ssh out of /usr/bin (if on a Linux/MacOS machine) into a different directory of your choice
2. Move the ssh executable in this repository into /usr/bin
3. Move the accompanying Python script into any folder and change the path in the ssh script to the correct location
4. If desired, change the path of the Logging folder


## Usage

The system runs in place of a legitimate copy of ssh. Once the installation steps above are complete, it will execute with the simple ssh command (either with no path specified or the /usr/bin path specified)

In order to actually execute the legitimate ssh executable, simply execute ssh with the full path included in the command (e.g. ./real/ssh)
