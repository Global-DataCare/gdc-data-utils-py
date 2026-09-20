"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/consent-provision-type|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/consent-provision-type',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ConsentProvisionType',
 'title': 'ConsentProvisionType',
 'status': 'draft',
 'description': 'How a rule statement is applied, such as adding additional consent or removing '
                'consent.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/consent-provision-type'}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.provision.type',
             'path': 'Consent.provision.type',
             'purpose': 'primary',
             'strength': 'required'}]}
