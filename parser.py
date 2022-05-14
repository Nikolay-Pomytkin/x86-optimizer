import pyparsing as pp

LABEL = pp.Word(pp.alphas+"_"+"?", pp.alphanums+"_"+"?") + ":"
EXTERN = "extern" + pp.Word(pp.alphas+"_"+"?", pp.alphanums+"_"+"?")
RET = "ret"
SECTION = "section" + pp.Word(pp.alphas+'.')
WORD = pp.Word(pp.alphanums+"_"+"?", pp.alphanums+"_"+"?") ^ pp.Regex(r'\[[A-za-z]+ \+ [0-9]+\]') ^ pp.Regex(r'\[[A-za-z]+ [0-9\_]+\]')
COMMAND = pp.Word(pp.alphanums+"?", pp.alphanums+"_"+"?") + WORD + pp.Optional(
    "," + WORD
)
LEA = pp.Regex(r'lea [A-Za-z]+, \[.+\]')
COMMAND_TTL = COMMAND ^ LEA
REGISTER = None

# TOTAL PARSING GRAMMER
PARSER = LABEL ^ COMMAND_TTL ^ EXTERN ^ SECTION ^ RET


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
