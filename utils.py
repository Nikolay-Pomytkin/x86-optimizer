from re import S
import typer


def print_break_line():
    typer.echo("==========================================\n")


def line_to_str(line: list[str]) -> str:
    if line[-1] == ':':
        return "".join(line)
    total = "        "
    # line_len = len(line) - 1
    for i, item in enumerate(line):
        if i != 0 and item != ',':
            total += " "
        total += item
    return total


def program_to_string(prog: list[list[str]]) -> str:
    return "\n".join(map(line_to_str, prog))


def save_program(file_path: str, program: str, optimized: bool = False):
    # make folder with same name as file with dot replaced with "_"
    file_path = file_path.split('.')
    if not optimized:
        file_path[len(file_path)-1] = '.s'
    else: 
        file_path[len(file_path)-1] = '_optimized.s'
    file_path = ''.join(file_path)
    # put both unoptimized and optimized file into that foldee
    file = open(file_path, "w")
    file.write(program)
    file.close()

