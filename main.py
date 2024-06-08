import func


def main():
    """Главный код программы"""
    this_load_operations = func.load_operations()
    this_executed = func.last_five_executed(this_load_operations)
    this_last_five_operations = func.last_five_operations(this_executed)
    #print(this_last_five_operations)
    this_new_format_date = func.sorted_date(this_last_five_operations)

    for operation in this_new_format_date:
        # print(operation)
        if operation.get('from') is not None:
            format_from = func.format_info_user(operation["from"])
            format_to = func.format_info_user(operation["to"])
            print(f'{operation["date"]} {operation["description"]}\n'
                  f'{format_from} -> {format_to}\n'
                  f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
    else:
        print(f'{operation["date"]} {operation["description"]}\n'
              f'{format_to}\n'
              f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


if __name__ == "__main__":
    main()
