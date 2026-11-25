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

def not_name_change(case):
    return case.type != "name_change"