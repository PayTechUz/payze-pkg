payze = Payze(
    ops=PayzeOPS(
        url="https://payze.io",
        auth_token="13F44DB31A5345EE8C16C98A8EFBA4BA:4268540BABB647E89C8535F62E0DD30B",  # noqa
        hooks=payze_req.Hooks(
            web_hook_gateway="https://webhook.site/3d9fbdda-125c-404b-b2b6-88a6b0283a9b", # noqa
            error_redirect_gateway="https://webhook.site/3d9fbdda-125c-404b-b2b6-88a6b0283a9b", # noqa
            success_redirect_gateway="https://webhook.site/3d9fbdda-125c-404b-b2b6-88a6b0283a9b", # noqa
        )
    )
)


resp = payze.just_pay(
    req_params=payze_req.JustPay(
        amount=1
    )
)