"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/flag-code|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/flag-code',
 'resolved': True,
 'version': '4.0.1',
 'name': 'FlagCode',
 'title': 'Flag Code',
 'status': 'draft',
 'description': 'Example list of detail codes for flagged issues.  (Not complete or necessarily '
                'appropriate.)',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '404684003'}]}]},
 'usages': [{'resourceType': 'Flag',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Flag-alert-uv-ips|2.0.1',
             'elementId': 'Flag.code',
             'path': 'Flag.code',
             'purpose': 'primary',
             'strength': 'example'}]}
