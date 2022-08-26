def get_quote_for_target_apr(
        target_api: float,
        fee_amount: float = None,
):
    # false rate calculation
    rate = (target_api + fee_amount) * 0.1

    return rate
