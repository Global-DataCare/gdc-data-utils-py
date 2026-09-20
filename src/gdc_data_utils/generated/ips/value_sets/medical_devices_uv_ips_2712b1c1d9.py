"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/medical-devices-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/medical-devices-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'MedicalDevicesUvIps',
 'title': 'Medical Devices - IPS',
 'status': 'active',
 'description': 'IPS Medical device codes value set.  This value set includes codes from SNOMED CT '
                '(SNOMED CT®) that are included in: all descendants of 49062001 \\|Device '
                '(physical object)\\|; all descendants or self of 787483001 \\|No known device use '
                '(situation)\\|\n'
                '\n'
                'SNOMED CT® ECL definition:\\\n'
                '< 49062001 \\|Device (physical object)\\| OR \\<\\< 787483001 \\|No known device '
                'use (situation)\\|',
 'immutable': False,
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'descendent-of',
                                      'value': '49062001'}]},
                         {'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '787483001'}]}]},
 'usages': [{'resourceType': 'Device',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Device-uv-ips|2.0.1',
             'elementId': 'Device.type',
             'path': 'Device.type',
             'purpose': 'primary',
             'strength': 'preferred'}]}
