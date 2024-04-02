"""
fastapi and payze webhook examples
"""
import logging

import fastapi
import uvicorn

from payze.client import Payze
from payze.param import webhook
from payze.param import PayzeOPS
from payze.param import request as payze_req


app = fastapi.FastAPI()
logger = logging.getLogger(__name__)


ops = PayzeOPS(
    url="https://payze.io",
    auth_token="your-auth:token",
    hooks=payze_req.Hooks(
        web_hook_gateway="https://mysite.com/v1/webhook/payze/success",
        error_redirect_gateway="https://mysite.com",
        success_redirect_gateway="https://mysite.com",
    )
)

payze = Payze(ops=ops)


@app.get("/v1/payment/pay-link")
def get_pay_link(order_id: str):
    """
    the get pay link endpoint.
    """
    metadata = payze_req.Metadata(
        order=payze_req.Order(order_id),
    )

    req_params = payze_req.JustPay(
        amount=1,
        metadata=metadata,
    )

    resp = payze.just_pay(
        req_params=req_params,
        reason="for_trip",
    )

    return {
        "pay_link": resp.data.payment.payment_url
    }


@app.post("/v1/webhook/payze/success")
def payze_webhook(payment_info: webhook.JustPaySerializer):
    """
    the payze webhook endpoint.
    """
    info = f"Order: {payment_info.metadata.order.order_id} has been triggered to {payment_info.payment_status}"  # noqa
    print(info)

    return {
        "is_webhook_accepted": True,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
