class UserInfo:
  def  __init__(self, uid, email):
    self.__uid = uid
    self.__email = email

  @property
  def uid(self):
    """:rtype: int"""
    return self.__uid

  @property
  def email(self):
    """:rtype: str"""
    return self.__email
