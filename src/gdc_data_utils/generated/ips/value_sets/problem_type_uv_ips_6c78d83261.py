"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/problem-type-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/problem-type-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'ProblemTypeUvIps',
 'title': 'Problem Type - IPS',
 'status': 'active',
 'description': 'This value set provides a category for the condition as a clinical problem for '
                'inclusion in the patient summary.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/condition-category',
                          'version': '2.0.0',
                          'concept': [{'code': 'problem-list-item',
                                       'display': 'Problem List Item'}]}]},
 'usages': [{'resourceType': 'Condition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.1',
             'elementId': 'Condition.category',
             'path': 'Condition.category',
             'purpose': 'primary',
             'strength': 'extensible'}]}
