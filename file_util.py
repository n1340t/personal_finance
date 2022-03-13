import abc

class FileUtil(abc.ABC):
  file_path = './csv_docs'
  @abc.abstractmethod
  def get_latest_file(self):
    return NotImplementedError
  
  @abc.abstractmethod
  def read_file(self):
    return NotImplementedError