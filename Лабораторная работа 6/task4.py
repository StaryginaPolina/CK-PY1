import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=",", new_line="\n") -> list[dict]:  # TODO реализовать конвертер из csv в json
    with open(file) as f:
        list_ = []
        for index, line in enumerate(f):
            values = line.strip(new_line).split(delimiter)
            if index == 0:
                headings = values
                continue
            list_.append({})
            for head, _ in enumerate(headings):
                list_[-1][headings[head]] = values[head]
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# end
