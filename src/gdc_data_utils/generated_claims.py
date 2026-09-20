"""Generated from exported gdc-common-utils-ts *Claim objects; do not edit."""

class AllergyIntoleranceClaim:
    """FHIR-like flat claims generated from TypeScript ``AllergyIntoleranceClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/allergyintolerance.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-AllergyIntolerance.html
    """

    IDENTIFIER = 'AllergyIntolerance.identifier'
    SUBJECT = 'AllergyIntolerance.subject'
    PATIENT = 'AllergyIntolerance.patient'
    CODE = 'AllergyIntolerance.code'
    CODE_TEXT = 'AllergyIntolerance.code-text'
    CODE_TEXT_LOCAL = 'AllergyIntolerance.code-text'
    CODE_DISPLAY = 'AllergyIntolerance.code-display'
    CLINICAL_STATUS = 'AllergyIntolerance.clinical-status'
    VERIFICATION_STATUS = 'AllergyIntolerance.verification-status'
    CATEGORY = 'AllergyIntolerance.category'
    CONTAINED_REFERENCE_LIST = 'AllergyIntolerance.contained-reference-list'
    CONTAINED_RESOURCE_LIST = 'AllergyIntolerance.contained-resource-list'
    CONTAINED_DOCUMENTS = 'AllergyIntolerance.contained-documents'
    ATTACHMENT_CONTENT_IDS = 'AllergyIntolerance.attachment-content-ids'
    CRITICALITY = 'AllergyIntolerance.criticality'
    ASSERTER = 'AllergyIntolerance.asserter'
    RECORDED_DATE = 'AllergyIntolerance.date'
    LAST_OCCURRENCE = 'AllergyIntolerance.last-date'
    MANIFESTATION = 'AllergyIntolerance.manifestation'
    ONSET = 'AllergyIntolerance.onset'
    ROUTE = 'AllergyIntolerance.route'
    SEVERITY = 'AllergyIntolerance.severity'
    TYPE = 'AllergyIntolerance.type'
    ONSET_DATE_TIME = 'AllergyIntolerance.onset-datetime'
    RECORDER = 'AllergyIntolerance.recorder'

class AppointmentClaim:
    """FHIR-like flat claims generated from TypeScript ``AppointmentClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/appointment.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Appointment.html
    """

    IDENTIFIER = 'Appointment.identifier'
    STATUS = 'Appointment.status'
    SERVICE_CATEGORY = 'Appointment.service-category'
    SERVICE_TYPE = 'Appointment.service-type'
    SPECIALTY = 'Appointment.specialty'
    APPOINTMENT_TYPE = 'Appointment.appointment-type'
    REASON_CODE = 'Appointment.reason-code'
    REASON_REFERENCE = 'Appointment.reason-reference'
    DESCRIPTION = 'Appointment.description'
    START = 'Appointment.start'
    END = 'Appointment.end'
    MINUTES_DURATION = 'Appointment.minutes-duration'
    CREATED = 'Appointment.created'
    NOTE_TEXT = 'Appointment.note-text'
    PATIENT_INSTRUCTION = 'Appointment.patient-instruction'
    BASED_ON = 'Appointment.based-on'
    PARTICIPANT_ACTOR = 'Appointment.actor'
    PARTICIPANT_STATUS = 'Appointment.part-status'
    PARTICIPANT_TYPE = 'Appointment.participant-type'

class AppointmentResponseClaim:
    """FHIR-like flat claims generated from TypeScript ``AppointmentResponseClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/appointmentresponse.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-AppointmentResponse.html
    """

    ACTOR = 'AppointmentResponse.actor'
    APPOINTMENT = 'AppointmentResponse.appointment'
    COMMENT = 'AppointmentResponse.comment'
    IDENTIFIER = 'AppointmentResponse.identifier'
    START = 'AppointmentResponse.start'
    END = 'AppointmentResponse.end'
    PARTICIPANT_TYPE = 'AppointmentResponse.participant-type'
    PARTICIPANT_STATUS = 'AppointmentResponse.participant-status'
    PATIENT = 'AppointmentResponse.patient'
    PRACTITIONER = 'AppointmentResponse.practitioner'
    LOCATION = 'AppointmentResponse.location'

