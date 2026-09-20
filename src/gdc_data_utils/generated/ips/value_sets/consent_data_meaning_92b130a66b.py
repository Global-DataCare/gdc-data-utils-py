"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/consent-data-meaning|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/consent-data-meaning',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConsentDataMeaning',
 'title': 'ConsentDataMeaning',
 'status': 'draft',
 'description': 'How a resource reference is interpreted when testing consent restrictions.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/consent-data-meaning'}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.provision.data.meaning',
             'path': 'Consent.provision.data.meaning',
             'purpose': 'primary',
             'strength': 'required'}]}
