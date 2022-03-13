import abc

class Serializer(abc.ABC):
  date_format = '%Y-%m-%d'
  @abc.abstractmethod
  def serialize(self):
    return NotImplementedError