class CarePlanClaim:
    """FHIR-like flat claims generated from TypeScript ``CarePlanClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/careplan.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-CarePlan.html
    """

    ACTIVITY_CODE = 'CarePlan.activity-code'
    ACTIVITY_DATE = 'CarePlan.activity-date'
    ACTIVITY_REFERENCE = 'CarePlan.activity-reference'
    BASED_ON = 'CarePlan.based-on'
    CARE_TEAM = 'CarePlan.care-team'
    CATEGORY = 'CarePlan.category'
    CATEGORY_TEXT = 'CarePlan.category-text'
    CATEGORY_DISPLAY = 'CarePlan.category-display'
    CONDITION = 'CarePlan.condition'
    DATE = 'CarePlan.date'
    ENCOUNTER = 'CarePlan.encounter'
    GOAL = 'CarePlan.goal'
    IDENTIFIER = 'CarePlan.identifier'
    INTENT = 'CarePlan.intent'
    PART_OF = 'CarePlan.part-of'
    PATIENT = 'CarePlan.patient'
    PERFORMER = 'CarePlan.performer'
    REPLACES = 'CarePlan.replaces'
    STATUS = 'CarePlan.status'
    SUBJECT = 'CarePlan.subject'
    NOTE = 'CarePlan.note'
    DESCRIPTION = 'CarePlan.description'
    PERIOD_START = 'CarePlan.period-start'
    PERIOD_END = 'CarePlan.period-end'
    ACTIVITY_STATUS = 'CarePlan.activity-status'
    ACTIVITY_STATUS_REASON = 'CarePlan.activity-status-reason'
    ACTIVITY_DO_NOT_PERFORM = 'CarePlan.activity-do-not-perform'
    ACTIVITY_OUTCOME = 'CarePlan.activity-outcome'
    ACTIVITY_LOCATION_DISPLAY = 'CarePlan.activity-location-display'
    ACTIVITY_TIMING_FREQUENCY = 'CarePlan.activity-timing-frequency'
    ACTIVITY_TIMING_PERIOD = 'CarePlan.activity-timing-period'
    ACTIVITY_TIMING_PERIOD_UNIT = 'CarePlan.activity-timing-period-unit'

class ChargeItemClaim:
    """FHIR-like flat claims generated from TypeScript ``ChargeItemClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/chargeitem.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-ChargeItem.html
    """

    IDENTIFIER = 'ChargeItem.identifier'
    STATUS = 'ChargeItem.status'
    PART_OF = 'ChargeItem.part-of'
    SUBJECT = 'ChargeItem.subject'
    OCCURRENCE = 'ChargeItem.occurrence'
    SUPPORTING_INFORMATION = 'ChargeItem.supporting-information'
    CODE = 'ChargeItem.code'
    CODE_TEXT = 'ChargeItem.code-text'
    CATEGORY = 'ChargeItem.category'
    SUPPLIER_PRODUCT_CODE = 'ChargeItem.supplier-productcode'
    QUANTITY = 'ChargeItem.quantity'
    QUANTITY_NUMBER = 'ChargeItem.quantity-number'
    QUANTITY_UNIT = 'ChargeItem.quantity-unit'
    ITEMS_PER_UNIT = 'ChargeItem.items-per-unit'
    ITEMS_QUANTITY = 'ChargeItem.items-quantity'
    ITEMS_QUANTITY_NUMBER = 'ChargeItem.items-quantity-number'
    ITEMS_QUANTITY_UNIT = 'ChargeItem.items-quantity-unit'

class ClinicalImpressionClaim:
    """FHIR-like flat claims generated from TypeScript ``ClinicalImpressionClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/clinicalimpression.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-ClinicalImpression.html
    """

    IDENTIFIER = 'ClinicalImpression.identifier'
    STATUS = 'ClinicalImpression.status'
    DESCRIPTION = 'ClinicalImpression.description'
    SUBJECT = 'ClinicalImpression.subject'
    ENCOUNTER = 'ClinicalImpression.encounter'
    EFFECTIVE_DATE_TIME = 'ClinicalImpression.effective-datetime'
    DATE = 'ClinicalImpression.date'
    ASSESSOR = 'ClinicalImpression.assessor'
    PROBLEM = 'ClinicalImpression.problem'
    FINDING = 'ClinicalImpression.finding'
    PROGNOSIS_CODE = 'ClinicalImpression.prognosis-code'
    SUMMARY = 'ClinicalImpression.summary'

