

def get_dept_code_from_plots(references: list[str]) -> list[str]:
    return [
        r[:2] if r[:2] != '97' else r[:3] for r in references
    ]
