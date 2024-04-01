# Payze Uzbekistan implementation.

Support Group - <a href="https://t.me/+Ng1axYLNyBAyYTRi">Telegram</a> <br/>

## Installation

```shell
pip install payze-pkg
```

## Payze PKG
- [JustPay](#justpay)
# Methods

## JustPay

```python
from payze.client import Payze
from payze.param import PayzeOPS
from payze.param import request as payze_req


payze = Payze(
    ops=PayzeOPS(
        url="https://payze.io",
        auth_token="get-your-auth-token-from-payze",
        hooks=payze_req.Hooks(
            web_hook_gateway="https://mysite.com/v1/webhook/payze/success",
            error_redirect_gateway="https://mysite.com/v1/payment/payze/re-pay",
            success_redirect_gateway="https://mysite.com/v1/payze/thanks",
        )
    )
)

resp = payze.just_pay(
    req_params=payze_req.JustPay(
        amount=1  # UZS sum...
    )
)
print(resp)
```
