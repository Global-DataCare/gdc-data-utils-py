"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/composition-attestation-mode',
 'resolved': True,
 'version': '4.0.1',
 'name': 'CompositionAttestationMode',
 'title': 'CompositionAttestationMode',
 'status': 'draft',
 'description': 'The way in which a person authenticated a composition.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/composition-attestation-mode'}]},
 'usages': [{'resourceType': 'Composition',
             'profile': 'http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips|2.0.1',
             'elementId': 'Composition.attester.mode',
             'path': 'Composition.attester.mode',
             'purpose': 'primary',
             'strength': 'required'}]}
