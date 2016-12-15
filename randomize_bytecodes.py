""" Some text """

import random

def main():
    content_begin = []
    content_middle = []
    content_end = []

    instruction_table = [
    ]

    info_table = [
    ]

    parse_instruction_table = False
    parse_info_table = False
    read_part = 0

    with open("angelscript.h", "r") as f:
        for line in f:
            if parse_info_table:
                if line.strip() == "{":
                    content_middle.append(line.rstrip())
                elif line.strip() == "};":
                    content_end.append(line.rstrip())
                    parse_info_table = False
                elif line.strip() == "":
                    pass
                elif line.strip().startswith("//"):
                    pass
                else:
                    info_table.append(line.strip()[:-1])
            elif parse_instruction_table:
                if line.strip() == "{":
                    content_begin.append(line.rstrip())
                elif line.strip() == "};":
                    content_middle.append(line.rstrip())
                    parse_instruction_table = False
                elif line.strip() == "":
                    pass
                elif line.strip().startswith("//"):
                    pass
                else:
                    instruction_table.append(line.split("=")[0].strip())
            else:
                if read_part == 0:
                    content_begin.append(line.rstrip())
                    if line.strip() == "enum asEBCInstr":
                        parse_instruction_table = True
                        read_part = 1
                elif read_part == 1:
                    content_middle.append(line.rstrip())
                    if line.strip() == "const asSBCInfo asBCInfo[256] =":
                        parse_info_table = True
                        read_part = 2
                else:
                    content_end.append(line.rstrip())

    max_bytecode = instruction_table.index("asBC_MAXBYTECODE")

    to_add = 256 - len(instruction_table)

    dummies = []

    for i in range(max_bytecode+1, max_bytecode+1+to_add):
        dummies.append("as_DUMMY_" + str(i))

    instruction_table[max_bytecode+1:max_bytecode+1] = dummies

    indexes = random.sample(range(0, max_bytecode), max_bytecode)

    with open("angelscript.h", "w") as f:
        f.write("\n".join(content_begin) + "\n")

        # randomize
        for ind, i in enumerate(indexes):
            f.write(instruction_table[i] + " = " + str(ind) + "," + "\n")

        for i in range(max_bytecode, 256):
            if i < 255:
                f.write(instruction_table[i] + " = " + str(i) + "," + "\n")
            else:
                f.write(instruction_table[i] + " = " + str(i) + "\n")

        f.write("\n".join(content_middle) + "\n")

        #randomize
        for ind, i in enumerate(indexes):
            f.write(info_table[i] + "," + "\n")

        for i in range(max_bytecode, 256):
            if i < 255:
                f.write(info_table[i] + "," + "\n")
            else:
                f.write(instruction_table[i] + "\n")

        f.write("\n".join(content_end))

main()
