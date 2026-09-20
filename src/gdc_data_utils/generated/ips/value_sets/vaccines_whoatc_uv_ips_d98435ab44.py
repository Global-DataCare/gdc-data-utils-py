"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/vaccines-whoatc-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/vaccines-whoatc-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'VaccinesWhoAtcUvIps',
 'title': 'Vaccines WHO ATC - IPS',
 'status': 'active',
 'description': 'IPS Vaccine codes value set.  This value set includes codes from the World Health '
                'Organization Anatomical Therapeutic Chemical (ATC) classification system: all '
                'descendants of J07 "VACCINES"',
 'immutable': False,
 'compose': {'include': [{'system': 'http://www.whocc.no/atc',
                          'filter': [{'property': 'concept',
                                      'op': 'descendent-of',
                                      'value': 'J07'}]}]},
 'usages': [{'resourceType': 'Immunization',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Immunization-uv-ips|2.0.1',
             'elementId': 'Immunization.vaccineCode',
             'path': 'Immunization.vaccineCode',
             'purpose': 'additional',
             'strength': 'preferred'}]}
