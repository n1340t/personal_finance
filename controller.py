import abc

class Controller(abc.ABC):
  @abc.abstractmethod
  def get_date_set(self):
    return NotImplementedError
  def get_max_date(self):
    return NotImplementedError
  def get_min_date(self):
    return NotImplementedError