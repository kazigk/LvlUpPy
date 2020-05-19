from .RequestsHelper import RequestsHelper
from .models.UserInfo import UserInfo
from .models.ReferralCode import ReferralCode
from .models.AuditLog import AuditLog
from .models.Order import Order
from .models.Payment import Payment
from .models.PaymentLink import PaymentLink
from .models.PaymentLinkInfo import PaymentLinkInfo
from .models.PageModel import PageModel
from .models.Service import Service
from .models.VPSInfo import VPSInfo


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

  def getAuditLog(self, limit=10, afterId=None, beforeId=None):
    """
    :rtype: PageModel[AuditLog]
    :param afterId: Get results after ID
    :type afterId: int
    :param beforeId: Get results before ID
    :type beforeId: int
    """
    return PageModel(
      **self._get_page('/me/log', limit, afterId, beforeId), model=AuditLog
    )

  def getReferralCodes(self):
    """
    :rtype: [ReferralCode]
    :param afterId: Get results after ID
    :type afterId: int
    :param beforeId: Get results before ID
    :type beforeId: int
    """
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

  def getOrders(self, limit=10, afterId=None, beforeId=None):
    """
    :rtype: PageModel[Order]
    :param afterId: Get results after ID
    :type afterId: int
    :param beforeId: Get results before ID
    :type beforeId: int
    """
    return PageModel(
      **self._get_page('/orders', limit, afterId, beforeId), model=Order
    )

  def getPayments(self, limit=10, afterId=None, beforeId=None):
    """
    :rtype: PageModel[Payment]
    :type afterId: int
    :type beforeId: int
    """
    return PageModel(
      **self._get_page('/payments', limit, afterId, beforeId), model=Payment
    )

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

  def getServices(self, limit=10, afterId=None, beforeId=None):
    """:rtype: [Service]"""
    return [Service(**i) for i in self._get('/services')['services']]

  def startVPS(self, id):
    """
    :param id: ID of VPS
    :type id: int
    """
    self._post('/services/vps/{0}/start'.format(id))

  def stopVPS(self, id):
    """
    :param id: ID of VPS
    :type id: int
    """
    self._post('/services/vps/{0}/stop'.format(id))

  def getVPSInfo(self, id):
    """
    :param id: ID of VPS
    :type id: int
    """
    return VPSInfo(**self._get('/services/vps/{0}/stats'.format(id)))
