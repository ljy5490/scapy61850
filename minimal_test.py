from __future__ import print_function
from scapy.all import *

class ASN1_Class_MMS(ASN1_Class_UNIVERSAL):
    name = "MMS"

    CONFIRMED_REQUEST_PDU = 0xa0

class ASN1_CONFIRMED_REQUEST_PDU(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.CONFIRMED_REQUEST_PDU

class BERcodec_CONFIRMED_REQUEST_PDU(BERcodec_SEQUENCE):
    tag = ASN1_Class_MMS.CONFIRMED_REQUEST_PDU


x=ASN1_SEQUENCE([ASN1_INTEGER(7), ASN1_STRING("egg"), ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
x.show()
hexdump(x)

y=ASN1_CONFIRMED_REQUEST_PDU([ASN1_INTEGER(7), ASN1_STRING("egg"), ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
y.show()
hexdump(y)
