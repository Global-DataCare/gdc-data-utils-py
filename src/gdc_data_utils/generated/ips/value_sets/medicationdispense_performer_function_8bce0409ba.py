"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/medicationdispense-performer-function',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/medicationdispense-performer-function',
 'resolved': True,
 'version': '4.0.1',
 'name': 'MedicationDispense Performer Function Codes',
 'title': 'Medication dispense  performer  function  codes',
 'status': 'draft',
 'description': 'MedicationDispense Performer Function Codes',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/medicationdispense-performer-function'}]},
 'usages': [{'resourceType': 'MedicationDispense',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationDispense|4.0.1',
             'elementId': 'MedicationDispense.performer.function',
             'path': 'MedicationDispense.performer.function',
             'purpose': 'primary',
             'strength': 'example'}]}
