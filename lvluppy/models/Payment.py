from .BaseModel import BaseModel
from .ServiceType import ServiceType
from enum import Enum


class Payment(BaseModel):
  def __init__(
    self,
    amount,
    createdAt,
    description,
    id,
    methodId,
    serviceId
  ):
    self.__amount = float(amount)
    self.__createdAt = self._parseDateTime(createdAt)
    self.__description = description
    self.__method = PaymentMethod(methodId)
    self.__serviceType = ServiceType(serviceId)

  @property
  def amount(self):
    """:rtype: float"""
    return self.__amount

  @property
  def createdAt(self):
    """:rtype: datetime"""
    return self.__createdAt

  @property
  def description(self):
    """:rtype: str"""
    return self.__description

  @property
  def method(self):
    """:rtype: PaymentMethod"""
    return self.__method

  @property
  def serviceType(self):
    """:rtype: ServiceType"""
    return self.__serviceType


class PaymentMethod(Enum):
  DOTPAY = 1
  SMS = 2
  FEE = 3
  TRANSFER = 4
  REFERRAL = 5
  BANK_TRANSFER = 6
  PAYPAL = 7
  PAYSAFECARD = 8
  PAYNOW = 9
  PRZELEWY24 = 10
