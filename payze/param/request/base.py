"""
base params requests.
"""
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
