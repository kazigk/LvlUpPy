from .BaseModel import BaseModel
from .ServiceType import ServiceType
from enum import Enum


class Order(BaseModel):
  def __init__(
    self,
    createdAt,
    doneAt,
    id,
    isDone,
    numberInQueue,
    planName,
    serviceId
  ):
    self.__createdAt = self._parseDateTime(createdAt)
    self.__doneAt = self._parseDateTime(doneAt) if isDone else None
    self.__id = id
    self.__isDone = isDone
    self.__numberInQueue = numberInQueue
    self.__planName = planName
    self.__serviceType = ServiceType(serviceId)

  @property
  def createdAt(self):
    """:rtype: datetime"""
    return self.__createdAt

  @property
  def doneAt(self):
    """:rtype: datetime"""
    return self.__doneAt

  @property
  def id(self):
    """:rtype: int"""
    return self.__id

  @property
  def isDone(self):
    """:rtype: boole"""
    return self.__isDone

  @property
  def numberInQueue(self):
    """:rtype: int"""
    return self.__numberInQueue

  @property
  def planName(self):
    """:rtype: str"""
    return self.__planName

  @property
  def serviceType(self):
    """:rtype: ServiceType"""
    return self.__serviceType
