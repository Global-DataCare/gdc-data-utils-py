"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/medicationrequest-intent|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/medicationrequest-intent',
 'resolved': True,
 'version': '4.0.1',
 'name': 'medicationRequest Intent',
 'title': 'Medication request  intent',
 'status': 'draft',
 'description': 'MedicationRequest Intent Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/CodeSystem/medicationrequest-intent'}]},
 'usages': [{'resourceType': 'MedicationRequest',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/MedicationRequest-uv-ips|2.0.1',
             'elementId': 'MedicationRequest.intent',
             'path': 'MedicationRequest.intent',
             'purpose': 'primary',
             'strength': 'required'}]}
