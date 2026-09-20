"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/results-status-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/results-status-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'ResultsStatusUvIps',
 'title': 'Results Status Codes - IPS',
 'status': 'active',
 'description': 'IPS Observation status codes allowable for results.  This value set includes all '
                'observation status codes except \\"entered-in-error\\" from '
                'http://hl7.org/fhir/observation-status.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/observation-status', 'version': '4.0.1'}],
             'exclude': [{'system': 'http://hl7.org/fhir/observation-status',
                          'version': '4.0.1',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': 'entered-in-error'}]}]},
 'usages': [{'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-laboratory-pathology-uv-ips|2.0.1',
             'elementId': 'Observation.status',
             'path': 'Observation.status',
             'purpose': 'primary',
             'strength': 'required'},
            {'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-radiology-uv-ips|2.0.1',
             'elementId': 'Observation.status',
             'path': 'Observation.status',
             'purpose': 'primary',
             'strength': 'required'}]}
