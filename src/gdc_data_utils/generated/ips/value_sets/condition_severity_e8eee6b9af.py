"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/condition-severity|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/condition-severity',
 'resolved': True,
 'version': '4.0.1',
 'name': 'Condition/DiagnosisSeverity',
 'title': 'Condition/Diagnosis Severity',
 'status': 'draft',
 'description': 'Preferred value set for Condition/Diagnosis severity grading.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'concept': [{'code': '24484000'},
                                      {'code': '6736007'},
                                      {'code': '255604002'}]}]},
 'usages': [{'resourceType': 'Condition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.1',
             'elementId': 'Condition.severity',
             'path': 'Condition.severity',
             'purpose': 'primary',
             'strength': 'preferred'}]}
