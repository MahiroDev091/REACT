import colorama
import time
import os
import sys

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def dev():
	print("[" + Color.LR + "+"+Color.RESET+"] Developer Name: " +Color.LR+"Kitty dev")
	print("[" + Color.LR + "+"+Color.RESET+"] Created: " +Color.LY+"Sep 3, 2022")
	backtomenu()

def terminal_cleaner():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')
        
def troll():
	print(Color.LY +"═══════════════════════════════════════")
	print(Color.LR + """\n\t█▀ █▄▀ █ █▀▄ █▀ █▀▀ █▀▀            
 \t▄█ █░█ █ █▄▀ ▄█ ██▄ █▄▄    """)
	print(Color.RESET + "\t TROLLER STARTING PACK :>")
	print(Color.LR + "skidsec@localhost",":~$ █")
	print(Color.LY  +"═══════════════════════════════════════\n")
	print("[" + Color.LR + "101"+Color.RESET+ "] PH_DDOS " +Color.LY+" ~> Instant File Deleter with DDOS design")
	print("[" + Color.LR + "102"+Color.RESET+ "] ROOTDROID " +Color.LY+" ~> Instant File Deleter with Rooting Design")
	print("[" + Color.LR + "103"+Color.RESET+ "] CURSE IMAGE " +Color.LY+" ~> Disable Accounts using Image link")
	print("[" + Color.LR + "104"+Color.RESET+ "] COVID19 RANSOMWARE" +Color.LY+" ~> ANDROID RANSOMWARE")
	print("[" + Color.LR + "105"+Color.RESET+ "] HOME " +Color.LY+" ~> Back to Home menu\n")
	
	keyboard()
        
def main():
	print(Color.LY +"═══════════════════════════════════════")
	print(Color.LR + """\n\t█▀ █▄▀ █ █▀▄ █▀ █▀▀ █▀▀            
 \t▄█ █░█ █ █▄▀ ▄█ ██▄ █▄▄    """)
	print(Color.RESET + "\tPENETRATION TOOL INSTALLER")
	print(Color.LR + "skidsec@localhost",":~$ █")
	print(Color.LY  +"═══════════════════════════════════════\n")
	time.sleep(0.2)
	print("[" + Color.LR + "1"+Color.RESET+"] Install Nmap " +Color.LY+"[Network Scanner]")
	print("[" + Color.LR + "2"+Color.RESET+"] Install Hydra " +Color.LY+"[Password Cracker]")
	print("[" + Color.LR + "3"+Color.RESET+"] Install SQLMap " +Color.LY+"[Automated SQL Injection Audit]")
	print("[" + Color.LR + "4"+Color.RESET+"] Install Nikto " +Color.LY+"[Web Vulnerablity Scanner]")
	print("[" + Color.LR + "5"+Color.RESET+ "] Install Aircrack-Ng " +Color.LY+"[Wifi Audit]")
	print("[" + Color.LR + "6"+Color.RESET+ "] Install FuzzTester " +Color.LY+"[Fuzzer For Penetration Testing]")
	print("[" + Color.LR + "7"+Color.RESET+ "] Install Karma-DDoS " +Color.LY+"[DDoS Script with Multiple Bypass.]")
	print("[" + Color.LR + "8"+Color.RESET+ "] Install Powerfull F-Tool DDoS " +Color.LR+"[Removed]")
	print("[" + Color.LR + "9"+Color.RESET+ "] Install Admin Finder " +Color.LY+"[Admin panel finder]")
	print("[" + Color.LR + "10"+Color.RESET+ "] Install Metasploit " +Color.LY+"[msfconsole]")
	print("\n[" + Color.LR + "99"+Color.RESET+ "] Exit... \n")
	
	keyboard()
	
def keyboard():
    Prompt = input(Color.LR +"""skidsec@localhost"""+Color.RESET+":~$ ")
    if Prompt == "01" or Prompt == "1":
        nmap()
    elif Prompt == "02" or Prompt == "2":
        hydra()
    elif Prompt == "03" or Prompt == "3":
    	sqlmap()
    elif Prompt == "04" or Prompt == "4":
    	nikto()
    elif Prompt == "05" or Prompt == "5":
    	air()
    elif Prompt == "06" or Prompt == "6":
    	fuzz()
    elif Prompt == "07" or Prompt == "7":
    	karma()
    elif Prompt == "08" or Prompt == "8":
    	print(Color.LR + " 'This tool is removed!'")
    	time.sleep(1.3)
    	os.system("clear")
    	main()
    elif Prompt == "09" or Prompt == "9":
    	finder()
    elif Prompt == "99":
    	os.system("clear")
    	print("\nExiting...")
    	print(Color.LR + "Thanks for using my tool <3"+ Color.RESET)
    	time.sleep(1.9)
    	os.system("clear")
    	sys.exit()
    if Prompt == "REF" or Prompt == "65":
    	os.system("clear")
    	main()
    if Prompt == "EXT" or Prompt == "66":
    	os.system("clear")
    	print("\nExiting...")
    	print(Color.LR + "Thanks for using my tool <3"+ Color.RESET)
    	time.sleep(1.9)
    	os.system("clear")
    	sys.exit()
    if Prompt == "HAX" or Prompt == "68":
    	os.system("clear")
    	troll()
    if Prompt == "HOME" or Prompt == "105":
    	os.system("clear")
    	main()
    	time.sleep(0.6)
    	os.system("?")
    if Prompt == "DEV" or Prompt == "67":
    	dev()
    	keyboard()
    elif Prompt == "10":
    	print("ok")
    elif Prompt == "?":
    	print("\n[" + Color.LR + "65"+Color.RESET+ "] REF " +Color.LY+" ~> Refresh the Menu")
    	print("[" + Color.LR + "66"+Color.RESET+ "] EXT " +Color.LY+" ~> Exit the program")
    	print("[" + Color.LR + "67"+Color.RESET+ "] DEV " +Color.LY+" ~> Developer Information")
    	print("[" + Color.LR + "68"+Color.RESET+ "] HAX " +Color.LY+" ~> Troller Starting Pack\n")
    	keyboard()
    elif Prompt == "65":
    	keyboard()
    elif Prompt == "67":
    	os.system("clear")
    	main()
    else:
        wrong()
        
