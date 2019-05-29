password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pw = input('Login Password: ')
	if pw == password:
		print('Login Success')
		break
	else:
		if x > 0:
			print('Wrong Password. You have', x , 'chance left')
		else:
			print('Login Fail')
	