class CommunicationClaim:
    """FHIR-like flat claims generated from TypeScript ``CommunicationClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/communication.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Communication.html
    """

    CATEGORY = 'Communication.category'
    STATUS = 'Communication.status'
    IDENTIFIER = 'Communication.identifier'
    SUBJECT = 'Communication.subject'
    RECIPIENT = 'Communication.recipient'
    SENDER = 'Communication.sender'
    SENT = 'Communication.sent'
    NOTE_TEXT = 'Communication.note-text'
    TOPIC = 'Communication.topic'
    TEXT = 'Communication.text'
    CONTENT_REFERENCE = 'Communication.content-reference'
    CONTENT_CODE = 'Communication.content-code'
    CONTENT_ATTACHMENT_DATA = 'Communication.content-attachment-data'
    CONTENT_ATTACHMENT_TYPE = 'Communication.content-attachment-type'
    CONTENT_ATTACHMENT_TITLE = 'Communication.content-attachment-title'
    CONTENT_ATTACHMENT_URL = 'Communication.content-attachment-url'
    PART_OF = 'Communication.part-of'

class CompositionClaim:
    """FHIR-like flat claims generated from TypeScript ``CompositionClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/composition.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Composition.html
    """

    SUBJECT = 'Composition.subject'
    SECTION = 'Composition.section'
    AUTHOR = 'Composition.author'
    ATTESTER = 'Composition.attester'
    ATTESTER_MODE = 'Composition.attester-mode'
    ATTESTER_TIME = 'Composition.attester-time'
    CUSTODIAN = 'Composition.custodian'
    DATE = 'Composition.date'
    ENTRY = 'Composition.entry'
    TYPE = 'Composition.type'
    IDENTIFIER = 'Composition.identifier'
    TITLE = 'Composition.title'

class ConditionClaim:
    """FHIR-like flat claims generated from TypeScript ``ConditionClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/condition.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Condition.html
    """

    IDENTIFIER = 'Condition.identifier'
    SUBJECT = 'Condition.subject'
    CLINICAL_STATUS = 'Condition.clinical-status'
    VERIFICATION_STATUS = 'Condition.verification-status'
    CATEGORY = 'Condition.category'
    CODE = 'Condition.code'
    CODE_TEXT = 'Condition.code-text'
    CODE_TEXT_LOCAL = 'Condition.code-text'
    CODE_DISPLAY = 'Condition.code-display'
    CONTAINED_REFERENCE_LIST = 'Condition.contained-reference-list'
    CONTAINED_RESOURCE_LIST = 'Condition.contained-resource-list'
    CONTAINED_DOCUMENTS = 'Condition.contained-documents'
    ATTACHMENT_CONTENT_IDS = 'Condition.attachment-content-ids'
    SEVERITY = 'Condition.severity'
    ONSET_DATE_TIME = 'Condition.onset-datetime'
    RECORDED_DATE = 'Condition.recorded-date'
    ASSERTER = 'Condition.asserter'
    RECORDER = 'Condition.recorder'

class CoverageClaim:
    """FHIR-like flat claims generated from TypeScript ``CoverageClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/coverage.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Coverage.html
    """

    IDENTIFIER = 'Coverage.identifier'
    STATUS = 'Coverage.status'
    TYPE = 'Coverage.type'
    POLICY_HOLDER = 'Coverage.policy-holder'
    SUBSCRIBER = 'Coverage.subscriber'
    BENEFICIARY = 'Coverage.beneficiary'
    RELATIONSHIP = 'Coverage.relationship'
    PERIOD_START = 'Coverage.period-start'
    PERIOD_END = 'Coverage.period-end'
    PAYOR = 'Coverage.payor'
    CLASS = 'Coverage.class'

class DeviceClaim:
    """FHIR-like flat claims generated from TypeScript ``DeviceClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/device.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Device.html
    """

    DEVICE_NAME = 'Device.device-name'
    IDENTIFIER = 'Device.identifier'
    LOCATION = 'Device.location'
    MANUFACTURER = 'Device.manufacturer'
    MODEL = 'Device.model'
    ORGANIZATION = 'Device.organization'
    PATIENT = 'Device.patient'
    SERIAL_NUMBER = 'Device.serial-number'
    STATUS = 'Device.status'
    TYPE = 'Device.type'
    TYPE_TEXT = 'Device.type-text'
    TYPE_DISPLAY = 'Device.type-display'
    UDI_CARRIER = 'Device.udi-carrier'
    URL = 'Device.url'
    NOTE = 'Device.note'

