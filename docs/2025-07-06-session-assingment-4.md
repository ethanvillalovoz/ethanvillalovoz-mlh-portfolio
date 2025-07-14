One catch from setting creating a service part 1 is that selinux was preventing the flask service from starting in roots home directory. 

You have two options:

1. Disable selinux to allow the flask service to start
2. Install flask in a directory other than roots home directory such as '/opt'

The instructions in the modules show that this should be running in the root directory, so these leads me to beleive that this was either selinux was not installed in the instructors vm or it was running in permissive mode. THis was not clarified in the instructions of the modules.