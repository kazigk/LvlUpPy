import requests
from .exceptions import *


class RequestsHelper:
  def __init__(self):
    self._baseUrl = ''
    self._headers = {}

  @staticmethod
  def _processResponse(response):
    if response.status_code in [200]:
      # this will raise json.decoder.JSONDecodeError on failure
      # i'm intentionnaly not catching it and not checking content-type here
      return response.json()
    elif response.status_code == 401:
      raise UnauthorizedException(response)
    elif response.status_code == 404:
      raise NotFoundException(response)
    else:
      raise WtfException(response)

  def _get(self, path, params=None):
    return self._processResponse(
      requests.get(self._baseUrl + path, headers=self._headers, params=params)
    )

  def _post(self, path, json=None):
    return self._processResponse(
      requests.post(self._baseUrl + path, headers=self._headers, json=json)
    )

  def _put(self, path, json=None):
    return self._processResponse(
      requests.put(self._baseUrl + path, headers=self._headers, json=json)
    )

  def _delete(self, path):
    return self._processResponse(
      requests.delete(self._baseUrl + path, headers=self._headers)
    )

  def _get_page(self, path, limit=10, afterId=None, beforeId=None):
    return self._get(path, params={
      'limit': limit,
      'afterId': afterId,
      'beforeId': beforeId
    })
