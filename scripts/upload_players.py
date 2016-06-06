# scripts/upload_players.py

from hello.models import Pitcher
import xlrd

def run():
    # Clear old pitchers
    Pitcher.objects.all().delete()

    # Upload new pitchers
    xl_workbook = xlrd.open_workbook('pitchers.xlsx')
    xl_sheet = xl_workbook.sheet_by_index(0)

    nrows = xl_sheet.nrows
    ncols = xl_sheet.ncols

    for rnum in range(nrows):
        if rnum == 0:
            continue

        row = xl_sheet.row(rnum)

        # For debug
     #   for cnum in range(ncols):
     #       cell_obj = xl_sheet.cell(rnum, cnum)
     #       print ('Column: [%s] cell_obj: [%s]' % (cnum, cell_obj.value))

        data = {}
        data['first_name'] = xl_sheet.cell(rnum, 0).value
        data['last_name'] = xl_sheet.cell(rnum, 1).value
        data['position'] = xl_sheet.cell(rnum, 2).value
        data['age'] = xl_sheet.cell(rnum, 3).value
        data['team'] = xl_sheet.cell(rnum, 4).value
        data['contract_date'] = xl_sheet.cell(rnum, 5).value
        data['pit_hand'] = xl_sheet.cell(rnum, 6).value
        data['kinds'] = xl_sheet.cell(rnum, 7).value
        data['era'] = xl_sheet.cell(rnum, 8).value
        data['w'] = xl_sheet.cell(rnum, 9).value
        data['l'] = xl_sheet.cell(rnum, 10).value
        data['sv'] = xl_sheet.cell(rnum, 11).value
        data['k9'] = xl_sheet.cell(rnum, 12).value

        p = Pitcher(**data)
        p.save()