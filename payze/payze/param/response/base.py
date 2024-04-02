"""
the just_pay response model
"""
from typing import Optional

from pydantic import Field
from pydantic import BaseModel


class CardPaymentDetails(BaseModel):
    """
    the card payment details model.
    """
    applePay: bool
    cardExpiration: Optional[str]
    cardMask: Optional[str]
    cardOwnerEntityType: Optional[str]
    googlePay: bool
    merchantId: Optional[str]
    preauthorize: bool
    processingVendor: Optional[str]
    processingVendorId: Optional[str]
    rrn: Optional[str]
    secureCardId: Optional[str]
    terminalId: Optional[str]
    token: Optional[str]


class Hooks(BaseModel):
    """
    the webhooks model
    """
    errorRedirectGateway: Optional[str]
    successRedirectGateway: Optional[str]
    webhookGateway: Optional[str]


class PaymentData(BaseModel):
    """
    the payment data model
    """
    amount: int
    blockedAmount: Optional[int]
    blockedDate: Optional[str]
    capturedAmount: Optional[int]
    capturedDate: Optional[str]
    cardPayment: CardPaymentDetails
    channel: Optional[str]
    createdDate: str
    crossCurrencySettlement: Optional[str]
    currency: str
    fee: Optional[int]
    hooks: Hooks
    id: int
    idempotencyKey: str
    language: Optional[str]
    lastModifiedDate: str
    metadata: Optional[dict]
    network: Optional[str]
    payer: Optional[dict]
    payment_url: str = Field(
        alias="paymentUrl"
    )
    receipt: Optional[str]
    refundedAmount: Optional[int]
    refundedDate: Optional[str]
    rejectReason: Optional[str]
    rejectedDate: Optional[str]
    requesterId: int
    reverseDate: Optional[str]
    reversedAmount: Optional[int]
    sandBox: bool
    settled: Optional[str]
    settledBalanceAmount: Optional[int]
    settledDate: Optional[str]
    shareLink: Optional[str]
    source: str
    status: str
    transactionId: str
    type: str
    version: int
    walletPayment: Optional[dict]


class Data(BaseModel):
    """
    the data model
    """
    payment: PaymentData


class Status(BaseModel):
    """
    the status model
    """
    errors: Optional[str]
    message: Optional[str]
    type: Optional[str]
