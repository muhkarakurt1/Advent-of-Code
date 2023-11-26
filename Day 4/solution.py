contains_counter = 0
overlaps_counter = 0

with open("input.txt") as f:
    line_no = 1

    for line in f:
        first_elf, second_elf = line.strip().split(",")
        first_elf_start, first_elf_end = first_elf.split("-")
        second_elf_start, second_elf_end = second_elf.split("-")

        first_elf_coverage = list(range(int(first_elf_start), int(first_elf_end) + 1))
        second_elf_coverage = list(range(int(second_elf_start), int(second_elf_end) + 1))

        # PART 1
        # if set(first_elf_coverage).issubset(second_elf_coverage) or set(second_elf_coverage).issubset(first_elf_coverage):
        #     print('FIRST', first_elf_coverage)
        #     print('SECOND', second_elf_coverage)
        #     print('LINE:', line_no)
        #     contains_counter += 1

        # PART 2
        if any(i in first_elf_coverage for i in second_elf_coverage):
            overlaps_counter += 1
            # print('FIRST', first_elf_coverage)
            # print('SECOND', second_elf_coverage)
            # print('LINE:', line_no)

        line_no += 1
print(overlaps_counter)
