from datetime import datetime


class BaseModel:
  @staticmethod
  def _parseDateTime(dt):
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S%z')
