"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/med-admin-perform-function',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/med-admin-perform-function',
 'resolved': True,
 'version': '4.0.1',
 'name': 'MedicationAdministration Performer Function Codes',
 'title': 'Medication administration  performer  function  codes',
 'status': 'draft',
 'description': 'MedicationAdministration Performer Function Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/med-admin-perform-function'}]},
 'usages': [{'resourceType': 'MedicationAdministration',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationAdministration|4.0.1',
             'elementId': 'MedicationAdministration.performer.function',
             'path': 'MedicationAdministration.performer.function',
             'purpose': 'primary',
             'strength': 'example'}]}
