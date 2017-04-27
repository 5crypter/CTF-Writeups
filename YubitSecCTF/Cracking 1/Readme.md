Cracking
======
**Category: Forensics
**Points: 150**

`Can you break it ?`

We are given a password protected Zip file. All we have to do is bruteforce to get the key!

On running the command: `fcrackzip -u -D -p passwords.txt Flag.zip`, **passwords.txt** being the dictionary you want to bruteforce with. After about 5-6 seconds, the command stopped giving the password `h0lyshit`.

On extracting the zip file with the password, we got the flag!

`YUBITSEC{3ASY_CR4CK_BR0_W3LL_D0N3}`
	

