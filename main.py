from datetime import datetime
from serializer import Serializer
from money_lover import MoneyLover
from bmo import BMO

lover = MoneyLover()
lover_file = lover.read_file()
lover_data = lover.serialize(lover_file)

bmo = BMO()
bmo_data = bmo.read_file('./csv_docs/bank/jan2021.csv')
bmo_data = bmo.serialize(bmo_data)

date_set = lover.get_date_set().union(bmo.get_date_set())
max_date_bmo = bmo.get_max_date()
min_date_bmo = bmo.get_min_date()

for date in date_set:
  date_str = date.strftime(Serializer.date_format)
  bm_trans = bmo_data.get(date_str, None)
  lover_trans = lover_data.get(date_str, None)
  if bm_trans and lover_trans:
    # print('bmo', bm_trans)
    # print('lover', lover_trans)
    for trans in bm_trans:
      if not trans in lover_trans:
        bm_trans[trans] = 'Missing Trans'
  elif bm_trans and lover_trans is None:
    for transaction in bmo_data[date_str]:
      bmo_data[date_str][transaction] = 'Missing Trans'
  elif bm_trans is None and lover_trans and min_date_bmo <= date <= max_date_bmo:
    bmo_data[date_str] = 'Missing Date'