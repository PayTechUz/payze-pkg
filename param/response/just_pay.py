"""
the just_pay response model
"""
from param.response import base


class JustPay(base.BaseModel):
    """
    the just pay response model.
    """
    data: base.Data
    status: base.Status