class DeviceUseStatementClaim:
    """FHIR-like flat claims generated from TypeScript ``DeviceUseStatementClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/deviceusestatement.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-DeviceUseStatement.html
    """

    IDENTIFIER = 'DeviceUseStatement.identifier'
    SUBJECT = 'DeviceUseStatement.subject'
    STATUS = 'DeviceUseStatement.status'
    DEVICE = 'DeviceUseStatement.device'
    DEVICE_DISPLAY = 'DeviceUseStatement.device-display'
    RECORDED_ON = 'DeviceUseStatement.recorded-on'
    TIMING_DATE_TIME = 'DeviceUseStatement.timing-datetime'
    TIMING_ABSENT_REASON = 'DeviceUseStatement.timing-absent-reason'
    REASON_CODE = 'DeviceUseStatement.reason-code'
    SOURCE = 'DeviceUseStatement.source'

class DiagnosticReportClaim:
    """FHIR-like flat claims generated from TypeScript ``DiagnosticReportClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/diagnosticreport.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-DiagnosticReport.html
    """

    BASED_ON = 'DiagnosticReport.based-on'
    CATEGORY = 'DiagnosticReport.category'
    CODE = 'DiagnosticReport.code'
    CODE_TEXT = 'DiagnosticReport.code-text'
    CODE_TEXT_LOCAL = 'DiagnosticReport.code-text'
    CODE_DISPLAY = 'DiagnosticReport.code-display'
    DATE = 'DiagnosticReport.date'
    ENCOUNTER = 'DiagnosticReport.encounter'
    IDENTIFIER = 'DiagnosticReport.identifier'
    MEDIA = 'DiagnosticReport.media'
    PATIENT = 'DiagnosticReport.patient'
    PERFORMER = 'DiagnosticReport.performer'
    RESULT = 'DiagnosticReport.result'
    RESULTS_INTERPRETER = 'DiagnosticReport.results-interpreter'
    SPECIMEN = 'DiagnosticReport.specimen'
    STATUS = 'DiagnosticReport.status'
    SUBJECT = 'DiagnosticReport.subject'
    PRESENTED_FORM_CONTENT_TYPE = 'DiagnosticReport.presented-form-contenttype'
    PRESENTED_FORM_DATA = 'DiagnosticReport.presented-form-data'
    PRESENTED_FORM_URL = 'DiagnosticReport.presented-form-url'
    CONTAINED_REFERENCE_LIST = 'DiagnosticReport.contained-reference-list'
    CONTAINED_RESOURCE_LIST = 'DiagnosticReport.contained-resource-list'
    CONTAINED_DOCUMENTS = 'DiagnosticReport.contained-documents'

class DocumentReferenceClaim:
    """FHIR-like flat claims generated from TypeScript ``DocumentReferenceClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/documentreference.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-DocumentReference.html
    """

    ATTESTER = 'DocumentReference.attester'
    AUTHOR = 'DocumentReference.author'
    BASED_ON = 'DocumentReference.based-on'
    CATEGORY = 'DocumentReference.category'
    CONTENT_DATA = 'DocumentReference.contentdata'
    CONTENT_HASH = 'DocumentReference.contenthash'
    CONTENT_TYPE = 'DocumentReference.contenttype'
    CONTEXT = 'DocumentReference.context'
    CREATION = 'DocumentReference.creation'
    DATE = 'DocumentReference.date'
    DESCRIPTION = 'DocumentReference.description'
    EVENT_CODE = 'DocumentReference.event-code'
    EVENT_REFERENCE = 'DocumentReference.event-reference'
    FORMAT_URI = 'DocumentReference.format-uri'
    IDENTIFIER = 'DocumentReference.identifier'
    LANGUAGE = 'DocumentReference.language'
    LOCATION = 'DocumentReference.location'
    MODALITY = 'DocumentReference.modality'
    RELATES_TO = 'DocumentReference.relatesto'
    RELATION = 'DocumentReference.relation'
    SUBJECT = 'DocumentReference.subject'
    TYPE = 'DocumentReference.type'
    TYPE_TEXT = 'DocumentReference.type-text'
    TYPE_DISPLAY = 'DocumentReference.type-display'
    USER_SELECTED = 'DocumentReference.user-selected'

class EncounterClaim:
    """FHIR-like flat claims generated from TypeScript ``EncounterClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/encounter.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Encounter.html
    """

    IDENTIFIER = 'Encounter.identifier'
    STATUS = 'Encounter.status'
    CLASS = 'Encounter.class'
    TYPE = 'Encounter.type'
    SUBJECT = 'Encounter.subject'
    PATIENT = 'Encounter.patient'
    PARTICIPANT = 'Encounter.participant'
    SERVICE_PROVIDER = 'Encounter.service-provider'
    PERIOD_START = 'Encounter.period-start'
    PERIOD_END = 'Encounter.period-end'
    REASON_CODE = 'Encounter.reason-code'
    DIAGNOSIS = 'Encounter.diagnosis'
    LOCATION = 'Encounter.location'

