import xlrd
import csv
import os

def xlsx_to_csv():
    xlwb = xlrd.open_workbook(sys.argv[1])
    xlsh = xlwb.sheet_by_name(sys.argv[2])
    new_csv = open(sys.argv[1], 'wb')
    writer = csv.writer(new_csv, quoting=csv.QUOTE_ALL)
    for row in xrange(xlsh.nrows):
        writer.writerow(xlsh.row_values(row))
    new_csv.close()

def main():
    xlsx_to_csv()

if __name__ == "__main__":
    main()
