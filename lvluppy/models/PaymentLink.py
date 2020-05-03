class PaymentLink:
  def __init__(
    self,
    url,
    id
  ):
    self.__url = url
    self.__id = id

  @property
  def url(self):
    """:rtype: str"""
    return self.__url

  @property
  def id(self):
    """:rtype: int"""
    return self.__id
