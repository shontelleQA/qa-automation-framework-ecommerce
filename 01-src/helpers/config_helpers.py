# 01-src/helpers/config_helpers.py
import os


def get_base_url() -> str:
    """
    Returns the correct base URL based on the environment.
    Example:
        export ENV=test   (Windows: set ENV=test)
    """
    env = os.environ.get("ENV", "test").lower()  # default to 'test' if not set

    if env == "test":
        return "http://localhost:8080"     # your Docker site
    elif env == "prod":
        return "https://demo-store-prod.com"  # example of a real prod site
    else:
        raise Exception(f"Unknown environment: '{env}'. Use 'test' or 'prod'.")
