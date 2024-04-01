"""
the just pay webhook data.
"""
from typing import Optional
from pydantic import BaseModel


class Refund(BaseModel):
    """
    the refund response model.
    """
    RefundId: Optional[str]
    Status: Optional[str]
    Refundable: Optional[bool]
    Amount: Optional[float]
    RequestedAmount: Optional[float]
    RejectReason: Optional[str]
    RefundDate: Optional[int]
    RefundDateIso: Optional[str]
    Revisions: Optional[list]


class Payer(BaseModel):
    """
    the payer response model
    """
    Phone: Optional[str]
    FullName: Optional[str]


class JustPay(BaseModel):
    """
    the just pay main response model
    """
    Source: str
    IdempotencyKey: str
    PaymentId: str
    Type: str
    Sandbox: bool
    PaymentStatus: str
    Amount: float
    FinalAmount: Optional[float]
    Currency: str
    RRN: Optional[str]
    Commission: Optional[float]
    Preauthorized: bool
    CanBeCaptured: bool
    CreateDate: int
    CreateDateIso: str
    CaptureDate: Optional[int]
    CaptureDateIso: Optional[str]
    BlockDate: Optional[int]
    BlockDateIso: Optional[str]
    Token: Optional[str]
    CardMask: Optional[str]
    CardOrigination: Optional[str]
    CardOwnerEntityType: Optional[str]
    CardBrand: Optional[str]
    CardCountry: Optional[str]
    CardHolder: Optional[str]
    ExpirationDate: Optional[str]
    SecureCardId: Optional[str]
    RejectionReason: Optional[str]
    Refund: Optional[Refund]
    Splits: Optional[list]
    Metadata: Optional[dict]
    Payer: Optional[Payer]
