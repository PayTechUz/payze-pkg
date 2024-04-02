"""
the just pay webhook data.
"""
from typing import Optional

from payze.param.webhook import base


class JustPay(base.BaseModel):
    """
    the just pay main response model
    """
    source: str = base.Field(alias="Source")
    idempotency_key: str = base.Field(alias="IdempotencyKey")
    payment_id: str = base.Field(alias="PaymentId")
    type: str = base.Field(alias="Type")
    sandbox: bool = base.Field(alias="Sandbox")
    payment_status: str = base.Field(alias="PaymentStatus")
    amount: float = base.Field(alias="Amount")
    final_amount: Optional[float] = base.Field(alias="FinalAmount")
    currency: str = base.Field(alias="Currency")
    rrn: Optional[str] = base.Field(alias="RRN")
    commission: Optional[float] = base.Field(alias="Commission")
    preauthorized: bool = base.Field(alias="Preauthorized")
    can_be_captured: bool = base.Field(alias="CanBeCaptured")
    create_date: int = base.Field(alias="CreateDate")
    create_date_iso: str = base.Field(alias="CreateDateIso")
    capture_date: Optional[int] = base.Field(alias="CaptureDate")
    capture_date_iso: Optional[str] = base.Field(alias="CaptureDateIso")
    block_date: Optional[int] = base.Field(alias="BlockDate")
    block_date_iso: Optional[str] = base.Field(alias="BlockDateIso")
    token: Optional[str] = base.Field(alias="Token")
    card_mask: Optional[str] = base.Field(alias="CardMask")
    card_origination: Optional[str] = base.Field(alias="CardOrigination")
    card_owner_entity_type: Optional[str] = base.Field(alias="CardOwnerEntityType")  # noqa
    card_brand: Optional[str] = base.Field(alias="CardBrand")
    card_country: Optional[str] = base.Field(alias="CardCountry")
    card_holder: Optional[str] = base.Field(alias="CardHolder")
    expiration_date: Optional[str] = base.Field(alias="ExpirationDate")
    secure_card_id: Optional[str] = base.Field(alias="SecureCardId")
    rejection_reason: Optional[str] = base.Field(alias="RejectionReason")
    refund: Optional[base.Refund] = base.Field(alias="Refund")
    splits: Optional[list] = base.Field(alias="Splits")
    metadata: Optional[base.Metadata] = base.Field(alias="Metadata")
    payer: Optional[base.Payer] = base.Field(alias="Payer")
