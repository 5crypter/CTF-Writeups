Cracking II
======
**Category: Forensics**
**Points: 250**

`Its short tunnel. Every gates help you, just be careful!`

We again have a password protected zip file! But this time, there are multiple Password protected Zip files within the first one! Again, all we have to do is bruteforce the key for each Zip file!

On running the command: `fcrackzip -u -D -p passwords.txt <filename>` for each file, we extract the zip files using the bruteforced password (for the 6th zip, there was no password!), and we are given with 10 images with numbers in Roman Numeral Form.

On simply running `strings` on each of the images, we found out that there was some base64 encoded text at the end.

On decoding (using `strings <filename> | tail -1 | base64 --decode`) and combining each of the base64 encoded strings, we get the flag!


`YUBITSEC{EVIL_CORP_WANTS_YOU}`

	

