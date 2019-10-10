import hashlib
import time

DISTRIBUTION_NAME = 'sawtooth-healthcare'

DEFAULT_URL = 'http://127.0.0.1:8008'

TP_FAMILYNAME = 'healthcare'
TP_VERSION = '1.0'
# CLINIC_ENTITY_NAME = 'clinic'
# DOCTOR_ENTITY_NAME = 'doctor'
# PATIENT_ENTITY_NAME = 'patient'
# CLAIM_ENTITY_NAME = 'claim'
# EVENT_ENTITY_NAME = 'event'
# LAB_TEST_ENTITY_NAME = 'lab_test'
# PULSE_ENTITY_NAME = 'pulse'
#
# CLAIM_ENTITY_HEX6 = hashlib.sha512(CLAIM_ENTITY_NAME.encode("utf-8")).hexdigest()[0:6]
# CLINIC_ENTITY_HEX64 = hashlib.sha512(CLINIC_ENTITY_NAME.encode("utf-8")).hexdigest()[0:64]

CLINIC_ENTITY_CODE = '01'
DOCTOR_ENTITY_CODE = '02'
PATIENT_ENTITY_CODE = '03'
CLAIM_ENTITY_CODE = '04'
EVENT_ENTITY_CODE = '05'
LAB_TEST_ENTITY_CODE = '06'
PULSE_ENTITY_CODE = '07'
LAB_ENTITY_CODE = '08'

PATIENT_LAB_TEST__RELATION_CODE = "51"
LAB_TEST_PATIENT__RELATION_CODE = "52"

PATIENT_PULSE__RELATION_CODE = "61"
PULSE_PATIENT__RELATION_CODE = "62"

PATIENT_CLAIM__RELATION_CODE = "71"
CLAIM_PATIENT__RELATION_CODE = "72"

CLINIC_CLAIM__RELATION_CODE = "81"
CLAIM_CLINIC__RELATION_CODE = "82"
# permissions = {
#     'read_clinic': '100',
#     'read_own_clinic': '101',
#     'write_own_clinic': '102',
#
#     'read_doctor': '200',
#     'read_own_doctor': '201',
#     'write_own_doctor': '202',
#
#     'read_patient': '300',
#     'read_own_patient': '301',
#     'write_own_patient': '302',
#
#     'read_lab': '800',
#     'read_own_lab': '801',
#     'write_own_lab': '802',
#
#     'read_lab_test': '600',
#     'read_own_lab_test': '601',
#     'write_lab_test': '602',
#
#     'read_pulse': '700',
#     'read_own_pulse': '701',
#     'write_own_pulse': '702',
#
#     'read_claim': '400',
#     'read_own_claim': '401',
#     'write_own_claim': '402'
# }

# roles = {'clinic': {
#     permissions['read_clinic'],
#     permissions['read_own_clinic']
# },
#     'patient': {
#         permissions['read_own_patient'],
#         permissions['read_own_lab_test'],
#         permissions['read_own_pulse'],
#         permissions['read_own_claim']
#     },
#     'doctor': {
#         permissions['read_own_doctor'],
#         permissions['read_lab'],
#         permissions['read_lab_test'],
#         permissions['read_claim']
#     },
#     'lab': {
#         permissions['read_own_lab'],
#         permissions['read_lab_test'],
#         permissions['write_lab_test']
#     }
# }


def _hash(identifier):
    return hashlib.sha512(identifier.encode('utf-8')).hexdigest()


TP_PREFFIX_HEX6 = _hash(TP_FAMILYNAME)[0:6]


def make_clinic_address(clinic_pkey):
    return TP_PREFFIX_HEX6 + CLINIC_ENTITY_CODE + _hash(clinic_pkey)[:62]


def make_clinic_list_address():
    return TP_PREFFIX_HEX6 + CLINIC_ENTITY_CODE


def make_doctor_address(doctor_pkey):
    return TP_PREFFIX_HEX6 + DOCTOR_ENTITY_CODE + _hash(doctor_pkey)[:62]


