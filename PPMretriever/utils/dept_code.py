

def get_dept_code_from_reference_code(references: list[str]) -> list[str]:
    """
    Isolates department codes from a list of reference
    :param references: list of plots (14 chars) or municipalities (5 chars) or dept code (2-3 chars)
    :return: Department codes
    """
    return [r[:2] if r[:2] != '97' else r[:3] for r in references]
