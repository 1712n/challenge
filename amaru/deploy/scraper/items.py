# Items docs:
# http://doc.scrapy.org/en/latest/topics/items.html
import hashlib
from dataclasses import dataclass


@dataclass
class SlowmistItem:
    time: str
    target: str
    description: str
    amount_of_loss: str
    attack_method: str
    reference_url: str
    _id: str = None

    def __post_init__(self):
        key = self.time + self.target + self.description
        self._id = hashlib.sha256(key.encode()).hexdigest()[:16]
