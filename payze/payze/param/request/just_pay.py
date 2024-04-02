"""
just pay method request parameters
"""
import uuid
from dataclasses import dataclass

from payze.param.request import base


@dataclass
class JustPay:
    """
    the paywith card parameters model
    """
    amount: float
    language: str = "UZ"
    source: str = "Card"
    currency: str = "UZS"
    hooks: base.Hooks = None
    metadata: base.Metadata = None
    idempotency_key: str = str(uuid.uuid4())

    def to_dict(self):
        """
        the dict representation.
        """
        if self.metadata:
            self.metadata = self.metadata.to_dict()

        return {
            "amount": self.amount,
            "currency": self.currency,
            "hooks": self.hooks.to_dict(),
            "idempotencyKey": self.idempotency_key,
            "source": self.source,
            "metadata": self.metadata
        }
