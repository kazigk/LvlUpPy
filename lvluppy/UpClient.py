from .RequestsHelper import RequestsHelper
from .models.UserInfo import UserInfo
from .models.ReferralCode import ReferralCode
from .models.AuditLog import AuditLog
from .models.Order import Order
from .models.Payment import Payment
from .models.PaymentLink import PaymentLink
from .models.PaymentLinkInfo import PaymentLinkInfo


class UpClient(RequestsHelper):
  """
    :param apiKey: Your LvlUp.pro access token
    :type apiKey: str
    :param baseUrl: API URL
    :type baseUrl: str
  """

  def __init__(self, apiKey, baseUrl='https://api.lvlup.pro/v4'):
    super().__init__()
    self._baseUrl = baseUrl
    self._headers['Authorization'] = 'Bearer ' + apiKey

  def getUserInfo(self):
    """:rtype: UserInfo"""
    return UserInfo(**self._get('/me'))

  def getAuditLog(self):
    """:rtype: [AuditLog]"""
    # TODO: implement query parameters
    return [AuditLog(**i) for i in self._get('/me/log')['items']]

  def getReferralCodes(self):
    """:rtype: [ReferralCode]"""
    r = self._get('/me/referral')
    # unlike other endpoints, this actually return null value
    # instead of empty list when no promo codes are created on the account
    if r['codes'] is None:
      return list()
    else:
      return [ReferralCode(**i) for i in r['codes']]

  def createReferralCode(self):
    """:rtype: str"""
    return self._post('/me/referral/generic')['code']

  def getOrders(self):
    """:rtype: [Order]"""
    # TODO: implement query parameters
    return [Order(**i) for i in self._get('/orders')['items']]

  def getPayments(self):
    """:rtype: [Payment]"""
    # TODO: implement query parameters
    return [Payment(**i) for i in self._get('/payments')['items']]

  def createPaymentLink(self, amount, redirectUrl=None, webhookUrl=None):
    """
    :type amount: float
    :type redirectUrl: str
    :type webhookUrl: str
    :rtype: PaymentLink
    """
    return PaymentLink(**self._post('/wallet/up', json={
      'amount': '{0:.2f}'.format(amount),
      'redirectUrl': redirectUrl,
      'webhookUrl': webhookUrl
    }))

  def getPaymentLinkInfo(self, id):
    """
    :param id: ID from PaymentLink
    :type id: str
    :rtype: PaymentLinkInfo
    """
    return PaymentLinkInfo(**self._get('/wallet/up/' + id))

  def getWalletBalance(self):
    """:rtype: float"""
    return self._get('/wallet')['balancePlnInt'] / 100.0
