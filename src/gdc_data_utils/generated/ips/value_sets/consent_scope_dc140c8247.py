"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/consent-scope',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/consent-scope',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConsentScopeCodes',
 'title': 'Consent Scope Codes',
 'status': 'draft',
 'description': 'This value set includes the four Consent scope codes.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/consentscope'}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.scope',
             'path': 'Consent.scope',
             'purpose': 'primary',
             'strength': 'extensible'}]}
