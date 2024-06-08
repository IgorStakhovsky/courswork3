from work_code import func

def test_sorted_date():
    """ Проверка функции перевода времени """
    date = [{"date": "2018-01-21T01:10:28.317704"}]
    assert func.sorted_date(date) == [{'date': '21.01.2018'}]

def test_last_five_operations():
    """ Проверка на сортировку 5 последних выполненных операций """

    assert func.last_five_operations([{
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
  }]) == [{
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

def test_last_five_executed():
    assert func.last_five_executed([{"state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"}]) == [{"state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"}]

def test_format_info_user():
    assert func.format_info_user('Счет 48894435694657014368') == 'Счет **4368'
    assert func.format_info_user('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'