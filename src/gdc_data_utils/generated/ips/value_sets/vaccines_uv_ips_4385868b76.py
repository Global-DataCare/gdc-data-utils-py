"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/vaccines-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/vaccines-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'VaccinesUvIps',
 'title': 'Vaccines - IPS',
 'status': 'active',
 'description': 'IPS Vaccine codes value set.  This value set includes codes from SNOMED CT®: all '
                'descendants of 787859002 \\|Vaccine product (product)\\|; all descendants or self '
                'of 787482006 \\|No known immunizations (situation)\\|\n'
                '\n'
                'SNOMED CT® ECL definition:\\\n'
                '< 787859002 \\|Vaccine product (product)\\| OR \\<\\< 787482006 \\|No known '
                'immunizations (situation)\\|',
 'immutable': False,
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'descendent-of',
                                      'value': '787859002'}]},
                         {'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '787482006'}]}]},
 'usages': [{'resourceType': 'Immunization',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Immunization-uv-ips|2.0.1',
             'elementId': 'Immunization.vaccineCode',
             'path': 'Immunization.vaccineCode',
             'purpose': 'primary',
             'strength': 'preferred'}]}
