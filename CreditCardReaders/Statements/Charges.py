from Config.CommonImports import *
import CreditCard

class Charges:
  def __init__(self, date: str, description: str, value: float, currency: str, card: 'CreditCard'):
    self.date = dt.strptime(date, "%d-%m-%Y")
    self.description = description
    self.value = value
    self.currency = currency
    self.card: CreditCard = card
    
  @classmethod
  def createCharge(cls, date: str, description: str, value: float, currency: str, card: 'CreditCard'):
    return cls(date, description, value, currency, card)
  
  def toDict(self) -> Dict[str, Any]:
    return {
      'date': self.date.strftime("%d-%m-%y"),
      'description': self.description,
      'value': self.value,
      'currency': self.currency,
      'card': self.card.toDict()
    }
    
  @classmethod
  def fromDict(cls, data: Dict[str, Any]) -> 'Charges':
    cardData = data['card']
    card = CreditCard.fromDict(cardData)
    return cls(
      data['data'],
      data['description'],
      data['value'],
      data['currency'],
      card
    )
  
  def toJson(self) -> str:
    return json.dumps(self.toDict(), indent=2)
  
  @classmethod
  def fromJson(cls, jsonData: str) -> 'Charges':
    data = json.loads(jsonData)
    return cls.fromDict(data)