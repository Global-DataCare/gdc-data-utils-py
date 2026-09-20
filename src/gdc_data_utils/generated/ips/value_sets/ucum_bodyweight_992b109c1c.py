"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/ucum-bodyweight|4.0.1',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/ucum-bodyweight',
 'resolved': True,
 'version': '4.0.1',
 'name': 'BodyWeightUnits',
 'title': 'Body Weight Units',
 'status': 'draft',
 'description': 'UCUM units for recording Body Weight',
 'compose': {'include': [{'system': 'http://unitsofmeasure.org',
                          'concept': [{'code': 'kg'}, {'code': '[lb_av]'}, {'code': 'g'}]}]},
 'usages': [{'resourceType': 'Observation',
             'profile': 'http://hl7.org/fhir/StructureDefinition/bodyweight|4.0.1',
             'elementId': 'Observation.value[x]:valueQuantity.code',
             'path': 'Observation.value[x].code',
             'purpose': 'primary',
             'strength': 'required'}]}
