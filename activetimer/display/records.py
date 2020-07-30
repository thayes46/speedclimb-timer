import gspread


def get_records():
    gc = gspread.service_account(filename='service_account.json')
    sh = gc.open("Record times")
    sorted_sheet = sh.get_worksheet(1)
    # Sorted entries are stored on Sheet2 in the g sheet
    # print statement for example/test
    top_times = (sorted_sheet.get('A1:C10'))
    return top_times
