from func import reading_json, sorted_executed, data_from_list, number_encoding

list_operation = sorted_executed(reading_json("operations.json"))
sorted_list_operation = sorted(list_operation, key=lambda x: x['date'])
final_list = []
final_dict = {}
for i in sorted_list_operation[-5:]:
    print(f"{data_from_list(i["date"])} | {i['description']} | "
          f"{number_encoding(i["from"])} -> {number_encoding(i["to"])} | "
          f"{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n")
