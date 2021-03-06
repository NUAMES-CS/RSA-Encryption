#import dependencies
import os, sys
try:
	import rsa
except:
	print("RSA module needed -- installing")
	os.system("pip3 install rsa")
	import rsa
	print("complete")

#load public key
if os.path.exists("public.pen"):
	with open("public.pen", 'rb') as f:
		public = rsa.PublicKey.load_pkcs1(f.read())
else:
	sys.exit('Inform Mr. Simonsen that the program could\'t find "public.pen"')

#prompt for relevant information
last = input("What is your last name?\n").title()
first = input("What is your legal first name?\n").title()
if input("Do you have a name that you prefer to go by?(Y/n)\n").lower() in("yes","y"):
	pref = input("What is your preferred name?\n").title()
else:
	pref = ''
valid = False
while not valid:
	try:
		period = int(input("What class period are you in?\n"))
	except ValueError:
		print("That wasn't a number.")
	if period not in range(1,9):
		print(f"{period} is not a valid class period.")
	else:
		valid = True
confirm = False
while not confirm:
	github = input("What's your GitHub username?\n")
	print("Double check that your username has been entered correctly.")
	print(github)
	if input("Is you username entered correctly?(Y/n)\n").lower() in ('y','yes'):
		confirm = True

#format text
data = f"{last},{first},{pref},{period}"
#encrypt text
code = rsa.encrypt(data.encode('ascii'), public)
#save encryption to file
with open(f"students/{github}.dat",'wb') as f:
	f.write(code)

print("encrypted file created")
