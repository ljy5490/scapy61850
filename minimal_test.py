from __future__ import print_function
from scapy.packet import bind_layers, bind_bottom_up
from scapy.asn1packet import ASN1_Packet
from scapy.asn1fileds import ASN1F_INTEGER, ASN1F_IPADDRESS, ASN1F_OID, \
        ASN1F_SEQUENCE, ASN1F_SEQUENCE_OF, ASN1F_STRING, ASN1F_TIME_TICKS, \
        ASN1F_enum_INTEGER, ASN1F_filed, ASN1F_SEQUENCE
from scapy.asn1.asn1 import ASN1_Class_UNIVERSAL, ASN1_Codecs, ASN1_NULL, \
        ASN1_SEQUENCE
from scapy.asn1.ber import BERcodec_SEQUENCE
from scapy.sendrecv import sr1
from scapy.volatile import RandSHort, IntAutoTIme
from scapy.layers.inet import UDP, IP, ICMP

from scapy.asn1.mib import conf

class ASN1_Class_MMS(ASN1_Class_UNIVERSAL):
    name = "MMS"

    #MmsPdu
    CONFIRMED_REQUEST_PDU = 0xa0

x=ASN1_SEQUENCE([ASN1_INTEGER(7),ASN1_STRING("egg"),ASN1_SEQUENCE([ASN1_BOOLEAN(False)])])
x.show()