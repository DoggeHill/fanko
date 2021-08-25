import xlsxwriter
import os

# Documentation of xlswriter here: https://xlsxwriter.readthedocs.io/index.html

class Excel:
  __DATBASE_NAME = "DATABASE.xlsx"

  def __init__(self):
    self.initializeWorksheet()
    
  def initializeWorksheet(self):
    # Create an new Excel file and add a worksheet.
    self.__workbook = xlsxwriter.Workbook(self.__DATBASE_NAME)
    self.__worksheet = self.__workbook.add_worksheet()
    
    # Widen the first column to make the text clearer.
    self.__worksheet.set_column("A:A", 20)
    self.__worksheet.set_column("B:B", 20)

    # Add a bold format to use to highlight cells.
    self.bold = self.__workbook.add_format({"bold": True})

    # Add headings
    self.__worksheet.write("A1", "date")
    self.__worksheet.write("B1", "author")
    self.__worksheet.write("C1", "title")

    # Done here
    print("excel created & ready for action")


  def write(self, row, col, expression):
    self.__worksheet.write(row, col, expression)

  def close(self):
    try:
      self.__workbook.close()
    except xlsxwriter.exceptions.FileCreateError:
      print('Please close excel before running the script')
  

if __name__ == "__main__":
  excel = Excel()
  excel.write(0, 3,"hey")

