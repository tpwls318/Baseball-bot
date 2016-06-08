# scripts/upload_players.py

from hello.models import Pitcher ,Hitter
import xlrd

def run():
    # Clear old pitchers
    Pitcher.objects.all().delete()
    Hitter.objects.all().delete()

    # Upload new pitchers
   # xl_workbook = xlrd.open_workbook('pitchers.xlsx')
    xl_workbook = xlrd.open_workbook('players.xlsx')
    xl_sheet_pitcher = xl_workbook.sheet_by_index(0)
    xl_sheet_hitter = xl_workbook.sheet_by_index(1)

    nrows_p = xl_sheet_pitcher.nrows
    ncols_p = xl_sheet_pitcher.ncols

    nrows_h = xl_sheet_hitter.nrows
    ncols_h = xl_sheet_hitter.ncols


    for rnum in range(nrows_p):
        if rnum == 0:
            continue

        row = xl_sheet_pitcher.row(rnum)

        # For debug
     #   for cnum in range(ncols):
     #       cell_obj = xl_sheet.cell(rnum, cnum)
     #       print ('Column: [%s] cell_obj: [%s]' % (cnum, cell_obj.value))

        data = {}
        data['first_name'] = xl_sheet_pitcher.cell(rnum, 0).value
        data['last_name'] = xl_sheet_pitcher.cell(rnum, 1).value
        data['position'] = xl_sheet_pitcher.cell(rnum, 2).value
        data['age'] = xl_sheet_pitcher.cell(rnum, 3).value
        data['team'] = xl_sheet_pitcher.cell(rnum, 4).value
        data['pit_hand'] = xl_sheet_pitcher.cell(rnum, 5).value
        data['kinds'] = xl_sheet_pitcher.cell(rnum, 6).value
        data['era'] = xl_sheet_pitcher.cell(rnum, 7).value
        data['w'] = xl_sheet_pitcher.cell(rnum, 8).value
        data['l'] = xl_sheet_pitcher.cell(rnum, 9).value
        data['sv'] = xl_sheet_pitcher.cell(rnum, 10).value
        data['k9'] = xl_sheet_pitcher.cell(rnum, 11).value

        p = Pitcher(**data)
        p.save()
        print p.show_statistics()
    for rnum in range(nrows_h):
        if rnum == 0:
            continue
        data['first_name'] = xl_sheet_hitter.cell(rnum, 0).value
        data['last_name'] = xl_sheet_hitter.cell(rnum, 1).value
        data['position'] = xl_sheet_hitter.cell(rnum, 2).value
        data['age'] = xl_sheet_hitter.cell(rnum, 3).value
        data['team'] = xl_sheet_hitter.cell(rnum, 4).value
        data['hit_hand'] = xl_sheet_hitter.cell(rnum, 5).value
        data['avg'] = xl_sheet_hitter.cell(rnum, 6).value
        data['obp'] = xl_sheet_hitter.cell(rnum, 7).value
        data['hr'] = xl_sheet_hitter.cell(rnum, 8).value
        data['rbi'] = xl_sheet_hitter.cell(rnum, 9).value
        data['r'] = xl_sheet_hitter.cell(rnum, 10).value

        h = Hitter(**data)
        h.save()
        print h.show_statistics()