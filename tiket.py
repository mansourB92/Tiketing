import os
MCode = 101
remeber = 0
Dmember = {}
Dadmnin = {"password": "abcd"}
def admin():
	exx = 0
	while True:
		if exx == 1:
			break
		global remeber
		global Dmember
		if remeber == 4:
			print("!!! Your account has been blocked !!!")
			break
		pw = input("insert your password: ")
		if pw == Dadmnin["password"]:
			while True:
				if Dmember == {}:
					print("\nMember list is empty\n")
					exx = 1
					break
				else:
					print("\n\tMember list:\n")
					for x, y in Dmember.items():
						print("Member ID",x,"\b: name:",y["name"],": Number:",y["number"],"\n",y["name"],"\b\'s requset:",y["req"],"\n")
					Ncheck = input("\nPlease, insert member ID or number for your response OR \n insert 0 for Exit:")
					if Ncheck == "0":
						exx = 1
						break
					Mcheck = 0
					if Ncheck in Dmember:
						print("\n\tresponse for member ID",Ncheck,"\b:")
						req = input("insert your response: ")
						Dmember[Ncheck]["Ares"] = req
						print("\nYour response for member ID",Ncheck,"has been registered \n")
						Mcheck = 1
					else:
						for x,y in Dmember.items():
							if y["number"] == Ncheck:
								print("\n\tresponse for member ID",x ,"\b:")
								req = input("insert your response: ")
								Dmember[x]["Ares"] = req
								print("\nYour response for member ID",x ,"has been registered \n")
								Mcheck = 1
								break
					if Mcheck == 0:
						print("!!! Your enter member not found !!!")

		else:
			print("!!! The password you entered is incorrect !!!\n\tYou can try",3 - remeber ," more times")
			remeber +=1

def member():
	global MCode
	global Dmember
	print(f"your ID is: {MCode}")
	Dmember[str(MCode)] = {
		"name": input("insert your name: "),
		"number": input("insert your namber: "),
		"req": input("insert your reqest: "),
		"Ares": "Empty"
	}
	print("\nMr", Dmember[str(MCode)]["name"], "\b, Your request has been registered \n")
	MCode += 1
def request():
	if Dmember == {}:
		print("\nMember list is empty\n")
	else:
		print("\n\tMember list:\n")
		for x, y in Dmember.items():
			print("Member Code",x,"\b: name:",y["name"],": Number:",y["number"],"\n",y["name"],"\b\'s requset:",y["req"])
			print("Admin response:",y["Ares"],"\n")
while True:
#	os.system("CLS")
	menu = input('''
 ________________________
|\t\t\t |
|\t1. Admin\t |
|\t2. Members\t |
|\t3. Reqests\t |
|\t0. Exit\t\t |
|________________________|

Please, insert yours option: ''')

	if menu == "1":
		print("\n 1. Amin:\n")
		admin()
	elif menu == "2":
		print("\n 2. Members:\n")
		member()
	elif menu == "3":
		print("\n 3. requests:\n")
		request()
	elif menu == "0":
		break
	else:
		continue
	

