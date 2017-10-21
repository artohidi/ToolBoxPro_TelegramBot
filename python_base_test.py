list_set = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
parameters = ["+/-", "%", "÷", "✕", "-", "+", "=", "."]
active_parameters = ["+/-", "✕", "+", "-", "÷", "."]
deactivate_parameters = ["%", "="]
output = '0'
output_plus = ''
output_minus = ''
param = ''
show_list = ''
calculator_keyboard = "AC\t+/-\t%\t÷\n1\t2\t3\t✕\n4\t5\t6\t-\n7\t8\t9\t+\n0\t\t.\t=\n=>"


def show_list_set():
    global list_set, show_list
    show_list = ''
    for i in range(0, len(list_set)):
        show_list = show_list + str(list_set[i])
    return show_list


def plus_function():
    return 1


while True:
    if len(list_set) < 2:
        print(output)
        print(calculator_keyboard)
        data = input()
        if data in active_parameters:
            if data == '+/-':
                output = "-" + output
            elif data == '✕':
                pass
            elif data == '+':
                pass
            elif data == '-':
                pass
            elif data == '÷':
                pass
            elif data == '.':
                pass
        elif data == 'AC':
            output = '0'
            list_set = []
        elif int(data) in numbers and data != '0':
            output = data
            list_set.append(data)
    elif len(list_set) < 9:
        print(show_list())
        print(calculator_keyboard)
        data = input()
        if data == 'AC':
            output = '0'
            list_set = []
        elif data in active_parameters:
            if data == '+/-':
                output = "-" + output
            elif data == '✕':
                pass
            elif data == '+':
                output_plus = show_list_set()
                show_list = '0'
                param = '+'
            elif data == '-':
                output_minus = show_list_set()
                show_list = '0'
                param = '-'
            elif data == '÷':
                pass
            elif data == '.':
                pass
        elif data in deactivate_parameters:
            if data == '=':
                if param == '+':
                    show_list = str(int(output_plus) + int(show_list))
                elif param == '-':
                    output = str(int(output_minus) - int(show_list))
                else:
                    pass
        elif int(data) in numbers and data != '0':
            output = data
            list_set.append(data)

    else:
        print(show_list_set())
        print(calculator_keyboard)
        data = input()
