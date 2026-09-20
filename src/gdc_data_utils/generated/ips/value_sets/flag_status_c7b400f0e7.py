"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/flag-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/flag-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'FlagStatus',
 'title': 'FlagStatus',
 'status': 'draft',
 'description': 'Indicates whether this flag is active and needs to be displayed to a user, or '
                'whether it is no longer needed or was entered in error.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/flag-status'}]},
 'usages': [{'resourceType': 'Flag',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Flag-alert-uv-ips|2.0.1',
             'elementId': 'Flag.status',
             'path': 'Flag.status',
             'purpose': 'primary',
             'strength': 'required'}]}
