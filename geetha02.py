







'''stmt=input("enter a statement")
word=input("enter a word")
if word in stmt:
	n=input("choose option:")
	n=int(n)
	if n==1:
 		new= input("enter a new word:")
 		print(stmt.replace(word, new))
	elif n==2:
 		print(stmt.index(word))
	else:
 		print("not choosen correct value")
else:
 	print("%s is not is statment"%(word))
'''

'''a=input("enter a character")
b= input("enter another character")
c= ord(a)
d=ord(b)
if c<d:
	print("%s appears before %s"%(a,b))
else:
	print("%s appears after %s"%(a,b))'''

# ip=input("enter time in hh:mm:ssfff")
# if len(time)==10:
# 	print("hours %s" %(time[0:3]))
# 	h=time[:2]
# 	m=time[3:5]
# 	s=time[6:8]
# 	f=time[9:]
# 		if f=="pm"
# 	print("%d:%s:%s" %(int(h)+12,m,s))
# else:
# 	print("%s:%s:%s:" %(h.m,s))
# else:
# print("not a format specified")


'''n=13
c=0
for i in range(1,n+1):
	if n%i == 0:
		c=c+1
	if c>2: 
		print("no of factors" + str(c))
		print(str(n)+ "is composite")
	else:
		print(str(n)+ "is prime")'''

'''n=8
for j in range(1,n+1):
	for i in range(1,j+1):
		print(i,end="")
		print()'''
'''n=5
for i in range(1,n+1):
	print(n,'x',i,'=',n*i)'''

'''stmt ="python is an easy programming language"
char="n"
for i in range(len(stmt)):
	if stmt[i] == char:
		print(i)'''

'''stmt="python is an esay programming language"
vowels="aeiou"
for i in stmt:
	if i in vowels:
		print(i)'''

n=5
for j in range(1,n+1):
	for i in range(ord("a"),ord("a")+j):
		print(chr(i),end="")
		print()












