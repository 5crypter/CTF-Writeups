Zip Tunnel
======
**Category: Forensics**
**Points: 300**

The zip file given was encrypted using a passphrase. I tried running fcrackzip on the zip file with all the dictionaries given [here] (https://github.com/danielmiessler/SecLists/tree/master/Passwords). But none of them found a valid password. 

On reading the hint, **wamerican** seemed a little suspicious. I mean, Subway doesn't have that in their menu!

A quick google search tells me that wamerican is a dictionary! I downloaded that and extracted the first file. Luckily, the name wasn't as random as the first one. 

I wrote a small script to extract each zip with a cracked password. 

```
import os

for i in range(419,0,-1):
	command1 = 'fcrackzip -u -D -p "american-english-insane" level'+str(i)+'.zip'
	data = os.popen(command1).readlines()
	s = ""
	for j in data:
		s+=j
	start = s.find('pw == ')+6
	end = s.find('\n',start)	
	password = s[start:end]
	command2 = 'unzip -P '+ password + ' level'+str(i)+'.zip'
	os.system(command2)
```

After about 20 minutes, the script crashed. And I was left with **level0.zip** whose password wasn't there in the dictionary. I again tried cracking the password with all the password files I had. Password was still not found. I then randomly tried **easyctf** as the password. Voila! I had the flag. 


```
Congratulations, you've made it to the bottom of the zip tunnel! I've got a flag for you: easyctf{x4m1n3_uR_z1pp34_PDq_17c4ee3}
```

