from docassemble.base.util import DAObject
from docassemble.base.functions import value


def convert_assignment(field: str) -> str:
    if field == "joint":
        return "Joint (50/50)"
    else:
        return str(value(field))


def assignment_choices(*args: DAObject, joint: bool = False) -> list[dict]:
    the_list = list()
    for arg in args:
        the_list.append({"label": arg, "value": arg.instanceName})
    if joint:
        the_list.append({"label": "Joint (50/50)", "value": "joint"})
    return the_list


def required_question(label: str) -> str:
    return f"""<div class="da-form-group darequired"><label class="da-top-label">{label}</label></div>"""
