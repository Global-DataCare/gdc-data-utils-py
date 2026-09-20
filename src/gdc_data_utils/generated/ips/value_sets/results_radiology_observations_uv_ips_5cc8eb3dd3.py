"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/results-radiology-observations-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/results-radiology-observations-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'ResultsRadiologyObservationUvIps',
 'title': 'Results Radiology Observation - IPS',
 'status': 'active',
 'description': 'Value Set Definition: \n'
                'LOINC {STATUS in {ACTIVE}, CLASS in LP29684-5 (\\"RAD\\")}',
 'immutable': False,
 'compose': {'include': [{'system': 'http://loinc.org',
                          'filter': [{'property': 'STATUS', 'op': '=', 'value': 'ACTIVE'},
                                     {'property': 'CLASS', 'op': '=', 'value': 'LP29684-5'}]}]},
 'usages': [{'resourceType': 'ImagingStudy',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/ImagingStudy-uv-ips|2.0.1',
             'elementId': 'ImagingStudy.procedureCode',
             'path': 'ImagingStudy.procedureCode',
             'purpose': 'additional',
             'strength': 'extensible'},
            {'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-radiology-uv-ips|2.0.1',
             'elementId': 'Observation.code',
             'path': 'Observation.code',
             'purpose': 'primary',
             'strength': 'preferred'}]}
