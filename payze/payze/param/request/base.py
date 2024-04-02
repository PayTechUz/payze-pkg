"""
base params requests.
"""
from typing import List
from typing import Optional
from dataclasses import dataclass


@dataclass
class Hooks:
    """
    the web hooks.
    """
    web_hook_gateway: str
    error_redirect_gateway: str
    success_redirect_gateway: str

    def to_dict(self):
        """
        dict representation.
        """
        return {
            "webhookGateway": self.web_hook_gateway,
            "successRedirectGateway": self.success_redirect_gateway,
            "errorRedirectGateway": self.error_redirect_gateway
        }


@dataclass
class ShippingAddress:
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

    def to_dict(self):
        """
        Dictionary representation.
        """
        return {
            "City": self.city,
            "Line1": self.line1,
            "Line2": self.line2,
            "State": self.state,
            "Country": self.country,
            "LastName": self.last_name,
            "FirstName": self.first_name,
            "PostalCode": self.postal_code,
            "PhoneNumber": self.phone_number
        }


@dataclass
class BillingAddress:
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

    def to_dict(self):
        """
        dict representation.
        """
        return {
            "City": self.city,
            "Line1": self.line1,
            "Line2": self.line2,
            "State": self.state,
            "Country": self.country,
            "LastName": self.last_name,
            "FirstName": self.first_name,
            "PostalCode": self.postal_code,
            "PhoneNumber": self.phone_number
        }


@dataclass
class UzRegulatoryOrderDetails:
    """
    Regulatory order details
    """
    taxi_tin: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    taxi_pinfl: Optional[str] = None
    taxi_vehicle_number: Optional[str] = None

    def to_dict(self):
        """
        Dictionary representation.
        """
        return {
            "TaxiTin": self.taxi_tin,
            "Latitude": self.latitude,
            "Longitude": self.longitude,
            "TaxiPinfl": self.taxi_pinfl,
            "TaxiVehicleNumber": self.taxi_vehicle_number
        }


@dataclass
class Order:
    """
    Order details
    """
    order_id: Optional[str] = None
    order_items: Optional[str] = None
    billing_address: BillingAddress = None
    shipping_address: ShippingAddress = None
    uz_regulatory_order_details: UzRegulatoryOrderDetails = None

    def to_dict(self):
        """
        Dictionary representation.
        """
        if self.billing_address:
            self.billing_address = self.billing_address.to_dict()

        if self.shipping_address:
            self.shipping_address = self.shipping_address.to_dict()

        if self.shipping_address:
            self.shipping_address = self.shipping_address.to_dict()

        return {
            "OrderId": str(self.order_id),
            "OrderItems": self.order_items,
            "BillingAddress": self.billing_address,
            "ShippingAddress": self.shipping_address,
            "UzRegulatoryOrderDetails": self.uz_regulatory_order_details
        }


@dataclass
class ExtraAttributes:
    """
    Extra attributes
    """
    key: str
    value: str
    description: Optional[str] = None

    def to_dict(self):
        """
        Dictionary representation.
        """
        return {
            "Key": self.key,
            "Value": self.value,
            "Description": self.description
        }


@dataclass
class Metadata:
    """
    Metadata details
    """
    order: Order
    channel: Optional[str] = None
    extra_attributes: List[ExtraAttributes] = None

    def to_dict(self):
        """
        Dictionary representation.
        """
        extra_attributes = []

        if self.order:
            self.order = self.order.to_dict()

        if self.extra_attributes:
            for item in self.extra_attributes:
                for key, value in item.items():
                    extra_attributes.append(
                        ExtraAttributes(
                            key=str(key),
                            value=str(value)
                        ).to_dict()
                    )

        return {
            "Order": self.order,
            "Channel": self.channel,
            "ExtraAttributes": extra_attributes
        }
