"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/medication-admin-category',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/medication-admin-category',
 'resolved': True,
 'version': '4.0.1',
 'name': 'MedicationAdministration Category Codes',
 'title': 'Medication administration  category  codes',
 'status': 'draft',
 'description': 'MedicationAdministration Category Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/medication-admin-category'}]},
 'usages': [{'resourceType': 'MedicationAdministration',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationAdministration|4.0.1',
             'elementId': 'MedicationAdministration.category',
             'path': 'MedicationAdministration.category',
             'purpose': 'primary',
             'strength': 'preferred'}]}
