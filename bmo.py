import glob
import os
import csv
from datetime import datetime
from controller import Controller
from file_util import FileUtil
from serializer import Serializer

class BMO(Controller,FileUtil, Serializer):
  file_path = FileUtil.file_path + '/bank/*'
  date_format = '%Y%m%d'
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
    list_of_files = glob.glob(BMO.file_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

  def read_file(self, file_path=None):
    latest_file = file_path or self.get_latest_file()
    print(latest_file)
    with open(latest_file, encoding='utf-8') as csvfile:
      # reader = csv.DictReader(csvfile.readlines()[0:10])
      reader = csv.DictReader(csvfile)
      self.file = list(reader)
      return self.file
  
  def serialize(self, data):
    for row in data:
      row['Transaction Date'] = datetime.strptime(row['Transaction Date'], BMO.date_format)
      self.__date_set.add(row['Transaction Date'])
      row['Transaction Date'] = row['Transaction Date'].strftime(Serializer.date_format)
      row['Transaction Amount'] = float(row['Transaction Amount'])
      if(self.data.get(row['Transaction Date'], None)):
        self.data[row['Transaction Date']][row['Transaction Amount']] = ''
      else:
        self.data[row['Transaction Date']] = {
          row['Transaction Amount']: '' 
        }
    
    return self.data

  def __repr__(self):
    for date in self.data:
      print(date, self.data[date])
    return ''