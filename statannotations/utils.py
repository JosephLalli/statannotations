import pandas as pd


def raise_expected_got(expected, for_, got, error_type=ValueError):
    """Raise a standardized error message.

    Raise an `error_type` error with the message
        Expected `expected` for `for_`; got `got` instead.
    Or, if `for_` is `None`,
        Expected `expected`; got `got` instead.

    """
    rendered_for = f"for {for_}" if for_ is not None else ""

    raise error_type(f'Expected {expected} {rendered_for}; got {got} instead.')


def assert_is_in(x, valid_values, error_type=ValueError, label=None):
    """Raise an error if x is not in valid_values."""
    if x not in valid_values:
        raise_expected_got(
            f'one of {valid_values}', label, x, error_type=error_type)


def remove_null(series):
    return series[pd.notnull(series)]
