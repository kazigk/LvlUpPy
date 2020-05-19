from .BaseModel import BaseModel


class Service(BaseModel):
  def __init__(
    self,
    active,
    createdAt,
    id,
    ip,
    name,
    nodeId,
    payedTo,
    planName
  ):
    self.__active = bool(active)
    self.__createdAt = self._parseDateTime(createdAt)
    self.__id = int(id)
    self.__ip = ip
    self.__name = name
    self.__nodeId = int(nodeId)
    self.__payedTo = self._parseDateTime(payedTo)
    self.__planName = planName

  @property
  def active(self):
    """:rtype: bool"""
    return self.__active

  @property
  def createdAt(self):
    """:rtype: datetime"""
    return self.__createdAt

  @property
  def id(self):
    """:rtype: int"""
    return self.__id

  @property
  def ip(self):
    """:rtype: str"""
    return self.__ip

  @property
  def name(self):
    """:rtype: str"""
    return self.__name

  @property
  def nodeId(self):
    """:rtype: int"""
    return self.__nodeId

  @property
  def payedTo(self):
    """:rtype: datetime"""
    return self.__payedTo

  @property
  def planName(self):
    """:rtype: str"""
    return self.__planName
