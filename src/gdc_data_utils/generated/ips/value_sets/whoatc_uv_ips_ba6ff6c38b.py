"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/uv/ips/ValueSet/whoatc-uv-ips|2.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/uv/ips/ValueSet/whoatc-uv-ips',
 'resolved': True,
 'version': '2.0.1',
 'name': 'WhoAtcUvIps',
 'title': 'WHO ATC - IPS',
 'status': 'active',
 'description': 'World Health Organization Anatomical Therapeutic Chemical (ATC) classification '
                'system.',
 'immutable': False,
 'compose': {'include': [{'system': 'http://www.whocc.no/atc'}]},
 'usages': [{'resourceType': 'AllergyIntolerance',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/AllergyIntolerance-uv-ips|2.0.1',
             'elementId': 'AllergyIntolerance.code',
             'path': 'AllergyIntolerance.code',
             'purpose': 'additional',
             'strength': 'preferred'},
            {'resourceType': 'Medication',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Medication-uv-ips|2.0.1',
             'elementId': 'Medication.code',
             'path': 'Medication.code',
             'purpose': 'additional',
             'strength': 'preferred'}]}
