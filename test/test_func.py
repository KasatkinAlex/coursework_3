from func import data_from_list, reading_json, sorted_executed, number_encoding
import json

a = [ {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]
b = [{
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }]
# def test_reading_json():
#     assert reading_json("operations.json") == list


def test_sorted_executed():
    assert sorted_executed(a) == a
    assert sorted_executed(b) == []
    assert sorted_executed([{"state": "1234", "from": "1234"}]) == []


def test_data_from_list():
    assert data_from_list("2019-08-26T10:50:58.294041") == "26. 8. 2019"


def test_number_encoding():
    assert number_encoding("Счет 41421565395219882431") == "Счет **2431"
    assert number_encoding("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"