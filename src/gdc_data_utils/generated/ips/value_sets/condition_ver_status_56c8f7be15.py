"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/condition-ver-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConditionVerificationStatus',
 'title': 'ConditionVerificationStatus',
 'status': 'draft',
 'description': 'The verification status to support or decline the clinical status of the '
                'condition or diagnosis.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/condition-ver-status'}]},
 'usages': [{'resourceType': 'Condition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips|2.0.1',
             'elementId': 'Condition.verificationStatus',
             'path': 'Condition.verificationStatus',
             'purpose': 'primary',
             'strength': 'required'}]}
