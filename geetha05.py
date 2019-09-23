







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

'''n=5
for j in range(1,n+1):
	for i in range(ord("a"),ord("a")+j):
		print(chr(i),end="")
		print()'''

'''ass'''

'''n=5
for i in range(1,n+1):
	print("*" *i)'''

'''stmt="python is an easy programmimng language"
vowels="aeiou"
for i in vowels:
	   print(i+str(stmt.count((i))))'''

'''stmt="python is esay "
char=" "
ind=-1
d=0
for i in range(stmt.count(char)):
	ind=stmt.index(char,ind+1)
	s=stmt[d:ind+1]
	d=ind
	print(s[::-1],end=" ")'''





# '''p=input("Geetha@01")
# x=true
# while x:
# 	if(len(p)<6 or len(p)>12):
# 		break
# 	elif not re.search("[a-z]",p):
# 		break
# 	elif not re.search("[0-9]",p):
# 		break
# 	elif not re.search("[A-Z]",p):
# 		break
# 	elif not re.search("[$#@]",p):
# 		break
# 	elif re.search("/s",p):
# 		break
# 	else:
# 		print("valid password")
# 		x=false
# 		break
# if x:
# 	print("not a valid password")'''


# '''1 Ram Input AND Input --> Raw input is used in python2 version it does nt exit in py3 and Input is used in python3 version
# 2 Rules for Delaring a Variable --> Must begin with a letter or underscore other character can be letters,numbers or
#                  case senstive.can be any lenght there are some reseved words which you cannot use as a  Variable
#                   name because python uses them other things.
# 3 Difference Detween String --> single quotes ('') are used in strings in python will nt apply to the condition
#                                 Doudle quotes ("") are used to pased for variables to replace whereas a strings
#                                 are used for comment the statement in python '''

'''stmt="python is esay "
char=" "
ind=-1
d=0
for i in range(stmt.count(char)):
	ind=stmt.index(char,ind+1)
	s=stmt[d:ind+1]
	d=ind
	print(s[::-1],end=" ")'''
'''a="\n\thyderbad\t\n"
print(a.strip())'''
'''n=10
l=[]
for i in range(n+1):
	l.append(i)
print(l)'''

'''n=10
l=[]
for i in range(n+1):
	l.append(i**2)
print(l)'''

'''n=10
l=[]
for i in range(n+1):
	if i%2==0:
		l.append(i)
print(l)'''

'''n=10
l=[]
for i in range(n+1):
	if i%2==0:
		l.append(i**2)
print(l)'''

'''num=4
l=[]
for i in range(num):
	l.append(chr(97+i))
print(l)'''
num=4
l=[]
for i in range(ord("a"),ord("a")+)e:
		l.append(i)
print(l)