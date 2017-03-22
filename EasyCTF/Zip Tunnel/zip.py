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
