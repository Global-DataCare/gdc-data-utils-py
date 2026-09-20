"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://terminology.hl7.org/ValueSet/v3-PurposeOfUse',
 'canonicalUrl': 'http://terminology.hl7.org/ValueSet/v3-PurposeOfUse',
 'resolved': True,
 'version': '2014-03-26',
 'name': 'v3.PurposeOfUse',
 'title': 'V3 Value SetPurposeOfUse',
 'status': 'active',
 'description': ' Supports communication of purpose of use at a general level.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-ActReason',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': 'PurposeOfUse'}]}]},
 'usages': [{'resourceType': 'Consent',
             'profile': 'http://hl7.org/fhir/StructureDefinition/Consent|4.0.1',
             'elementId': 'Consent.provision.purpose',
             'path': 'Consent.provision.purpose',
             'purpose': 'primary',
             'strength': 'extensible'}]}
