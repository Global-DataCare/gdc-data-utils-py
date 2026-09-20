"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/consent-action',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/consent-action',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConsentActionCodes',
 'title': 'Consent Action Codes',
 'status': 'draft',
 'description': 'This value set includes sample Consent Action codes.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/consentaction'}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.provision.action',
             'path': 'Consent.provision.action',
             'purpose': 'primary',
             'strength': 'example'}]}
