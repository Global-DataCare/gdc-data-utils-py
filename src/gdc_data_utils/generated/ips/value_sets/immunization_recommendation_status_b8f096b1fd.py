"""Generated deduplicated IPS ValueSet; do not edit."""


VALUE_SET = {'canonicalReference': 'http://hl7.org/fhir/ValueSet/immunization-recommendation-status',
 'canonicalUrl': 'http://hl7.org/fhir/ValueSet/immunization-recommendation-status',
 'resolved': True,
 'version': '4.0.1',
 'name': 'ImmunizationRecommendationStatusCodes',
 'title': 'Immunization Recommendation Status Codes',
 'status': 'draft',
 'description': 'The value set to instantiate this attribute should be drawn from a '
                'terminologically robust code system that consists of or contains concepts to '
                'support describing the status of the patient towards perceived immunity against a '
                'vaccine preventable disease. This value set is provided as a suggestive example.',
 'immutable': True,
 'compose': {'include': [{'system': 'http://terminology.hl7.org/CodeSystem/immunization-recommendation-status'}]},
 'usages': [{'resourceType': 'ImmunizationRecommendation',
             'profile': 'http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation|4.0.1',
             'elementId': 'ImmunizationRecommendation.recommendation.forecastStatus',
             'path': 'ImmunizationRecommendation.recommendation.forecastStatus',
             'purpose': 'primary',
             'strength': 'example'}]}