class FlagClaim:
    """FHIR-like flat claims generated from TypeScript ``FlagClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/flag.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Flag.html
    """

    AUTHOR = 'Flag.author'
    DATE = 'Flag.date'
    ENCOUNTER = 'Flag.encounter'
    IDENTIFIER = 'Flag.identifier'
    PATIENT = 'Flag.patient'
    SUBJECT = 'Flag.subject'
    STATUS = 'Flag.status'
    CATEGORY = 'Flag.category'
    CODE = 'Flag.code'
    CODE_TEXT = 'Flag.code-text'
    CODE_TEXT_LOCAL = 'Flag.code-text'
    CODE_DISPLAY = 'Flag.code-display'
    PERIOD_START = 'Flag.period-start'
    PERIOD_END = 'Flag.period-end'
    DETAIL = 'Flag.flag-detail'
    PRIORITY = 'Flag.flag-priority'

class ImmunizationClaim:
    """FHIR-like flat claims generated from TypeScript ``ImmunizationClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/immunization.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Immunization.html
    """

    DATE = 'Immunization.date'
    IDENTIFIER = 'Immunization.identifier'
    LOCATION = 'Immunization.location'
    LOT_NUMBER = 'Immunization.lot-number'
    MANUFACTURER = 'Immunization.manufacturer'
    PATIENT = 'Immunization.patient'
    PERFORMER = 'Immunization.performer'
    REACTION_DATE = 'Immunization.reaction-date'
    REASON_CODE = 'Immunization.reason-code'
    REASON_REFERENCE = 'Immunization.reason-reference'
    SERIES = 'Immunization.series'
    STATUS = 'Immunization.status'
    STATUS_REASON = 'Immunization.status-reason'
    TARGET_DISEASE = 'Immunization.target-disease'
    VACCINE_CODE = 'Immunization.vaccine-code'
    VACCINE_CODE_TEXT = 'Immunization.vaccine-code-text'
    VACCINE_CODE_DISPLAY = 'Immunization.vaccine-code-display'
    DOSE_SEQUENCE = 'Immunization.dose-sequence'
    SUBJECT = 'Immunization.subject'
    NOTE = 'Immunization.note'
    ROUTE = 'Immunization.route'
    ROUTE_DISPLAY = 'Immunization.route-display'
    SITE = 'Immunization.site'
    SITE_DISPLAY = 'Immunization.site-display'

class InvoiceClaim:
    """FHIR-like flat claims generated from TypeScript ``InvoiceClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/invoice.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Invoice.html
    """

    IDENTIFIER = 'Invoice.identifier'
    DATE = 'Invoice.date'
    STATUS = 'Invoice.status'
    SUBJECT = 'Invoice.subject'
    RECIPIENT = 'Invoice.recipient'
    ISSUER = 'Invoice.issuer'
    ISSUER_DISPLAY = 'Invoice.issuer-display'
    PAYMENT_TERMS = 'Invoice.payment-terms'
    PAYMENT_URL = 'Invoice.payment-url'
    TOTAL_NET_VALUE = 'Invoice.totalnet-value'
    TOTAL_NET_CURRENCY = 'Invoice.totalnet-currency'
    TOTAL_GROSS_VALUE = 'Invoice.totalgross-value'
    TOTAL_GROSS_CURRENCY = 'Invoice.totalgross-currency'

class LocationClaim:
    """FHIR-like flat claims generated from TypeScript ``LocationClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/location.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Location.html
    """

    IDENTIFIER = 'Location.identifier'
    STATUS = 'Location.status'
    NAME = 'Location.name'
    DESCRIPTION = 'Location.description'
    TYPE = 'Location.type'
    MODE = 'Location.mode'
    TELECOM = 'Location.telecom'
    ADDRESS = 'Location.address'
    PHYSICAL_TYPE = 'Location.physical-type'
    MANAGING_ORGANIZATION = 'Location.managing-organization'
    PART_OF = 'Location.part-of'

