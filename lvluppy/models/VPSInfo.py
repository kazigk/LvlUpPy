from enum import Enum, auto


class VPSInfo:
  def __init__(
    self,
    status,
    vmUptimeS
  ):
    self.__status = VPSStatus(status)
    self.__uptime = int(vmUptimeS)

  @property
  def status(self):
    """:rtype: VPSStatus"""
    return self.__status

  @property
  def uptime(self):
    """
    :return: Uptime in seconds
    :rtype: int
    """
    return self.__uptime


class VPSStatus(Enum):
  RUNNING = "running"
  STOPPED = "stopped"
