from policyengine_canada.model_api import *


class ntcb_younger_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for the NTCB in the younger bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(
                period
            ).gov.provinces.nt.tax.income.benefits.child_benefit.younger.age_eligibility
        )
