"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/care-plan-category',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/care-plan-category',
 'resolved': True,
 'version': '4.0.1',
 'name': 'CarePlanCategory',
 'title': 'Care Plan Category',
 'status': 'draft',
 'description': 'Example codes indicating the category a care plan falls within.  Note that these '
                'are in no way complete and might not even be appropriate for some uses.',
 'compose': {'include': [{'system': 'http://snomed.info/sct',
                          'filter': [{'property': 'concept',
                                      'op': 'is-a',
                                      'value': '734163000'}]}]},
 'usages': [{'resourceType': 'CarePlan',
             'profile': 'http://hl7.org/fhir/StructureDefinition/CarePlan|4.0.1',
             'elementId': 'CarePlan.category',
             'path': 'CarePlan.category',
             'purpose': 'primary',
             'strength': 'example'}]}