class MedicationStatementClaim:
    """FHIR-like flat claims generated from TypeScript ``MedicationStatementClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/medicationstatement.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-MedicationStatement.html
    """

    IDENTIFIER = 'MedicationStatement.identifier'
    SUBJECT = 'MedicationStatement.subject'
    PATIENT = 'MedicationStatement.patient'
    STATUS = 'MedicationStatement.status'
    CATEGORY = 'MedicationStatement.category'
    EFFECTIVE = 'MedicationStatement.effective'
    EFFECTIVE_PERIOD_START = 'MedicationStatement.effective-period-start'
    EFFECTIVE_PERIOD_END = 'MedicationStatement.effective-period-end'
    CODE = 'MedicationStatement.code'
    CODE_TEXT = 'MedicationStatement.code-text'
    CODE_TEXT_LOCAL = 'MedicationStatement.code-text'
    CODE_DISPLAY = 'MedicationStatement.code-display'
    MEDICATION = 'MedicationStatement.medication'
    PART_OF = 'MedicationStatement.part-of'
    SOURCE = 'MedicationStatement.source'
    MEDICATION_TEXT = 'MedicationStatement.medication-text'
    ADHERENCE = 'MedicationStatement.adherence'
    ADHERENCE_TEXT = 'MedicationStatement.adherence-text'
    ADHERENCE_DISPLAY = 'MedicationStatement.adherence-display'
    USER_SELECTED = 'MedicationStatement.user-selected'
    NOTE = 'MedicationStatement.note'
    CONTAINED_REFERENCE_LIST = 'MedicationStatement.contained-reference-list'
    CONTAINED_RESOURCE_LIST = 'MedicationStatement.contained-resource-list'
    CONTAINED_DOCUMENTS = 'MedicationStatement.contained-documents'
    ATTACHMENT_CONTENT_IDS = 'MedicationStatement.attachment-content-ids'
    DOSAGE_INSTRUCTION = 'MedicationStatement.dosage-instruction'
    MEDICATION_IDENTIFIER = 'MedicationStatement.medication-identifier'
    MEDICATION_SERIAL_NUMBER = 'MedicationStatement.medication-serial-number'
    MEDICATION_EXPIRATION_DATE = 'MedicationStatement.medication-expiration-date'
    DOSE_QUANTITY_VALUE = 'MedicationStatement.dose-quantity-value'
    DOSE_QUANTITY_UNIT = 'MedicationStatement.dose-quantity-unit'
    DOSAGE_ROUTE = 'MedicationStatement.dosage-route'
    TIMING_FREQUENCY = 'MedicationStatement.timing-frequency'
    TIMING_PERIOD = 'MedicationStatement.timing-period'
    TIMING_PERIOD_UNIT = 'MedicationStatement.timing-period-unit'

class ObservationClaim:
    """FHIR-like flat claims generated from TypeScript ``ObservationClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/observation.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Observation.html
    """

    BASED_ON = 'Observation.based-on'
    CATEGORY = 'Observation.category'
    CODE_SYSTEM = 'Observation.code-system'
    CODE_VALUE = 'Observation.code-value'
    CODE_TEXT = 'Observation.code-text'
    CODE_TEXT_LOCAL = 'Observation.code-text'
    CODE_DISPLAY = 'Observation.code-display'
    CODE = 'Observation.code'
    DATE = 'Observation.date'
    DEVICE = 'Observation.device'
    ENCOUNTER = 'Observation.encounter'
    FOCUS = 'Observation.focus'
    HAS_MEMBER = 'Observation.has-member'
    COMPONENT_TAGS = 'Observation.component-tags'
    COMPONENT_CODE_VALUES = 'Observation.component-code-values'
    COMPONENT_NAMES = 'Observation.component-names'
    IDENTIFIER = 'Observation.identifier'
    LANGUAGE = 'Observation.language'
    METHOD = 'Observation.method'
    PATIENT = 'Observation.patient'
    PERFORMER = 'Observation.performer'
    SPECIMEN = 'Observation.specimen'
    STATUS = 'Observation.status'
    SUBJECT = 'Observation.subject'
    VALUE_CONCEPT = 'Observation.value-concept'
    VALUE_CONCEPT_SYSTEM = 'Observation.value-concept-system'
    VALUE_CONCEPT_VALUE = 'Observation.value-concept-value'
    VALUE_CONCEPT_TEXT = 'Observation.value-concept-text'
    VALUE_CONCEPT_DISPLAY = 'Observation.value-concept-display'
    VALUE_DATE = 'Observation.value-date'
    VALUE_QUANTITY_COMPARATOR = 'Observation.value-quantity-comparator'
    VALUE_QUANTITY_NUMBER = 'Observation.value-quantity-number'
    VALUE_QUANTITY_UNIT = 'Observation.value-quantity-unit'
    REFERENCE_RANGE_LOW_NUMBER = 'Observation.reference-range-low-number'
    REFERENCE_RANGE_HIGH_NUMBER = 'Observation.reference-range-high-number'
    REFERENCE_RANGE_UNIT = 'Observation.reference-range-unit'
    REFERENCE_RANGE_TEXT = 'Observation.reference-range-text'
    COMPONENT_CODE = 'Observation.component-code'
    COMPONENT_CODE_DISPLAY = 'Observation.component-code-display'
    COMPONENT_VALUE_QUANTITY_NUMBER = 'Observation.component-value-quantity-number'
    COMPONENT_VALUE_QUANTITY_UNIT = 'Observation.component-value-quantity-unit'
    SCORE_TOTAL_NUMBER = 'Observation.score-total-number'
    BLOOD_PRESSURE_SYSTOLIC_NUMBER = 'Observation.bp-systolic-number'
    BLOOD_PRESSURE_DIASTOLIC_NUMBER = 'Observation.bp-diastolic-number'
    VALUE_STRING = 'Observation.value-string'
    NOTE = 'Observation.note'
    EFFECTIVE_DATE_TIME = 'Observation.effective-datetime'

