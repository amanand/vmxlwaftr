#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ErrCode:
  """
  Enum for the Error Codes returned by the Thrift Service APIs
  """
  EOK = 0
  INVALID_ARGUMENTS = 1
  NO_RECORDS_FOUND = 2
  DAEMON_NOT_RESPONDING = 3
  ROUTE_ADD_RETURN_FAILED = 1001
  ROUTE_ADD_RETURN_TABLEID_INVALID = 1002
  ROUTE_ADD_RETURN_IFLIDX_INVALID = 1003
  ROUTE_ADD_RETURN_LCLADDR_INVALID = 1004
  ROUTE_ADD_RETURN_PREFIX_INVALID = 1005
  ROUTE_ADD_RETURN_GWHANDLE_INVALID = 1006
  ROUTE_ADD_RETURN_DYNIFL_CREATE_FAILED = 1007
  ROUTE_ADD_RETURN_MASK2SHORT = 1008
  ROUTE_ADD_RETURN_BAD_NEXTHOP = 1009
  ROUTE_ADD_RETURN_NEXTHOP_ECMP_LIMIT = 1010
  ROUTE_ADD_RETURN_MASK2LONG = 1011
  ROUTE_ADD_RETURN_RTT_NOT_READY = 1012
  ROUTE_DELETE_RETURN_ROUTE_NOTFOUND = 1013
  ROUTE_DELETE_RETURN_TABLE_NOTFOUND = 1014
  ROUTE_DELETE_RETURN_MASK2SHORT = 1015
  ROUTE_DELETE_RETURN_MASK2LONG = 1016
  ROUTE_DELETE_RETURN_COOKIE_MISMATCH = 1017
  FW_FILTER_NOT_FOUND = 1500
  FW_FILTER_IN_USE = 1501
  FW_FILTER_ALREADY_EXISTS = 1502
  FW_FILTER_CONFIG_ERR = 1503
  FW_TERM_NOT_FOUND = 1504
  FW_TERM_ALREADY_EXISTS = 1505
  FW_TERM_CONFIG_ERR = 1506
  FW_TERM_CONFLICT_ERR = 1507
  FW_POLICER_NOT_FOUND = 1508
  FW_POLICER_IN_USE = 1509
  FW_POLICER_ALREADY_EXISTS = 1510
  FW_POLICER_CONFIG_ERR = 1511
  FW_ATTACH_POINT_NOT_FOUND = 1512
  FW_ATTACH_POINT_IN_USE = 1513
  FW_DFW_INDEX_EXHAUSTED = 1514
  FW_OUT_OF_MEMORY_ERR = 1515
  FW_INTERNAL_ERR = 1516
  FW_TIMER_NOT_FOUND = 1517
  FW_TIMER_IN_USE = 1518
  FW_TIMER_ALREADY_EXISTS = 1519
  FW_TIMER_CONFIG_ERR = 1520
  FW_TNP_SESSION_ERR = 1521
  FW_PREFIX_LIST_NOT_FOUND = 1522
  FW_FCU_NOT_FOUND = 1523
  FW_INVALID_TERM = 1524
  FW_TERM_CONTAINS_NO_MATCH = 1525
  FW_TERM_MATCH_INVALID = 1526
  FW_TERM_ACTION_INVALID = 1527
  FW_TERM_END_FAILED = 1528
  FW_FILTER_TRANS_SEND = 1529
  FW_FILTER_TRANS_ALLOC = 1530
  FW_TERM_START_FAILED = 1531
  FW_FILTER_WRONG_DIRECTION = 1532
  FW_POLICER_INVALID_PARAMETER = 1533
  FW_POLICER_ACTION_DISCARD = 1534
  FW_FILTER_HANDLE_ALLOC = 1535
  FW_FILTER_COUNTER_ADD = 1536
  FW_FILTER_STATS_TRANS_ALLOC = 1537
  FW_FILTER_STATS_TRANS_SEND = 1538
  FW_POLICER_STATS_TRANS_ADD = 1539
  FW_STATS_NOT_AVAILABLE = 1540
  GENERAL_ERROR = 2000

  _VALUES_TO_NAMES = {
    0: "EOK",
    1: "INVALID_ARGUMENTS",
    2: "NO_RECORDS_FOUND",
    3: "DAEMON_NOT_RESPONDING",
    1001: "ROUTE_ADD_RETURN_FAILED",
    1002: "ROUTE_ADD_RETURN_TABLEID_INVALID",
    1003: "ROUTE_ADD_RETURN_IFLIDX_INVALID",
    1004: "ROUTE_ADD_RETURN_LCLADDR_INVALID",
    1005: "ROUTE_ADD_RETURN_PREFIX_INVALID",
    1006: "ROUTE_ADD_RETURN_GWHANDLE_INVALID",
    1007: "ROUTE_ADD_RETURN_DYNIFL_CREATE_FAILED",
    1008: "ROUTE_ADD_RETURN_MASK2SHORT",
    1009: "ROUTE_ADD_RETURN_BAD_NEXTHOP",
    1010: "ROUTE_ADD_RETURN_NEXTHOP_ECMP_LIMIT",
    1011: "ROUTE_ADD_RETURN_MASK2LONG",
    1012: "ROUTE_ADD_RETURN_RTT_NOT_READY",
    1013: "ROUTE_DELETE_RETURN_ROUTE_NOTFOUND",
    1014: "ROUTE_DELETE_RETURN_TABLE_NOTFOUND",
    1015: "ROUTE_DELETE_RETURN_MASK2SHORT",
    1016: "ROUTE_DELETE_RETURN_MASK2LONG",
    1017: "ROUTE_DELETE_RETURN_COOKIE_MISMATCH",
    1500: "FW_FILTER_NOT_FOUND",
    1501: "FW_FILTER_IN_USE",
    1502: "FW_FILTER_ALREADY_EXISTS",
    1503: "FW_FILTER_CONFIG_ERR",
    1504: "FW_TERM_NOT_FOUND",
    1505: "FW_TERM_ALREADY_EXISTS",
    1506: "FW_TERM_CONFIG_ERR",
    1507: "FW_TERM_CONFLICT_ERR",
    1508: "FW_POLICER_NOT_FOUND",
    1509: "FW_POLICER_IN_USE",
    1510: "FW_POLICER_ALREADY_EXISTS",
    1511: "FW_POLICER_CONFIG_ERR",
    1512: "FW_ATTACH_POINT_NOT_FOUND",
    1513: "FW_ATTACH_POINT_IN_USE",
    1514: "FW_DFW_INDEX_EXHAUSTED",
    1515: "FW_OUT_OF_MEMORY_ERR",
    1516: "FW_INTERNAL_ERR",
    1517: "FW_TIMER_NOT_FOUND",
    1518: "FW_TIMER_IN_USE",
    1519: "FW_TIMER_ALREADY_EXISTS",
    1520: "FW_TIMER_CONFIG_ERR",
    1521: "FW_TNP_SESSION_ERR",
    1522: "FW_PREFIX_LIST_NOT_FOUND",
    1523: "FW_FCU_NOT_FOUND",
    1524: "FW_INVALID_TERM",
    1525: "FW_TERM_CONTAINS_NO_MATCH",
    1526: "FW_TERM_MATCH_INVALID",
    1527: "FW_TERM_ACTION_INVALID",
    1528: "FW_TERM_END_FAILED",
    1529: "FW_FILTER_TRANS_SEND",
    1530: "FW_FILTER_TRANS_ALLOC",
    1531: "FW_TERM_START_FAILED",
    1532: "FW_FILTER_WRONG_DIRECTION",
    1533: "FW_POLICER_INVALID_PARAMETER",
    1534: "FW_POLICER_ACTION_DISCARD",
    1535: "FW_FILTER_HANDLE_ALLOC",
    1536: "FW_FILTER_COUNTER_ADD",
    1537: "FW_FILTER_STATS_TRANS_ALLOC",
    1538: "FW_FILTER_STATS_TRANS_SEND",
    1539: "FW_POLICER_STATS_TRANS_ADD",
    1540: "FW_STATS_NOT_AVAILABLE",
    2000: "GENERAL_ERROR",
  }

  _NAMES_TO_VALUES = {
    "EOK": 0,
    "INVALID_ARGUMENTS": 1,
    "NO_RECORDS_FOUND": 2,
    "DAEMON_NOT_RESPONDING": 3,
    "ROUTE_ADD_RETURN_FAILED": 1001,
    "ROUTE_ADD_RETURN_TABLEID_INVALID": 1002,
    "ROUTE_ADD_RETURN_IFLIDX_INVALID": 1003,
    "ROUTE_ADD_RETURN_LCLADDR_INVALID": 1004,
    "ROUTE_ADD_RETURN_PREFIX_INVALID": 1005,
    "ROUTE_ADD_RETURN_GWHANDLE_INVALID": 1006,
    "ROUTE_ADD_RETURN_DYNIFL_CREATE_FAILED": 1007,
    "ROUTE_ADD_RETURN_MASK2SHORT": 1008,
    "ROUTE_ADD_RETURN_BAD_NEXTHOP": 1009,
    "ROUTE_ADD_RETURN_NEXTHOP_ECMP_LIMIT": 1010,
    "ROUTE_ADD_RETURN_MASK2LONG": 1011,
    "ROUTE_ADD_RETURN_RTT_NOT_READY": 1012,
    "ROUTE_DELETE_RETURN_ROUTE_NOTFOUND": 1013,
    "ROUTE_DELETE_RETURN_TABLE_NOTFOUND": 1014,
    "ROUTE_DELETE_RETURN_MASK2SHORT": 1015,
    "ROUTE_DELETE_RETURN_MASK2LONG": 1016,
    "ROUTE_DELETE_RETURN_COOKIE_MISMATCH": 1017,
    "FW_FILTER_NOT_FOUND": 1500,
    "FW_FILTER_IN_USE": 1501,
    "FW_FILTER_ALREADY_EXISTS": 1502,
    "FW_FILTER_CONFIG_ERR": 1503,
    "FW_TERM_NOT_FOUND": 1504,
    "FW_TERM_ALREADY_EXISTS": 1505,
    "FW_TERM_CONFIG_ERR": 1506,
    "FW_TERM_CONFLICT_ERR": 1507,
    "FW_POLICER_NOT_FOUND": 1508,
    "FW_POLICER_IN_USE": 1509,
    "FW_POLICER_ALREADY_EXISTS": 1510,
    "FW_POLICER_CONFIG_ERR": 1511,
    "FW_ATTACH_POINT_NOT_FOUND": 1512,
    "FW_ATTACH_POINT_IN_USE": 1513,
    "FW_DFW_INDEX_EXHAUSTED": 1514,
    "FW_OUT_OF_MEMORY_ERR": 1515,
    "FW_INTERNAL_ERR": 1516,
    "FW_TIMER_NOT_FOUND": 1517,
    "FW_TIMER_IN_USE": 1518,
    "FW_TIMER_ALREADY_EXISTS": 1519,
    "FW_TIMER_CONFIG_ERR": 1520,
    "FW_TNP_SESSION_ERR": 1521,
    "FW_PREFIX_LIST_NOT_FOUND": 1522,
    "FW_FCU_NOT_FOUND": 1523,
    "FW_INVALID_TERM": 1524,
    "FW_TERM_CONTAINS_NO_MATCH": 1525,
    "FW_TERM_MATCH_INVALID": 1526,
    "FW_TERM_ACTION_INVALID": 1527,
    "FW_TERM_END_FAILED": 1528,
    "FW_FILTER_TRANS_SEND": 1529,
    "FW_FILTER_TRANS_ALLOC": 1530,
    "FW_TERM_START_FAILED": 1531,
    "FW_FILTER_WRONG_DIRECTION": 1532,
    "FW_POLICER_INVALID_PARAMETER": 1533,
    "FW_POLICER_ACTION_DISCARD": 1534,
    "FW_FILTER_HANDLE_ALLOC": 1535,
    "FW_FILTER_COUNTER_ADD": 1536,
    "FW_FILTER_STATS_TRANS_ALLOC": 1537,
    "FW_FILTER_STATS_TRANS_SEND": 1538,
    "FW_POLICER_STATS_TRANS_ADD": 1539,
    "FW_STATS_NOT_AVAILABLE": 1540,
    "GENERAL_ERROR": 2000,
  }


class RetStatus:
  """
  Data type for Error Handling
  Every API returns this under all circumstances.
  When there are API-specific return values, they are nested with
  this data type.
  ErrCode is 0 (EOK) when API invocation is a SUCCESS.
  Errcode is a negative integer when API invocation is a FAILURE.
  ErrStr is valid only when ErrCode != 0.

  Attributes:
   - err_code: Error code
   - err_str: Error string
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'err_code', None, None, ), # 1
    (2, TType.STRING, 'err_str', None, None, ), # 2
  )

  def __init__(self, err_code=None, err_str=None,):
    self.err_code = err_code
    self.err_str = err_str

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.err_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.err_str = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RetStatus')
    if self.err_code is not None:
      oprot.writeFieldBegin('err_code', TType.I32, 1)
      oprot.writeI32(self.err_code)
      oprot.writeFieldEnd()
    if self.err_str is not None:
      oprot.writeFieldBegin('err_str', TType.STRING, 2)
      oprot.writeString(self.err_str)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
