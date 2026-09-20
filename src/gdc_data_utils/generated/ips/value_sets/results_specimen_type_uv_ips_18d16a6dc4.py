"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/results-specimen-type-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/results-specimen-type-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'ResultsSpecimenTypeUvIps',
 'title': 'Results Specimen Type - IPS',
 'status': 'active',
 'description': 'IPS Specimen Type codes value set.  This value set includes codes from SNOMED '
                'CT®: all descendants of 123038009 \\|Specimen (specimen)\\|\n'
                '\n'
                'SNOMED CT® ECL definition:\\\n'
                '< 123038009 \\|Specimen (specimen)\\|',
 'immutable': False,
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'descendent-of',
                                      'value': '123038009'}]}]},
 'usages': [{'resourceType': 'Specimen',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Specimen-uv-ips|2.0.1',
             'elementId': 'Specimen.type',
             'path': 'Specimen.type',
             'purpose': 'primary',
             'strength': 'preferred'}]}
