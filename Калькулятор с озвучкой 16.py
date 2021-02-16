import os, sys
c = sys.platform
while True:
	d = input('У вас Android? да, нет: ')
	if d == 'да':
		import androidhelper
		while True:
			droid = androidhelper.Android()
			droid.ttsSpeak('Выберите операцию.')
			a=input('Выберите операцию(help справка): ')
			if a =='+':
				droid.ttsSpeak('Выбрано сложение')
				print('Выбрано сложение')
			if a =='*':
				droid.ttsSpeak('Выбрано умножение')
				print('Выбрано умножение')
			if a == '/':
				droid.ttsSpeak('Выбрано деление')
				print('Выбрано деление')
			if a == '**':
				droid.ttsSpeak('Выбрано возведение в степень')
				print('Выбрано возведение в степень')
			while a not in ['+','-','/','*','**','help','cls','clear']:
				print('Выберите другое действие!')
				droid.ttsSpeak('Выберите другое действие.')
				a = input('Выберите операцию(help справка): ')
			while a == 'help':
				droid.ttsSpeak('Выбрана справка.')
				print('+ — сложение, - — вычитание,*  — умножение,** — возведение в степень, / — деление, cls — очистка экрана, clear — очистка экрана')
				a = input('Выберите действие: ')
			while a == 'cls':
				droid.ttsSpeak('Выбрана очистка экрана.')
				os.system('clear')
				a =input('Выберите действие: ')
			while a == 'clear':
				droid.ttsSpeak('Выбрана очистка экрана.')
				os.system('clear')
				a = input('Выберите действие: ')
			try:
				droid.ttsSpeak('Введите число.')
				b=float(input('Введите число: '))
				h=str(b)	
				droid.ttsSpeak('Вы ввели число'+h)
				print('Вы ввели число: '+h)
			except ValueError:
				print('Нельзя проводить операции с буквами.')
				droid.ttsSpeak('Нельзя проводить операции с буквами.')
				droid.ttsSpeak('Введите число.')
				b=float(input('Введите число: '))
				h=str(b)
				droid.ttsSpeak('Вы ввели число'+h)
				print('Вы ввели число: '+h)
			try:
				droid.ttsSpeak('Введите число.')
				c=float(input('Введите число: '))
				i=str(c)
				droid.ttsSpeak('Вы ввели второе число'+i)
				print('Вы ввели второе число: '+i)
			except ValueError:
				print('Нельзя проводить операции с буквами.')
				droid.ttsSpeak('Нельзя проводить операции с буквами.')
				droid.ttsSpeak('Введите число.')
				c=float(input('Введите число: '))
				h=str(c)
				droid.ttsSpeak('Вы ввели второе число'+i)
				print('Вы ввели второе число: '+i)
			if a == '+':
				d=b+c
				e = str(d)
				droid.ttsSpeak('Результат'+e)
				print('Результат = '+e)
			if a == '-':
				d=b-c
				e = str(d)
				droid.ttsSpeak('Результат = '+e)
				print('Результат'+e)
			if a == '*':
				d=b*c
				e = str(d)
				droid.ttsSpeak('Результат'+e)
				print('Результат'+e)
			if a == '**':
				d = b**c
				e = str(d)
				droid.ttsSpeak('Результат'+e)
				print('Результат'+e)
			try:
				if a == '/':
					d=b/c
					e = str(d)
					droid.ttsSpeak('Результат'+e)
					print('Результат'+e)
			except ZeroDivisionError:
				droid.ttsSpeak('Делить на ноль нельзя')
				print ('Делить на ноль нельзя')
	if d == 'нет':
		if c == 'win32':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						a=input('Выберите операцию(help справка): ')
						if a =='+':
							print('Выбрано сложение')
						if a =='-':
							print('Выбрано вычитание')
						if a =='*':
							print('Выбрано умножение')
						if a == '/':
							print('Выбрано деление')
						if a == '**':
							print('Выбрано возведение в степень')
						while a not in ['+','-','/','*','**','help','cls','clear']:
							print('Выберите другое действие!')
							a = input('Выберите операцию(help справка): ')
						while a == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clear — очистка экрана')
							a = input('Выберите действие: ')
						while a == 'cls':
							os.system('clear')
							a =input('Выберите действие: ')
						while a == 'clear':
							os.system('clear')
							a = input('Выберите действие: ')
						try:
							b=float(input('Введите число: '))
							h=str(b)	
							print('Вы ввели число: '+h)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							b=float(input('Введите число: '))
							h=str(b)
							print('Вы ввели число: '+h)
						try:
							c=float(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							c=float(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if a == '+':
							d=b+c
							e = str(d)
							print('Результат = '+e)
						if a == '-':
							d=b-c
							e = str(d)
							print('Результат = '+e)
						if a == '*':
							d=b*c
							e = str(d)
							print('Результат = '+e)
						if a == '**':
							d = b**c
							e = str(d)
							print('Результат = '+e)
						try:
							if a == '/':
								d=b/c
								e = str(d)
								print('Результат = '+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimal import *

					root = Tk()
					root.title('Calculator')

					buttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					activeStr = ''
					stack = []
					def calculate():
						global stack
						global label
						result = 0
						operand2 = Decimal(stack.pop())
						operation = stack.pop()
						operand1 = Decimal(stack.pop())

						if operation == '+':
							result = operand1 + operand2
						if operation == '-':
							result = operand1 - operand2
						if operation == '/':
							try:
								result = operand1 / operand2
							except ZeroDivisionError:
								label.configure(text='Деление на ноль')
						if operation == '*':
							result = operand1 * operand2
						label.configure(text=result)
					def click(text):
						global activeStr
						global stack
						if text == 'CE':
							stack.clear()
							activeStr = ''
							label.configure(text='0')
						elif '0' <= text <= '9':
							activeStr += text
							label.configure(text=activeStr)
						elif text == '.':
							if activeStr.find('.') == -1:
								activeStr += text
								label.configure(text=activeStr)
						else:
							if len(stack) >= 2:
								stack.append(label['text'])
								calculate()
								stack.clear()
								stack.append(label['text'])
								activeStr = ''
								if text != '=':
									stack.append(text)
							else:
								if text != '=':
									stack.append(label['text'])
									stack.append(text)
									activeStr = ''
									label.configure(text='0')
					label = Label(root, text='0', width=35)
					label.grid(row=0, column=0, columnspan=4, sticky="nsew")

					button = Button(root, text='CE', command=lambda text='CE': click(text))
					button.grid(row=1, column=3, sticky="nsew")
					for row in range(4):
						for col in range(4):
							button = Button(root, text=buttons[row][col],
									command=lambda row=row, col=col: click(buttons[row][col]))
							button.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)
		if c == 'linux':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						a=input('Выберите операцию(help справка): ')
						if a =='+':
							print('Выбрано сложение')
						if a =='-':
							print('Выбрано вычитание')
						if a =='*':
							print('Выбрано умножение')
						if a == '/':
							print('Выбрано деление')
						if a == '**':
							print('Выбрано возведение в степень')
						while a not in ['+','-','/','*','**','help','cls','clear']:
							print('Выберите другое действие!')
							a = input('Выберите операцию(help справка): ')
						while a == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clear — очистка экрана')
							a = input('Выберите действие: ')
						while a == 'cls':
							os.system('clear')
							a =input('Выберите действие: ')
						while a == 'clear':
							os.system('clear')
							a = input('Выберите действие: ')
						try:
							b=float(input('Введите число: '))
							h=str(b)	
							droid.ttsSpeak('Вы ввели число'+h)
							print('Вы ввели число: '+h)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							b=float(input('Введите число: '))
							h=str(b)
							print('Вы ввели число: '+h)
						try:
							c=float(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							c=float(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if a == '+':
							d=b+c
							e = str(d)
							print('Результат = '+e)
						if a == '-':
							d=b-c
							e = str(d)
							print('Результат = '+e)
						if a == '*':
							d=b*c
							e = str(d)
							print('Результат = '+e)
						if a == '**':
							d = b**c
							e = str(d)
							print('Результат = '+e)
						try:
							if a == '/':
								d=b/c
								e = str(d)
								print('Результат = '+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimal import *

					root = Tk()
					root.title('Calculator')

					buttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					activeStr = ''
					stack = []
					def calculate():
						global stack
						global label
						result = 0
						operand2 = Decimal(stack.pop())
						operation = stack.pop()
						operand1 = Decimal(stack.pop())

						if operation == '+':
							result = operand1 + operand2
						if operation == '-':
							result = operand1 - operand2
						if operation == '/':
							try:
								result = operand1 / operand2
							except ZeroDivisionError:
								label.configure(text='Деление на ноль')
						if operation == '*':
							result = operand1 * operand2
						label.configure(text=result)
					def click(text):
						global activeStr
						global stack
						if text == 'CE':
							stack.clear()
							activeStr = ''
							label.configure(text='0')
						elif '0' <= text <= '9':
							activeStr += text
							label.configure(text=activeStr)
						elif text == '.':
							if activeStr.find('.') == -1:
								activeStr += text
								label.configure(text=activeStr)
						else:
							if len(stack) >= 2:
								stack.append(label['text'])
								calculate()
								stack.clear()
								stack.append(label['text'])
								activeStr = ''
								if text != '=':
									stack.append(text)
							else:
								if text != '=':
									stack.append(label['text'])
									stack.append(text)
									activeStr = ''
									label.configure(text='0')
					label = Label(root, text='0', width=35)
					label.grid(row=0, column=0, columnspan=4, sticky="nsew")

					button = Button(root, text='CE', command=lambda text='CE': click(text))
					button.grid(row=1, column=3, sticky="nsew")
					for row in range(4):
						for col in range(4):
							button = Button(root, text=buttons[row][col],
									command=lambda row=row, col=col: click(buttons[row][col]))
							button.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)
		if c == 'darwin':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						a=input('Выберите операцию(help справка): ')
						if a =='+':
							print('Выбрано сложение')
						if a =='-':
							print('Выбрано вычитание')
						if a =='*':
							print('Выбрано умножение')
						if a == '/':
							print('Выбрано деление')
						if a == '**':
							print('Выбрано возведение в степень')
						while a not in ['+','-','/','*','**','help','cls','clear']:
							print('Выберите другое действие!')
							a = input('Выберите операцию(help справка): ')
						while a == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clear — очистка экрана')
							a = input('Выберите действие: ')
						while a == 'cls':
							os.system('clear')
							a =input('Выберите действие: ')
						while a == 'clear':
							os.system('clear')
							a = input('Выберите действие: ')
						try:
							b=float(input('Введите число: '))
							h=str(b)	
							droid.ttsSpeak('Вы ввели число'+h)
							print('Вы ввели число: '+h)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							b=float(input('Введите число: '))
							h=str(b)
							print('Вы ввели число: '+h)
						try:
							c=float(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except ValueError:
							print('Нельзя проводить операции с буквами.')
							c=float(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if a == '+':
							d=b+c
							e = str(d)
							print('Результат = '+e)
						if a == '-':
							d=b-c
							e = str(d)
							print('Результат = '+e)
						if a == '*':
							d=b*c
							e = str(d)
							print('Результат = '+e)
						if a == '**':
							d = b**c
							e = str(d)
							print('Результат = '+e)
						try:
							if a == '/':
								d=b/c
								e = str(d)
								print('Результат = '+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimal import *

					root = Tk()
					root.title('Calculator')

					buttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					activeStr = ''
					stack = []
					def calculate():
						global stack
						global label
						result = 0
						operand2 = Decimal(stack.pop())
						operation = stack.pop()
						operand1 = Decimal(stack.pop())

						if operation == '+':
							result = operand1 + operand2
						if operation == '-':
							result = operand1 - operand2
						if operation == '/':
							try:
								result = operand1 / operand2
							except ZeroDivisionError:
								label.configure(text='Деление на ноль')
						if operation == '*':
							result = operand1 * operand2
						label.configure(text=result)
					def click(text):
						global activeStr
						global stack
						if text == 'CE':
							stack.clear()
							activeStr = ''
							label.configure(text='0')
						elif '0' <= text <= '9':
							activeStr += text
							label.configure(text=activeStr)
						elif text == '.':
							if activeStr.find('.') == -1:
								activeStr += text
								label.configure(text=activeStr)
						else:
							if len(stack) >= 2:
								stack.append(label['text'])
								calculate()
								stack.clear()
								stack.append(label['text'])
								activeStr = ''
								if text != '=':
									stack.append(text)
							else:
								if text != '=':
									stack.append(label['text'])
									stack.append(text)
									activeStr = ''
									label.configure(text='0')
					label = Label(root, text='0', width=35)
					label.grid(row=0, column=0, columnspan=4, sticky="nsew")

					button = Button(root, text='CE', command=lambda text='CE': click(text))
					button.grid(row=1, column=3, sticky="nsew")
					for row in range(4):
						for col in range(4):
							button = Button(root, text=buttons[row][col],
									command=lambda row=row, col=col: click(buttons[row][col]))
							button.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)

					root.mainloop()