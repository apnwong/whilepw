password = 'a123456'
x = 3
while True:
	pw = input('Login Password: ')
	if pw == password:
		print('Login Success')
		break
	else:
		x = x - 1
		print('Wrong Password, You have', x , 'chance left')
		if i == 0:
			print('Login Fail')
			break


