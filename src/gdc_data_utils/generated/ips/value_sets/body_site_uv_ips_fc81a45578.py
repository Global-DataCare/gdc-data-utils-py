"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/body-site-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/body-site-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'BodySiteUvIps',
 'title': 'Body Site - IPS',
 'status': 'active',
 'description': 'IPS body site value set. This value set includes a set of codes from SNOMED CT '
                'that may be used to represent body sites (e.g., for laboratory specimen '
                'collection). This value set includes codes from SNOMED CT®: all descendants of '
                '442083009 \\|Anatomical or acquired body structure (body structure)\\|\n'
                '\n'
                'SNOMED CT® ECL definition:\\\n'
                '< 442083009 \\|Anatomical or acquired body structure (body structure)\\|',
 'immutable': False,
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'descendent-of',
                                      'value': '442083009'}]}]},
 'usages': [{'resourceType': 'Specimen',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Specimen-uv-ips|2.0.1',
             'elementId': 'Specimen.collection.bodySite',
             'path': 'Specimen.collection.bodySite',
             'purpose': 'primary',
             'strength': 'preferred'}]}
