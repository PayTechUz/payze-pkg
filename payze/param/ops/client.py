"""
the payze client ops
"""
from dataclasses import dataclass

from payze.param.request.base import Hooks


@dataclass
class PayzeOPS:
    """
    payze options.
    url: string -> the payze api endpoint url
    auth_token: string -> the payze auth token
    hooks: list of payze hooks.
    timeout: int -> timeout in seconds
    """
    url: str
    auth_token: str
    hooks: Hooks
    timeout: str = 10
