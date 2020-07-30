import gspread

gc = gspread.service_account(filename='service_account.json')
sh = gc.open("Record times")
