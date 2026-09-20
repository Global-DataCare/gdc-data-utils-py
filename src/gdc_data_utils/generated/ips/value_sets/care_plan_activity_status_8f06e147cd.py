"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/care-plan-activity-status|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/care-plan-activity-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'CarePlanActivityStatus',
 'title': 'CarePlanActivityStatus',
 'status': 'draft',
 'description': 'Codes that reflect the current state of a care plan activity within its overall '
                'life cycle.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://hl7.org/fhir/care-plan-activity-status'}]},
 'usages': [{'resourceType': 'CarePlan',
             'profile': 'http://hl7.org/fhir/StructureDefinition/CarePlan|4.0.1',
             'elementId': 'CarePlan.activity.detail.status',
             'path': 'CarePlan.activity.detail.status',
             'purpose': 'primary',
             'strength': 'required'}]}
