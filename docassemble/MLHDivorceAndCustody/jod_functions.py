from docassemble.base.functions import states_list, state_name, country_name
from docassemble.base.util import Address, validation_error


def validate_us_state(address: Address) -> None:
    if address.country == "US" and not len(address.state) == 2:
        users_state = address.state.lower()
        states_abbr = {v.lower(): k for k, v in states_list().items()}
        if users_state in states_abbr:
            address.state = states_abbr[users_state]
        else:
            validation_error("You must enter the state's two-letter abbreviation.", f"""{address.attr_name("state")}""")

def cases_for_UCCJEA_5(cases):
    return [case for case in cases if case.type != "name_change" and case.resolved == False]

def custody_plaintiff_complaint_residence(user, is_confidential):
    if is_confidential:
        if user.lives_in_Michigan:
            return user.address.county + " County, Michigan"
        elif user.safe_to_disclose_state:
            if user.foreign_residence:
                return country_name(user.country_of_residence_to_disclose)
            else:
                return "State of " + state_name(user.state_of_residence_to_disclose)
        else:
            return "Confidential"
    else:
        if user.address.country == "US":
            if user.address.state == "MI":
                return user.address.county + " County, Michigan"
            else:
                return "State of " + state_name(user.address.state)
        else:
            return country_name(user.address.country)