class OrganizationClaim:
    """FHIR-like flat claims generated from TypeScript ``OrganizationClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/organization.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Organization.html
    """

    IDENTIFIER = 'Organization.identifier'
    ACTIVE = 'Organization.active'
    TYPE = 'Organization.type'
    NAME = 'Organization.name'
    ALIAS = 'Organization.alias'
    PART_OF = 'Organization.part-of'
    TELECOM = 'Organization.telecom'
    ADDRESS = 'Organization.address'

class PractitionerRoleClaim:
    """FHIR-like flat claims generated from TypeScript ``PractitionerRoleClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/practitionerrole.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-PractitionerRole.html
    """

    IDENTIFIER = 'PractitionerRole.identifier'
    ACTIVE = 'PractitionerRole.active'
    PRACTITIONER = 'PractitionerRole.practitioner'
    ORGANIZATION = 'PractitionerRole.organization'
    LOCATION = 'PractitionerRole.location'
    SERVICE = 'PractitionerRole.service'
    SPECIALTY = 'PractitionerRole.specialty'
    PERIOD_START = 'PractitionerRole.period-start'
    PERIOD_END = 'PractitionerRole.period-end'
    CODE = 'PractitionerRole.code'
    CODE_TEXT = 'PractitionerRole.code-text'
    CODE_DISPLAY = 'PractitionerRole.code-display'

class ProcedureClaim:
    """FHIR-like flat claims generated from TypeScript ``ProcedureClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/procedure.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Procedure.html
    """

    BASED_ON = 'Procedure.based-on'
    BODY_SITE = 'Procedure.body-site'
    CODE = 'Procedure.code'
    CODE_TEXT = 'Procedure.code-text'
    CODE_DISPLAY = 'Procedure.code-display'
    DATE = 'Procedure.date'
    ENCOUNTER = 'Procedure.encounter'
    IDENTIFIER = 'Procedure.identifier'
    INSTANTIATES_CANONICAL = 'Procedure.instantiates-canonical'
    INSTANTIATES_URI = 'Procedure.instantiates-uri'
    LOCATION = 'Procedure.location'
    PART_OF = 'Procedure.part-of'
    PATIENT = 'Procedure.patient'
    PERFORMER = 'Procedure.performer'
    REASON_CODE = 'Procedure.reason-code'
    REASON_REFERENCE = 'Procedure.reason-reference'
    STATUS = 'Procedure.status'
    SUBJECT = 'Procedure.subject'
    NOTE = 'Procedure.note'

class RelatedPersonClaim:
    """FHIR-like flat claims generated from TypeScript ``RelatedPersonClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/relatedperson.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-RelatedPerson.html
    """

    IDENTIFIER = 'RelatedPerson.identifier'
    IDENTIFIER_VALUE = 'RelatedPerson.identifier'
    ACTIVE = 'RelatedPerson.active'
    PATIENT = 'RelatedPerson.patient'
    RELATIONSHIP = 'RelatedPerson.relationship'
    ROLE = 'RelatedPerson.role'
    NAME = 'RelatedPerson.name'
    TELECOM = 'RelatedPerson.telecom'
    GENDER = 'RelatedPerson.gender'
    BIRTH_DATE = 'RelatedPerson.birthdate'
    ADDRESS = 'RelatedPerson.address'
    RELATED_ENTITY_TYPE = 'RelatedPerson.related-entity-type'
    ACTOR_IDENTIFIER = 'RelatedPerson.actor-identifier'

