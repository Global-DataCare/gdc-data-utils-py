"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/consent-state-codes',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConsentState',
 'title': 'ConsentState',
 'status': 'draft',
 'description': 'Indicates the state of the consent.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/consent-state-codes'}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.status',
             'path': 'Consent.status',
             'purpose': 'primary',
             'strength': 'required'}]}
