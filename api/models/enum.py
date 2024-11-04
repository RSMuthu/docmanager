from enum import Enum


class DocType(str, Enum):
    """
    Represents types of Doc.
    """

    BANK_DRAFT = "bank-draft"
    BILL_OF_LADING = "bill-of-lading"
    BANK_DRAFT2 = "bank-draft-2"
    BILL_OF_LADING2 = "bill-of-lading-2"
    INVOICE = "invoice"