class ResearchSubjectClaim:
    """FHIR-like flat claims generated from TypeScript ``ResearchSubjectClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/researchsubject.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-ResearchSubject.html
    """

    IDENTIFIER = 'ResearchSubject.identifier'

class TaskClaim:
    """FHIR-like flat claims generated from TypeScript ``TaskClaim``.

    Only names published on the resource search page are canonical
    FHIR search parameters. Other names require a FHIR standard or
    custom extension contract.

    Search parameters: https://hl7.org/fhir/task.html#search
    Standard extensions: https://hl7.org/fhir/extensions/extensions-Task.html
    """

    ID = 'Task.id'
    IDENTIFIER = 'Task.identifier'
    GROUP_IDENTIFIER = 'Task.group-identifier'
    STATUS = 'Task.status'
    STATUS_REASON = 'Task.status-reason'
    BUSINESS_STATUS = 'Task.business-status'
    INTENT = 'Task.intent'
    CODE = 'Task.code'
    DESCRIPTION = 'Task.description'
    SUBJECT = 'Task.subject'
    FOR = 'Task.for'
    REQUESTER = 'Task.requester'
    OWNER = 'Task.owner'
    FOCUS = 'Task.focus'
    PART_OF = 'Task.part-of'
    BASED_ON = 'Task.based-on'
    BASED_ON_DISPLAY = 'Task.based-on-display'
    LANGUAGE = 'Task.language'
    CHANNEL = 'Task.channel'
    AUTHORED_ON = 'Task.authored-on'
    LAST_MODIFIED = 'Task.last-modified'
    SCHEDULED_AT = 'Task.scheduled-at'
    RETRY_INTERVAL_MINUTES = 'Task.retry-interval-minutes'
    MAX_ATTEMPTS = 'Task.max-attempts'
    TRIGGER_TYPE = 'Task.trigger-type'
    ATTEMPT = 'Task.attempt'
    WINDOW_START = 'Task.window-start'
    WINDOW_END = 'Task.window-end'
    AUTO_CLOSE_AT = 'Task.auto-close-at'
    ESCALATION_RECIPIENT = 'Task.escalation-recipient'
    CONFIRMED = 'Task.confirmed'
    CONFIRMED_AT = 'Task.confirmed-at'
    REPETITIONS = 'Task.repetitions'
    DAYS_OF_WEEK = 'Task.days-of-week'
    REPEAT_COUNT = 'Task.repeat-count'
    REPEAT_DURATION_VALUE = 'Task.repeat-duration-value'
    REPEAT_DURATION_UNIT = 'Task.repeat-duration-unit'
    MODIFIED = 'Task.modified'
    PRIORITY = 'Task.priority'
    RESTRICTION_PERIOD_START = 'Task.restriction-period-start'
    RESTRICTION_PERIOD_END = 'Task.restriction-period-end'
    EXECUTION_PERIOD_START = 'Task.execution-period-start'
    EXECUTION_PERIOD_END = 'Task.execution-period-end'
    OUTPUT_TYPE = 'Task.output-type'
    OUTPUT_VALUE_REFERENCE = 'Task.output-value-reference'
    OUTPUT_VALUE_STRING = 'Task.output-value-string'
    USER_SELECTED = 'Task.user-selected'

__all__ = [
    'AllergyIntoleranceClaim',
    'AppointmentClaim',
    'AppointmentResponseClaim',
    'CarePlanClaim',
    'ChargeItemClaim',
    'ClinicalImpressionClaim',
    'CommunicationClaim',
    'CompositionClaim',
    'ConditionClaim',
    'CoverageClaim',
    'DeviceClaim',
    'DeviceUseStatementClaim',
    'DiagnosticReportClaim',
    'DocumentReferenceClaim',
    'EncounterClaim',
    'FlagClaim',
    'ImmunizationClaim',
    'InvoiceClaim',
    'LocationClaim',
    'MedicationStatementClaim',
    'ObservationClaim',
    'OrganizationClaim',
    'PractitionerRoleClaim',
    'ProcedureClaim',
    'RelatedPersonClaim',
    'ResearchSubjectClaim',
    'TaskClaim',
]
