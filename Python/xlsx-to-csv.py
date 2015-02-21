import xlrd
import csv
import os
import sys

def xlsx_to_csv(wbook, sheet):
    xlwb = xlrd.open_workbook(wbook)
    xlsh = xlwb.sheet_by_name(sheet)
    new_csv = open(wbook[:-4]+"csv", 'wb')
    writer = csv.writer(new_csv, quoting=csv.QUOTE_ALL)
    for row in xrange(xlsh.nrows):
        writer.writerow(xlsh.row_values(row))
    new_csv.close()

def main():
    xlsx_to_csv(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