def wrong():
        print(Color.LR + "Wrong Query! ,Please try again..")
        time.sleep(3)
        terminal_cleaner()
        main()

#DEF INSTALLMENT:
	
def nmap():
	os.system("clear")
	print("\n#### Installing Nmap ####")
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install nmap')
	print("#### Type 'nmap' to start. ####")
	backtomenu()
	sys.exit()

def hydra():
	os.system("clear")
	print('\n#### Installing Hydra ####')
	os.system('apt update -y && apt upgrade -y')
	os.system('git clone https://github.com/vanhauser-thc/thc-hydra')
	os.system('cd thc-hydra')
	backtomenu()
	sys.exit()
	
def sqlmap():
	os.system("clear")
	print('\n#### Installing SQLMAP ####')
	os.system('apt update -y && apt upgrade -y')
	os.system('https://github.com/sqlmapproject/sqlmap')
	os.system('cd sqlmap')
	os.system('chmod +x sqlmap.py')
	os.system('python sqlmap.py')
	backtomenu()
	sys.exit()
	
def nikto():
	os.system("clear")
	print('\n#### Installing Nikto ####')
	os.system('apt-get install perl')
	os.system('git clone https://github.com/sullo/nikto.git')
	os.system('cd nikto')
	os.system('cd program')
	os.system('perl nikto.pl')
	backtomenu()
	sys.exit()
	
def air():
	os.system("clear")
	print("#### Installing AirCrack-Ng ####")
	q = input(Color.LR + "Your phone have root access? (y/n) " + Color.RESET)
	if q == "y" or q == "Y":
		os.system('apt update -y && apt upgrade -y')
		os.system('apt install root-repo aircrack-ng')
		print("### Type 'aircrack-ng' to start ###")
		sys.exit()
	elif q == "n" or q == "N":
		print(Color.LR +"Make sure your phone is rooted to run this tool")
		time.sleep(0.9)
		os.system("clear")
		main()
	else:
		air()
		
def karma():
	os.system("clear")
	print('\n#### Installing Karma DDoS ####')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python3')
	os.system('git clone https://github.com/HyukIsBack/KARMA-DDoS.git')
	os.system('cd KARMA-DDoS')
	os.system('pip install -r requirements.txt')
	os.system('python3 setup.py')
	os.system('python3 main.py')
	backtomenu()
	sys.exit()
	
def finder():
	os.system("clear")
	print('\n#### Installing Admin Finder ####')
	os.system('git clone https://github.com/CyberCommands/Admin-finder.git')
	os.system('cd Admin-finder/')
	os.system('pip install -r requirements.txt')
	print("""python3 finder.py <Target Url> 
For example:
python3 finder.py http://example.com")
	""")
	backtomenu()
	sys.exit()
	
def fuzz():
	os.system('clear')
	print('\n#### Installing FuzzTester ####')
	os.system('git clone https://github.com/fafsnords/FuzzTester')
	os.system('cd FuzzTester')
	os.system('pip install -r requirements.txt')
	os.system('python fuzz.py')
	backtomenu()
	sys.exit()
	
def backtomenu():
  print(Color.LY +"═══════════════════════════════════════")
  print("[" + Color.LR + "105"+Color.RESET+ "] Back to main menu")
  print("[" + Color.LR + "66"+Color.RESET+ "] Exit the Program")
  print(Color.LY +"═══════════════════════════════════════")
  
  key()
  
def key():
  ak = input(Color.LR +"""skidsec@localhost"""+Color.RESET+":~$ ")
  if ak == "105":
    	os.system("clear")
    	main()
  if ak == "66":
    	sys.exit()
  else:
  	print(Color.LR + "Wrong input, try again..")
  	time.sleep(0.9)
  	os.system("clear")
  	backtomenu()

#PASSWORD:
ps= "sc1"		
		
def check():
		print(Color.LY +"═══════════════════════════════════════")
		print(Color.LR + """\n\t█▀ █▄▀ █ █▀▄ █▀ █▀▀ █▀▀            
 \t▄█ █░█ █ █▄▀ ▄█ ██▄ █▄▄    """)
		print(Color.RESET + "\tPENETRATION TOOL INSTALLER")
		print(Color.LR + "skidsec@localhost",":~$ █")
		print(Color.LY  +"═══════════════════════════════════════\n")
		for i in range(3):
		  	pwd = input(Color.LR +"""Password"""+Color.RESET+":~$ ")
		  	j=3
		  	if (pwd==ps):
		  		print(Color.LR + "\t 'Welcome Back, " + Color.RESET + "Kitty " +Color.LR+ "'")
		  		time.sleep(1.8)
		  		os.system("clear")
		  		main()
		  		break
		  	else:
		  		print(Color.LR + "\t[ " + Color.RESET + "Incorrect pass!" + Color.LR + " ]")
		  		time.sleep(0.9)
		  		os.system("clear")
		  		check()
		  		
check()