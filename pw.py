import os, sys

print ("\033[30;1mSilahkan Masukkan Username & Password Anda")

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

			print "\033[31;1mMaaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
