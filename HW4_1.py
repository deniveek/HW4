from sys import argv


def unpack(args: list):
    return args[0], args[1:]


def payroll(info: list):
    try:
        wage = int(info[0])
        hours = int(info[1])
        premium = int(info[2]) if len(info) == 3 else 0
    except ValueError:
        return "все параметры должны быть целыми числами"
    except IndexError:
        return "должно быть как минимум два параметра: ставка и часы"
    return wage * hours + premium


print(payroll(unpack(argv)[1]))