def make_doctor_list_address():
    return TP_PREFFIX_HEX6 + DOCTOR_ENTITY_CODE


def make_patient_address(patient_pkey):
    return TP_PREFFIX_HEX6 + PATIENT_ENTITY_CODE + _hash(patient_pkey)[:62]


def make_patient_list_address():
    return TP_PREFFIX_HEX6 + PATIENT_ENTITY_CODE


def make_lab_address(lab_pkey):
    return TP_PREFFIX_HEX6 + LAB_ENTITY_CODE + _hash(lab_pkey)[:62]


def make_lab_list_address():
    return TP_PREFFIX_HEX6 + LAB_ENTITY_CODE


# def make_claim_address(claim_id, clinic_pkey):
#     return TP_PREFFIX_HEX6 + CLAIM_ENTITY_CODE + _hash(claim_id)[:16] + \
#            CLINIC_ENTITY_CODE + _hash(clinic_pkey)[:44]
#
#
# def make_claim_list_address():
#     return TP_PREFFIX_HEX6 + CLAIM_ENTITY_CODE


# Claim entity
def make_claim_address(claim_id):
    return TP_PREFFIX_HEX6 + CLAIM_ENTITY_CODE + _hash(claim_id)[:62]


def make_claim_list_address():
    return TP_PREFFIX_HEX6 + CLAIM_ENTITY_CODE


# Claim <-> Patient relation
def make_claim_patient__relation_address(claim_id, client_pkey):
    return TP_PREFFIX_HEX6 + CLAIM_PATIENT__RELATION_CODE + \
        CLAIM_ENTITY_CODE + _hash(claim_id)[:30] + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:28]


def make_patient_list_by_claim_address(claim_id):
    return TP_PREFFIX_HEX6 + CLAIM_PATIENT__RELATION_CODE + CLAIM_ENTITY_CODE + _hash(claim_id)[:30]


# Patient <-> Claim relation
def make_patient_claim__relation_address(client_pkey, claim_id):
    return TP_PREFFIX_HEX6 + PATIENT_CLAIM__RELATION_CODE + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:30] + \
        CLAIM_ENTITY_CODE + _hash(claim_id)[:28]


def make_claim_list_by_patient_address(client_pkey):
    return TP_PREFFIX_HEX6 + PATIENT_CLAIM__RELATION_CODE + PATIENT_ENTITY_CODE + _hash(client_pkey)[:30]


# Claim <-> Clinic relation
def make_claim_clinic__relation_address(claim_id, client_pkey):
    return TP_PREFFIX_HEX6 + CLAIM_CLINIC__RELATION_CODE + \
        CLAIM_ENTITY_CODE + _hash(claim_id)[:30] + \
        CLINIC_ENTITY_CODE + _hash(client_pkey)[:28]


def make_clinic_list_by_claim_address(claim_id):
    return TP_PREFFIX_HEX6 + CLAIM_CLINIC__RELATION_CODE + CLAIM_ENTITY_CODE + _hash(claim_id)[:30]


# Clinic <-> Claim relation
def make_clinic_claim__relation_address(client_pkey, claim_id):
    return TP_PREFFIX_HEX6 + CLINIC_CLAIM__RELATION_CODE + \
        CLINIC_ENTITY_CODE + _hash(client_pkey)[:30] + \
        CLAIM_ENTITY_CODE + _hash(claim_id)[:28]


def make_claim_list_by_clinic_address(client_pkey):
    return TP_PREFFIX_HEX6 + CLINIC_CLAIM__RELATION_CODE + CLINIC_ENTITY_CODE + _hash(client_pkey)[:30]


def make_event_address(claim_id, clinic_pkey, event_time):
    return TP_PREFFIX_HEX6 + EVENT_ENTITY_CODE + _hash(claim_id)[:12] + \
           CLINIC_ENTITY_CODE + _hash(clinic_pkey)[:10] + \
           _hash(event_time)[:38]


def make_event_list_address(claim_id, clinic_pkey):
    return TP_PREFFIX_HEX6 + EVENT_ENTITY_CODE + _hash(claim_id)[:12] + \
           CLINIC_ENTITY_CODE + _hash(clinic_pkey)[:10]


