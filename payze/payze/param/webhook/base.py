"""
the base webhook data structure
"""
from typing import Optional, List
from pydantic import BaseModel, Field


class Refund(BaseModel):
    """
    the refund response model.
    """
    refund_id: Optional[str] = Field(
        alias="RefundId"
    )
    status: Optional[str] = Field(
        alias="Status"
    )
    refundable: Optional[bool] = Field(
        alias="Refundable"
    )
    amount: Optional[float] = Field(
        alias="Amount"
    )
    requested_amount: Optional[float] = Field(
        alias="RequestedAmount"
    )
    reject_reason: Optional[str] = Field(
        alias="RejectReason"
    )
    refund_date: Optional[int] = Field(
        alias="RefundDate"
    )
    refund_date_iso: Optional[str] = Field(
        alias="RefundDateIso"
    )
    revisions: Optional[list] = Field(
        alias="Revisions"
    )


class Payer(BaseModel):
    """
    the payer response model
    """
    phone: Optional[str] = Field(
        alias="Phone"
    )
    full_name: Optional[str] = Field(
        alias="FullName"
    )


class UzRegulatoryOrderDetails(BaseModel):
    """
    Regulatory order details
    """
    taxi_tin: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    taxi_pinfl: Optional[str] = None
    taxi_vehicle_number: Optional[str] = None


class ExtraAttributes(BaseModel):
    """
    Extra attributes
    """
    key: str = Field(alias="Key")
    value: str = Field(alias="Value")
    description: Optional[str] = Field(alias="Description")

    def to_dict(self):
        """
        Dictionary representation.
        """
        return {
            "Key": self.key,
            "Value": self.value,
            "Description": self.description
        }


class ShippingAddress(BaseModel):
    """
    Shipping address
    """
    city: Optional[str] = None
    line1: Optional[str] = None
    line2: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    postal_code: Optional[str] = None
    phone_number: Optional[str] = None


class BillingAddress(BaseModel):
    """
    billing adddress
    """
    city: Optional[str] = None
    line1: Optional[str] = None
    line2: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    postal_code: Optional[str] = None
    phone_number: Optional[str] = None


class Order(BaseModel):
    """
    Order details
    """
    order_id: Optional[str] = Field(alias="OrderId")
    order_items: Optional[str] = Field(alias="OrderItems")
    billing_address: BillingAddress = Field(alias="BillingAddress")
    shipping_address: ShippingAddress = Field(alias="ShippingAddress")
    uz_regulatory_order_details: UzRegulatoryOrderDetails = Field("UzRegulatoryOrderDetails")  # noqa


class Metadata(BaseModel):
    """
    Metadata details
    """
    order: Order = Field(alias="Order")
    channel: Optional[str] = Field(alias="Channel")
    extra_attributes: List[ExtraAttributes] = Field(alias="ExtraAttributes")
