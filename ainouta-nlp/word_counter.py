import argparse
from collections import Counter

from spacy.lang.ja import Japanese

EXCLUDED_POS_SET = set(
    (
        "PUNCT",  # punctuation 句読点 （、。！？「」）
        "ADP",  # adposition 助詞（は、の、に、が、を）
        "AUX",  # auxiliary 助動詞（てる、だ、たい）
        "PART",  # particle 接辞（か、な、よ）
        "SCONJ",  # subordinating conjunction 従属接続詞（て）
    )
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_txt_path")
    parser.add_argument("--lower_limit", "-l", type=int, default=1)
    parser.add_argument("--display_pos", "-p", action="store_true")
    args = parser.parse_args()

    if args.display_pos:
        args.lower_limit = 0

    nlp = Japanese()

    words = []
    with open(args.input_txt_path, encoding="utf8") as f:
        for line in f:
            sentence = line.rstrip()
            if sentence:
                tokens = nlp(sentence)
                words.extend(
                    [
                        (token.lemma_, token.pos_)
                        if args.display_pos
                        else token.lemma_
                        for token in tokens
                        if token.pos_ not in EXCLUDED_POS_SET
                        and not token.is_stop
                    ]
                )

    counter = Counter(words)
    for word, count in counter.most_common():
        if count <= args.lower_limit:
            break
        print(f"{word} [{count}]")
