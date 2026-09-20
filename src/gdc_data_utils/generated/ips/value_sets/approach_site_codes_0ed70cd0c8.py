"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/approach-site-codes',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/approach-site-codes',
 'resolved': True,
 'version': '4.0.1',
 'name': 'SNOMEDCTAnatomicalStructureForAdministrationSiteCodes',
 'title': 'SNOMED CT Anatomical Structure for Administration Site Codes',
 'status': 'draft',
 'description': 'This value set includes Anatomical Structure codes from SNOMED CT - provided as '
                'an exemplar.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept', 'op': 'is-a', 'value': '91723000'}]}]},
 'usages': [{'resourceType': 'MedicationAdministration',
             'profile': 'http://hl7.org/fhir/StructureDefinition/MedicationAdministration|4.0.1',
             'elementId': 'MedicationAdministration.dosage.site',
             'path': 'MedicationAdministration.dosage.site',
             'purpose': 'primary',
             'strength': 'example'}]}
