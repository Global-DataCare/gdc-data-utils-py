"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/request-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/request-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'RequestStatus',
 'title': 'RequestStatus',
 'status': 'draft',
 'description': 'Codes identifying the lifecycle stage of a request.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/request-status'}]},
 'usages': [{'resourceType': 'CarePlan',
             'profile': 'http://hl7.org/fhir/StructureDefinition/CarePlan|4.0.1',
             'elementId': 'CarePlan.status',
             'path': 'CarePlan.status',
             'purpose': 'primary',
             'strength': 'required'}]}
