from docassemble.base.functions import states_list
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

#def custody_plaintiff_complaint_residence():
#    if value('confidential_contact_info_yn'):
#        if value('users[0].lives_in_Michigan'):
#            return value('users[0].address.county') + " County, Michigan"
#        elif value('safe_to_disclose_state'):
#            if value('users[0].foreign_residence'):
#                return value('country_name(users[0].country_of_residence_to_disclose)')
#            else:
#                return "State of " + value('state_name(users[0].state_of_residence_to_disclose)')
#        else:
#            return "Confidential"
#    else:
#        if value('users[0].address.country') == "US":
#            if value('users[0].address.state') == "MI":
#                return value('users[0].address.county') + " County, Michigan"
#            else:
#                return "State of " + value('state_name(users[0].address.state)')
#        else:
#            return value('country_name(users[0].address.country)')