# Lab Test entity
def make_lab_test_address(lab_test_id):
    return TP_PREFFIX_HEX6 + LAB_TEST_ENTITY_CODE + _hash(lab_test_id)[:62]


def make_lab_test_list_address():
    return TP_PREFFIX_HEX6 + LAB_TEST_ENTITY_CODE


# Lab Test <-> Patient relation
def make_lab_test_patient__relation_address(lab_test_id, client_pkey):
    return TP_PREFFIX_HEX6 + LAB_TEST_PATIENT__RELATION_CODE + \
        LAB_TEST_ENTITY_CODE + _hash(lab_test_id)[:30] + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:28]


def make_patient_list_by_lab_test_address(lab_test_id):
    return TP_PREFFIX_HEX6 + LAB_TEST_PATIENT__RELATION_CODE + LAB_TEST_ENTITY_CODE + _hash(lab_test_id)[:30]


# Patient <-> Lab Test relation
def make_patient_lab_test__relation_address(client_pkey, lab_test_id):
    return TP_PREFFIX_HEX6 + PATIENT_LAB_TEST__RELATION_CODE + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:30] + \
        LAB_TEST_ENTITY_CODE + _hash(lab_test_id)[:28]


def make_lab_test_list_by_patient_address(client_pkey):
    return TP_PREFFIX_HEX6 + PATIENT_LAB_TEST__RELATION_CODE + PATIENT_ENTITY_CODE + _hash(client_pkey)[:30]


# Pulse entity
def make_pulse_address(pulse_id):
    return TP_PREFFIX_HEX6 + PULSE_ENTITY_CODE + _hash(pulse_id)[:62]

# def make_pulse_address(public_key, timestamp):
#     return TP_PREFFIX_HEX6 + PULSE_ENTITY_CODE + _hash(public_key)[:12] + \
#            _hash(str(timestamp))[:50]


def make_pulse_list_address():
    return TP_PREFFIX_HEX6 + PULSE_ENTITY_CODE


# Pulse <-> Patient relation
def make_pulse_patient__relation_address(pulse_id, client_pkey):
    return TP_PREFFIX_HEX6 + PULSE_PATIENT__RELATION_CODE + \
        PULSE_ENTITY_CODE + _hash(pulse_id)[:30] + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:28]


def make_patient_list_by_pulse_address(pulse_id):
    return TP_PREFFIX_HEX6 + PULSE_PATIENT__RELATION_CODE + PULSE_ENTITY_CODE + _hash(pulse_id)[:30]


# Patient <-> Pulse relation
def make_patient_pulse__relation_address(client_pkey, pulse_id):
    return TP_PREFFIX_HEX6 + PATIENT_PULSE__RELATION_CODE + \
        PATIENT_ENTITY_CODE + _hash(client_pkey)[:30] + \
        PULSE_ENTITY_CODE + _hash(pulse_id)[:28]


def make_pulse_list_by_patient_address(client_pkey):
    return TP_PREFFIX_HEX6 + PATIENT_PULSE__RELATION_CODE + PATIENT_ENTITY_CODE + _hash(client_pkey)[:30]


def get_current_timestamp():
    return int(round(time.time() * 1000))


# def get_signer(request, client_key):
#     if request.app.config.SIGNER_CLINIC.get_public_key().as_hex() == client_key:
#         client_signer = request.app.config.SIGNER_CLINIC
#     elif request.app.config.SIGNER_PATIENT.get_public_key().as_hex() == client_key:
#         client_signer = request.app.config.SIGNER_PATIENT
#     elif request.app.config.SIGNER_DOCTOR.get_public_key().as_hex() == client_key:
#         client_signer = request.app.config.SIGNER_DOCTOR
#     elif request.app.config.SIGNER_LAB.get_public_key().as_hex() == client_key:
#         client_signer = request.app.config.SIGNER_LAB
#     else:
#         client_signer = request.app.config.SIGNER_PATIENT
#     return client_signer
