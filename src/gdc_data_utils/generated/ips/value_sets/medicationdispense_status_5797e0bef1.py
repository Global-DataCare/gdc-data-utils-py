"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/medicationdispense-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/medicationdispense-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'MedicationDispense Status Codes',
 'title': 'Medication dispense  status  codes',
 'status': 'draft',
 'description': 'MedicationDispense Status Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/medicationdispense-status'}]},
 'usages': [{'resourceType': 'MedicationDispense',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationDispense|4.0.1',
             'elementId': 'MedicationDispense.status',
             'path': 'MedicationDispense.status',
             'purpose': 'primary',
             'strength': 'required'}]}
