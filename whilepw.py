password = 'a123456'
x = 3
while x > 0:
	pw = input('Login Password: ')
	if pw == password:
		print('Login Success')
		break
	else:
		x = x - 1
		print('Wrong Password, You have', x , 'chance left')
	


