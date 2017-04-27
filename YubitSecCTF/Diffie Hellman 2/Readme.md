Diffie-Hellman II
======
**Category: Steganography**
**Points: 275**

`II. part is STEGO.`
`If you already solved the I. part.`
`Everything is clear.`
`Just analyze the file.`

This part is a continuation of Diffie Hellman I. The first part was basic bruteforce.

Here's the script for that:

```python
g = 10
q = 1357
for i in range(1000):
	for j in range(1000):
		if pow(g,i,q)==419 and pow(g,j,q)==34 and pow(g,i*j,q)==33:
			print "a:"+str(i)+" b:"+str(j)
```

`a:521 b:619`

As the second part was stego, I decided to run `strings` on the image file. 

At the bottom, there was a clue: 
`Hmm.. maybe the other part is stego`
`Key: abababababab`

Since they gave a key, I was pretty sure that I had to use steghide with the given key. 

So I replaced the **a**s with 521 and **b**s with 619 in the key and tried it as the password. And it worked!

I got a text file with a tumblr link: `http://ababababababqbababababababab.tumblr.com/`

On opening that link, we were asked for a password. On looking at the url, we saw that it was a different sequence of **a**,**b** and **q**. So I substituted the corresponding values in the url, and used it as a password. That was it, I was given the flag!

```
Congratulations!

Here is the flag: YUBITSEC{Y0U_MUST_B3_1ZZ3TT1N}
```




	

