from Config.CommonImports import *

class CreditCard:
  def __init__(self, lastDigits:int, bank:str, limit:float, closingDay:int, dueDay:int):
    self.lastDigits = lastDigits
    self.bank = bank
    self.limit = limit
    self.closingDay = closingDay
    self.dueDay = dueDay
    
  @classmethod
  def createCreditCard(cls, lastDigits:int, bank:str, limit:float, closingDay:int, dueDay:int):
    return cls(lastDigits, bank, limit, dueDay, closingDay)

  def toDict(self) -> Dict[str, Any]:
    return{
      'lastDigits': self.lastDigits,
      'bank': self.bank,
      'limit': self.limit,
      'closingDay': self.closingDay,
      'dueDay': self.dueDay
    }
    
  @classmethod
  def fromDict(cls, data: Dict[str, Any]) -> 'CreditCard':
    
    return cls(data['last_digits'], data['bank'], data['limit'], data['closing_day'], data['due_day'])

