drive = input('你是否有開過車?')
if drive != '有' and drive != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = int(input('你的年齡'))
if drive == '有':
	if age >= 18:
		print('你通過測試了')
	else:
		print('你年齡不符怎可以開車')
else:
	if age >= 18:
		print('你可以去考駕照')
	else:
		print('再過幾年就可以開車囉')

