"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/flag-category|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/flag-category',
 'resolved': True,
 'version': '4.0.1',
 'name': 'FlagCategory',
 'title': 'Flag Category',
 'status': 'draft',
 'description': 'Example list of general categories for flagged issues. (Not complete or '
                'necessarily appropriate.)',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/flag-category'}]},
 'usages': [{'resourceType': 'Flag',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Flag-alert-uv-ips|2.0.1',
             'elementId': 'Flag.category',
             'path': 'Flag.category',
             'purpose': 'primary',
             'strength': 'example'}]}
