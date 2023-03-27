from policyengine_canada.model_api import *


class ntcb_older_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount for all children under the NTCB"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        younger = household("ntcb_younger_base", period)
        older = household("ntcb_older_base", period)
        return older + younger
