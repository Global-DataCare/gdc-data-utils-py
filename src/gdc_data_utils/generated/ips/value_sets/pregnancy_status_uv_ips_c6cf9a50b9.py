"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/pregnancy-status-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/pregnancy-status-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'PregnancyStatusUvIps',
 'title': 'Pregnancy Status - IPS',
 'status': 'active',
 'description': 'IPS pregnancy status codes value set.  This value set includes codes from SNOMED '
                'CT®: 77386006 \\|Pregnant\\|; 60001007 \\|Not pregnant\\|; 152231000119106 '
                '\\|Pregnancy not yet confirmed\\|; 146799005 \\|Possible pregnancy\\|\n'
                '\n'
                'SNOMED CT® ECL definition:\\\n'
                '77386006 \\|Pregnant\\| OR 60001007 \\|Not pregnant\\| OR 152231000119106 '
                '\\|Pregnancy not yet confirmed\\| OR 146799005 \\|Possible pregnancy\\|',
 'immutable': False,
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'concept': [{'code': '77386006', 'display': 'Pregnant'},
                                      {'code': '60001007', 'display': 'Not pregnant'},
                                      {'code': '152231000119106',
                                       'display': 'Pregnancy not yet confirmed'},
                                      {'code': '146799005', 'display': 'Possible pregnancy'}]}]},
 'usages': [{'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-pregnancy-status-uv-ips|2.0.1',
             'elementId': 'Observation.value[x]:valueCodeableConcept',
             'path': 'Observation.value[x]',
             'purpose': 'primary',
             'strength': 'preferred'}]}
