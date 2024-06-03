from Auth.env_load import load_api_keys
from Auth.token_encode import encode
from enum import Enum

BASE_URL = 'https://api.huntress.io/v1/'
API_VERSION = '1.0.0'
API_KEY, API_SECRET = load_api_keys()
AUTH_STRING = encode(API_KEY, API_SECRET)

class Endpoint(Enum):
    """
    Enum to hold endpoint resources.
    Slash will be pre-pended to each.
    """
    ACCOUNT = 'account'
    ORGANIZATIONS = 'organizations'
    AGENTS = 'agents'
    INCIDENT_REPORTS = 'incident_reports'
    SUMMARY_REPORTS = 'reports'
    BILLING_REPORTS = 'billing_reports'

# For billing
USD = 'USD'
CAD = 'CAD'
AUD = 'AUD'
CURRENCY_TYPES = [USD, CAD, AUD]

BILL_OPEN = 'open'
BILL_PAID = 'paid'
BILL_FAILED = 'failed'
BILL_PARTIAL_REFUND = 'partial_refund'
BILL_FULL_REFUND = 'full refund'
BILL_STATUS = [BILL_OPEN, BILL_PAID, BILL_FAILED, BILL_PARTIAL_REFUND, BILL_FULL_REFUND]