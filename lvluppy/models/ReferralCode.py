from .BaseModel import BaseModel


class ReferralCode(BaseModel):
  def __init__(
    self,
    active,
    code,
    commission,
    commissionEstCurMonth,
    commissionEstPrevMonth,
    createdAt,
    discount
  ):
    self.__code = code
    self.__active = active
    self.__commission = commission
    self.__commissionEstCurMonth = float(commissionEstCurMonth) if commissionEstCurMonth != '' else 0
    self.__commissionEstPrevMonth = float(commissionEstPrevMonth) if commissionEstPrevMonth != '' else 0
    self.__createdAt = self._parseDateTime(createdAt)
    self.__discount = discount

  @property
  def active(self):
    """:rtype: boole"""
    return self.__active

  @property
  def code(self):
    """:rtype: str"""
    return self.__code

  @property
  def commision(self):
    """
    :return: Percentage of commission for partner
    :rtype: int
    """
    return self.__commission

  @property
  def commissionEstCurMonth(self):
    """
    :return: Estimated commission payout for current month in PLN
    :rtype: float
    """
    return self.__commissionEstCurMonth

  @property
  def commissionEstPrevMonth(self):
    """
    :return: Estimated commission payout for previous month in PLN
    :rtype: float
    """
    return self.__commissionEstPrevMonth

  @property
  def discount(self):
    """
    :return: Percentage of discount to buyer
    :rtype: int
    """
    return self.__discount
