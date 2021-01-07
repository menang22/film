import os, sys

print ("\033[30;1mSilahkan Masukkan Username & Password Scriptnya")

print ("\033[33;1matau silahkan Hubungi Author ")

username = 'hackers70'      

password = 'pinter777'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[32;1mAkhirnya password bener juga tuh", 

			sys.exit()



		else:

			print "\033[31;1mPasswordnya salah woiii... [?]\033[33;1m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[30;1mUsernamenya salah woiii... [?]\033[31;1m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
