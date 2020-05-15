class PageModel:
  """
  Iterable model for paged responses
  """
  def __init__(self, count, items, model):
    self.__total = count
    self.__items = [model(**i) for i in items]
    self.__model = model

  def __iter__(self):
    return self.__items.copy().__iter__()

  def __len__(self):
    return len(self.__items)

  @property
  def total(self):
    """
    Count of all remotely available items returned by API

    You probably want to use len() instead

    :rtype: int
    """
    return self.__total
