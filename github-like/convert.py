import json
from argparse import ArgumentParser
from datetime import datetime

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("dates_txt_path")
    parser.add_argument("output_json_path")
    args = parser.parse_args()

    commits_dict = {}
    with open(args.dates_txt_path, encoding="utf8") as fin:
        for row in fin:
            date_str = row.rstrip()
            the_datetime = datetime.strptime(date_str, "%Y/%m/%d")
            timestamp = the_datetime.timestamp()
            commits_dict[str(timestamp)] = 1

    with open(args.output_json_path, "w", encoding="utf8") as fout:
        json.dump(commits_dict, fout, indent=2)
