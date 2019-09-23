







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

# #1st program

'''n=5
for i in range(1,n+1):
	print("*" *i)'''

# # 2nd program

'''password=input("ENTER A PASSWAORD:")
l=len(password)
a=b=c=d=0
s=["@","&","$"]
if l>6 and l<12:
	if password.isdigit():
		print("character is missing")
	else:
		for l in password:
			if ord(l)>96 and ord(l)<123:
				a=a+1
			elif ord(l)>64 and ord(l)<91:
				b=b+1
			elif ord(l)>47 and ord(l)<58:
				c=c+1
			elif l in s:
				d=d+1
	if a==0:
		print("small character is missing")
	if b==0:
		print("capital character is missing")
	if c==0:
		print("number character is missing")
	if d==0:
		print("special character is missing")
else:
	print("length is in between 6 & 12")'''			

## 4th program

'''stmt="python is an easy programmimng language"
vowels="aeiou"
for i in vowels:
	   print(i+str(stmt.count((i))))'''

## 5th program

'''n1=int(input("enter 1st number :"))
n2=int(input("enter 2nd number :"))
n3=int(input("enter 3rd number :"))
mean=(n1+n2+n3)/3
print(mean)
median=n2
print("median="+str(n2))
if n1==n2:
	if n1==n3:
		print("mode=" + str(n1))
	else:
		print("mode=" + str(n2))
elif n1==n3:
	print("mode=" + str(n2))
elif n2==n3:
	print("mode=" + str(n2))
else:
	print("no mode")'''					

## 6th program

'''stmt="python is esay "
char=" "
ind=-1
d=0
for i in range(stmt.count(char)):
	ind=stmt.index(char,ind+1)
	s=stmt[d:ind+1]
	d=ind
	print(s[::-1],end=" ")'''








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
'''num=4
l=[]
for i in range(
		l.append(i)
print(l)'''
           # 08/07/19    
'''l1=[20,4,3,50] 
l2=[5,5,8,54]
op=[]
if len(l1)==len(l2):
 	for i in range(len(l1)):
 		op.append(l1[i]+l2[i])	
print(op)'''
'''stmt="python is an esay programming language"
char="m"
char=[ i for i in stmt if ord(i) > ord(char)]
char.sort()
print(char)'''
'''stmt="python is an easy programmimg language"
words=[i for i in stmt.split() if len(i)>5]
print(words)'''
# task on sort(the output will in ass order)
'''nums=[34,2,58,7,5,87,74,24,52]
nums.sort()
print(nums)'''
# by reverse() (the otp will be des order) 
'''nums=[25,54,75,87,69,78,89]
nums.sort()
nums.reverse()
print(nums)'''

'''nums=[58,45,65,95,2,41,14]
nums.sort
print(nums)'''
# task on, tuples
'''nums=(1,2,3,4,5,6,7,8)
print(type(nums))'''
'''nums=1,2,5,7,9,7,9
print(nums[2:7:2])'''
'''nums=(1,2,3,4,5,6)
print(nums[0:3])
print(nums[0:4])'''
'''nums=(1,45,25,36,75,95,12)
tech=("php","java","mysql","php")
for i in nums+tech:
	print(i)'''
'''a=20,30,40
print(a)
print(type(a))'''
'''fees=(10,20,30,40,50,60)
print(fees)
print(type(fees))'''
'''fees=(10,20,30,40,50,60)
fees=list(fees)
print(type(fees))
fees[3]=55
print(fees)
print(type(fees))
fees=tuple(fees)
print(fees)
print(type(fees))'''
'''nums=(20,52,(65,54,"php"),56,8,9,[88,78,65,"java"],8)
op=[]
for i in nums: 
	if type(i) is list or type(i) is tuple:
		for j in i:
			op.append(j)
	else:
		op.append(i)
print(tuple(op))'''		
'''l1=[20,12,0,42,52,45,52]
l2=[12,52,3,25,45,41]
nl=l1+l2
#l1.extend(l2)
print(l1)
print(l2)
print(nl)'''
#for i in l1:
#	l1.extend

               # 11/07/19
 # delecting the element              
'''tech={"python":3.7,"mysql":8,"java":5,"php":8,"pip":5}
del(tech["java"])
print(tech)'''
# modify the keys into new variables
'''tech={"python":3.7,"mysql":8,"java":5,"php":8,"pip":5}
tech["mysql"]=5
print(tech)'''
# adding the element to the object
'''tech={"python":3.7,"mysql":8,"java":5,"php":8,"pip":5}
tech["orcale"]=8
print(tech)'''
# task on multiplies usind dictorinces
'''n=10
d={}
for i in range(n+1):
	d[i]=i**2
print(d)'''	
# task
'''l1=[10,20,30,40,50,60]
l2=[2,3,4,5,6,7]
d={}
if len(l1)==len(l2):
	for i in range(len(l1)):
		d[l1[i]]=l2[i]
print(d)'''	
# task
'''stmt="python is easy language"
d={}
for i in stmt.split():
	d[i]=len(i)
print(d)'''
# ZIP Functions
'''l1=[10,20,30,40,50]	
l2=[2,3,4,5,6]
zo=zip(l1,l2)
print(zo)
zl=list(zo)
print(zl)
zt=tuple(zo)
print(zt)
zd=dic(zo)
print(zd)'''

# it is removing the last element 
# tech={"python":3.7,"mysql":8,"java":5,"php":8,"pip":5}
# print(tech)
# tech.popitem()
# print(tech)

'''tech={"python":3.7,"mysql":8,"java":5,"php":8,"pip":5}
num={1:"one",2:"two",3:"three","four":4}
tech.update(num)
print(tech)
print(num)'''

stmt="python is an esay language"
char="m"
d={}
for i in stmt:
	if ord(i) > ord(char):
		d[i]=chr(ord(i)+1)
print(d)		









