"""
the payze client.
"""
import json
import logging

from typing import Any
from requests import Session, Response

from payze.param import PayzeOPS
from payze.param import request as payze_req
from payze.param import response as payze_res


logger = logging.getLogger(__name__)


class Payze:
    """
    payze http client implementation.
    """
    def __init__(self, ops: PayzeOPS):
        self.url = ops.url
        self.hooks = ops.hooks
        self.timeout = ops.timeout
        self.session = Session()
        self.session.headers.update({
            "Authorization": ops.auth_token,
            "Content-Type": "application/json"
        })

    def __send_request(self, url: str, req_data: str, method: str) -> Any:
        try:
            resp_data: Response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                data=req_data,
            )
            resp_data.raise_for_status()
            return resp_data.json()
        except Exception as exc:
            logger.error(f"{method} error: %s", exc)
            raise exc

    def _handle_response(
        self,
        resp_data: dict,
        resp_class: Any
    ) -> Any:
        return resp_class(**resp_data)

    def just_pay(
        self,
        req_params: payze_req.JustPay,
        **kwargs
    ) -> payze_res.JustPay:
        """
        the just pay method implementation
        """
        url = f"{self.url}/v2/api/payment"

        req_params = payze_req.JustPay(
            amount=req_params.amount,
            idempotency_key=req_params.idempotency_key,
            source=req_params.source,
            currency=req_params.currency,
            metadata=req_params.metadata
        )

        if req_params.metadata:
            req_params.metadata.extra_attributes = [
                kwargs
            ]

        req_params.hooks = self.hooks
        req_data = json.dumps(req_params.to_dict())

        resp_data = self.__send_request(url, req_data, "PUT")

        return self._handle_response(resp_data, payze_res.JustPay)
