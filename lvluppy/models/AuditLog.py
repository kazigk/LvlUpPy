from .BaseModel import BaseModel
from enum import Enum


class AuditLog(BaseModel):
  def __init__(
    self,
    action,
    createdAt,
    id,
    ip,
    ua
  ):
    self.__action = AuditLogAction(action)
    self.__createdAt = self._parseDateTime(createdAt)
    self.__id = id
    self.__ip = ip
    self.__userAgent = ua

  @property
  def action(self):
    """:rtype: AuditLogAction"""
    return self.__action

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
  def userAgent(self):
    """:rtype: str"""
    return self.__userAgent


class AuditLogAction(Enum):
  SUCCESS = 1
  FAIL = 2
  FAIL_UNKNOWN_ACCOUNT = 3
  EMAIL_CHANGE_INIT = 4
  EMAIL_CHANGE_FINISH = 5
  SUCCESS_FROM_V2 = 6
