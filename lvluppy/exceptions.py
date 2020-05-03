class StatusCodeException(Exception):
  def __init__(self, response):
    if 'Content-Type' in response.headers \
    and 'application/json' in response.headers['Content-Type']:
      try:
        self.details = response.json()
      except:
        self.details = response.text
    else:
      self.details = response.text
    self.status_code = response.status_code

class UnauthorizedException(StatusCodeException):
  pass

class NotFoundException(StatusCodeException):
  pass

class WtfException(StatusCodeException):
  pass
