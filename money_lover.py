import glob
import os
import csv
from datetime import datetime
from controller import Controller
from file_util import FileUtil
from serializer import Serializer

class MoneyLover(Controller, FileUtil, Serializer):
  file_path = FileUtil.file_path + '/money_lover/*'
  date_format = "%d/%m/%Y"
  def __init__(self):
    self.file = None
    self.__date_set = set()
    self.data = {}

  def get_date_set(self):
    return self.__date_set

  def get_max_date(self):
    return max(self.__date_set)

  def get_min_date(self):
    return min(self.__date_set)

  def get_latest_file(self):
    list_of_files = glob.glob(MoneyLover.file_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

  def read_file(self, file_path=None):
    latest_file = file_path or self.get_latest_file()
    with open(latest_file, encoding='utf-16') as csvfile:
      # reader = csv.DictReader(csvfile.readlines()[0:50])
      reader = csv.DictReader(csvfile)
      self.file = list(reader)
      return self.file

  def serialize(self, data):
    for row in data:
      row['Date'] = datetime.strptime(row['Date'], MoneyLover.date_format)
      self.__date_set.add(row['Date'])
      row['Date'] = row['Date'].strftime(Serializer.date_format)
      row['Amount'] = -float(row['Amount'])
      if(self.data.get(row['Date'], None)):
        self.data[row['Date']][row['Amount']] = ''
      else:
        self.data[row['Date']] = {
          row['Amount']: '' 
        }
    return self.data