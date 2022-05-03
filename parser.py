import pyparsing as pp

LABEL = pp.Word(pp.alphas+"_", pp.alphanums+"_") + ":"
EXTERN = "extern" + pp.Word(pp.alphas+"_")
RET = "ret"
SECTION = "section" + pp.Word(pp.alphas+'.')
COMMAND = pp.Word(pp.alphas) + pp.Word(pp.alphas+"_") + pp.Optional(
    "," + pp.Word(pp.alphas+"_")
)
PARSER = LABEL ^ COMMAND ^ EXTERN ^ SECTION ^ RET


def parse(program: str) -> list[str]:
    lines = []
    for line in program.splitlines():
        parsed_line = None
        try:
            parsed_line = PARSER.parseString(line)
            lines.append(parsed_line)
        except pp.ParseException as e:
            print(e.msg)
            print("Failed parsing line:")
            print(line)
    lines = map_results_to_list(lines)
    return lines


def map_results_to_list(results):
    return list(
        map(
            lambda r:
                r.__dict__['_ParseResults__toklist']
                if '_ParseResults__toklist' in r.__dict__.keys() else None,
            results
        )
    )