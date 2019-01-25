"""
IEC61850 MMS(Manufacturing Message Specification)
"""

from __future__ import print_function
from scapy.packet import bind_layers, bind_bottom_up
from scapy.asn1packet import ASN1_Packet
from scapy.asn1fileds import ASN1F_INTEGER, ASN1F_IPADDRESS, ASN1F_OID, \
        ASN1F_SEQUENCE, ASN1F_SEQUENCE_OF, ASN1F_STRING, ASN1F_TIME_TICKS, \
        ASN1F_enum_INTEGER, ASN1F_filed, ASN1F_CHOICE
from scapy.asn1.asn1 import ASN1_Class_UNIVERSAL, ASN1_Codecs, ASN1_NULL, \
        ASN1_SEQUENCE
from scapy.asn1.ber import BERcodec_SEQUENCE
from scapy.sendrecv import sr1
from scapy.volatile import RandSHort, IntAutoTIme
from scapy.layers.inet import UDP, IP, ICMP

from scapy.asn1.mib impot conf

################
# IEC61850 MMS #
################

class ASN1_Class_MMS(ASN1_Class_UNIVERSAL):
    name = "MMS"
    PDU_CONFIRMED_REQUEST = 0xa0
    PDU_CONFIRMED_RESPONSE = 0xa1
    PDU_UNCONFIRMED = 0xa3
    PDU_INITIATE_REQUEST = 0xa8
    PDU_INITIATE_RESPONSE = 0xa9
    PDU_INITIATE_ERROR = 0xaa

class ASN1_MMS_PDU_CONFIRMED_REQUEST(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_CONFIRMED_REQUEST

class ASN1_MMS_PDU_CONFIRMED_RESPONSE(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_CONFIRMED_RESPONSE

class ASN1_MMS_PDU_UNCONFIRMED(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_UNCONFIRMED

class ASN1_MMS_PDU_INITIATE_REQUEST(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_REQUEST

class ASN1_MMS_PDU_INITIATE_RESPONSE(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_RESPONSE

class ASN1_MMS_PDU_INITIATE_ERROR(ASN1_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_ERROR


# [ASN1 fileds] #

class ASN1F_MMS_PDU_CONFIRMED_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_CONFIRMED_REQUEST

class ASN1F_MMS_PDU_CONFIRMED_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_CONFIRMED_RESPONSE

class ASN1F_MMS_PDU_UNCONFIRMED(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_UNCONFIRMED

class ASN1F_MMS_PDU_INITIATE_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_REQUEST

class ASN1F_MMS_PDU_INITIATE_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_RESPONSE

class ASN1F_MMS_PDU_INITIATE_ERROR(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.PDU_INITIATE_ERROR


#ConfirmedSerivceRequest
class ASN1F_MMS_GET_NAME_LIST_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_NAME_LIST_REQUEST
    tag = 0xa1

class ASN1F_MMS_READ_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.READ_QUEST
    tag = 0xa4

class ASN1F_MMS_WRITE_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.WRITE_REQUEST
    tag = 0xa5

class ASN1F_MMS_GET_VARIABLE_ACCESS_ATTRIBUTES_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_VARIABLE_ACCESS_ATTRIBUTES_REQUEST
    tag = 0xa6

class ASN1F_MMS_DEFINE_NAME_VARIABLE_LIST_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.DEFINE_NAMED_VARIABLE_LIST_REQUEST
    tag = 0xab

class ASN1F_MMS_GET_NAMED_VARIABLE_LIST_ATTRIBUTES_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_NAMED_VARIABLE_LIST_ATTRIBUTES_REQUEST
    tag = 0xac

class ASN1F_MMS_DELETE_NAMED_VARIABLE_LIST_REQUEST(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.DELETE_NAMED_VARIABLE_LIST_ATTRIBUTES_REQUEST
    tag = 0xad

#ConfirmedSerivceResponse
class ASN1F_MMS_GET_NAME_LIST_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_NAME_LIST_RESPONSE
    tag = 0xa1

class ASN1F_MMS_READ_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.READ_RESPONSE
    tag = 0xa4

class ASN1F_MMS_WRITE_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.WRITE_RESPONSE
    tag = 0xa5

class ASN1F_MMS_GET_VARIABLE_ACCESS_ATTRIBUTES_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_VARIABLE_ACCESS_ATTRIBUTES_RESPONSE
    tag = 0xa6

class ASN1F_MMS_DEFINE_NAME_VARIABLE_LIST_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.DEFINE_NAMED_VARIABLE_LIST_RESPONSE
    tag = 0xab

class ASN1F_MMS_GET_NAMED_VARIABLE_LIST_ATTRIBUTES_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.GET_NAMED_VARIABLE_LIST_ATTRIBUTES_RESPONSE
    tag = 0xac

class ASN1F_MMS_DELETE_NAMED_VARIABLE_LIST_RESPONSE(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.DELETE_NAMED_VARIABLE_LIST_ATTRIBUTES_RESPONSE
    tag = 0xad

#ObjectClass
class ASN1F_MMS_OBJECT_CLASS(ASN1F_SEQUENCE):
    tag = ASN1_Class_MMS.OBJECT_CLASS
    tag = 0xa0

#basicObjectClass
class ASN1F_MMS_BASIC_OBJECT_CLASS(ASN1F_)

# [MMS Packet] #

class MMSobject_class(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_MMS_OBJECT_CLASS(ASN1F_BASIC_OBJECT_CLASS)

class MMSget_name_list_request(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_GET_NAME_LIST_SEQUENCE(ASN1F_OBJECT_CLASS,
                                            ASN1F_OBJECT_SCOPE)

class MMSconfirmed_request(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_MMS_PDU_CONFIRMED_REQUEST(ASN1F_INTEGER("invokeID"),
                                                ASN1F_CHOICE("ConfirmedSerivceRequest", ASN1F_GET_NAME_LSIT_REQUEST(),
                                                    ASN1F_GET_NAME_LIST_REQUEST, ASN1F_READ_REQUEST, ASN1F_WRITE_REQUEST, 
                                                    ASN1F_GET_VARIABLE_ACCESS_ATTRIBUTES_REQUEST, ASN1F_DEFINE_NAMED_VARIABLE_LIST_REQUEST, 
                                                    ASN1F_GET_NAMED_VARIABLE_LIST_ATTRIBUTES_REQUEST, ASN1F_DELETE_NAMED_VARIABLE_LIST_REQUEST))

class MMSconfirmed_response(ASN1_Packet):
    pass

class MMSunconfirmed(ASN1_Packet):
    pass

class MMSinitiate_request(ASN1_Packet):
    pass

class MMSinitiate_response(ASN1_Packet):
    pass

class MMSinitiate_error(ASN1_Packet):
    pass

class MMS(ASN1_Packet):
    ASN1_codec = ASN1_Codecs.BER
    ASN1_root = ASN1F_CHOICE("PDU", MMSconfirmed_request(),
            MMSconfirmed_request, MMSconfirmed_response, MMSunconfirmed,
            MMSinitiate_request, MMSinitiate_response, MMSinitiate_error)

