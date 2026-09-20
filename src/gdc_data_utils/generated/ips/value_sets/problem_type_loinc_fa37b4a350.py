"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/problem-type-loinc|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/problem-type-loinc',
 'resolved': True,
 'version': '2.0.1',
 'name': 'ProblemTypeLoinc',
 'title': 'Problem Type (LOINC)',
 'status': 'active',
 'description': 'This value set indicates the level of medical judgment used to determine the '
                'existence of a problem.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://loinc.org',
                          'concept': [{'code': '75326-9', 'display': 'Problem'}]}]},
 'usages': [{'resourceType': 'Condition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.1',
             'elementId': 'Condition.category',
             'path': 'Condition.category',
             'purpose': 'additional',
             'strength': 'extensible'}]}
