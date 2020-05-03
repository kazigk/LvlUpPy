class PaymentLinkInfo:
  def __init__(
    self,
    amountInt,
    amountWithFeeInt,
    payed,
    **kwargs
  ):
    self.__amount = amountInt / 100.0
    self.__amountWithFee = amountWithFeeInt / 100.0
    self.__payed = payed

  @property
  def amount(self):
    """:rtype: float"""
    return self.__amount

  @property
  def amountWithFee(self):
    """:rtype: float"""
    return self.__amountWithFee

  @property
  def payed(self):
    """:rtype: bool"""
    return self.__payed
