"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/medicationdispense-category',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/medicationdispense-category',
 'resolved': True,
 'version': '4.0.1',
 'name': 'MedicationDispense Category Codes',
 'title': 'Medication dispense  category  codes',
 'status': 'draft',
 'description': 'MedicationDispense Category Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-category'}]},
 'usages': [{'resourceType': 'MedicationDispense',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationDispense|4.0.1',
             'elementId': 'MedicationDispense.category',
             'path': 'MedicationDispense.category',
             'purpose': 'primary',
             'strength': 'preferred'}]}
