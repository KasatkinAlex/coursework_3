import json
from datetime import datetime

def reading_json(json_file):
    """
    Считывает файл json
    :param json_file: файл.json
    :return: список словарей
    """
    with open(json_file, "rt", encoding="utf-8") as fail:
        return json.load(fail)


def sorted_executed(operation: list):
    """
    Вытаскивает и сортирует нужные нам данные из список словарей
    :param operation: список словарей от файла json
    :return: отсортированный список словарей по дате
    """
    dict_executed = []
    for i in operation:
        if i.get("state") == "EXECUTED" and i.get("from"):
            dict_executed.append(i)
    return sorted(dict_executed, key=lambda x: x['date'])


def data_from_list(date_list):
    """
    Переводит из строки в дату
    :param date_list: строка с датой
    :return: число, месяц, год
    """
    date = datetime.fromisoformat(date_list)
    return f"{date.day}. {date.month}. {date.year}"


def number_encoding(account:str):
    """
    Кодирует счет или номер карты
    :param account: строка с счетом или название платежной системы
    :return: закодированные цифры
    """
    account_list = account.split()
    str_account_code = ""
    if "счет" in account.lower():
        for i in account_list:
            if not i.isdigit():
                str_account_code += i
            else:
                str_account_code += f" **{i[:4]}"
    else:
        for i in account_list:
            if not i.isdigit():
                str_account_code += i + " "
            else:
                str_account_code += f"{i[:4]} {i[4:6]}** **** {i[-4:]}"
    return str_account_code


list_operation = reading_json("operations.json")
sorted_list_operation = sorted_executed(list_operation)
final_list = []
final_dict = {}
for i in sorted_list_operation[-5:]:
    print(f"{data_from_list(i["date"])} | {i['description']} | "
          f"{number_encoding(i["from"])} -> {number_encoding(i["to"])} | "
          f"{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n")

