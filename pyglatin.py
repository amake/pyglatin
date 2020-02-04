import sys
import re

CONSONANTS = r'^(?P<pref>[bcdfghjklmnpqrstvwxyz]+)'
CONSONANTS_PATTERN = re.compile(CONSONANTS, re.IGNORECASE)
PUNCTUATION = (r'^(?P<pref>[^abcdefghijklmnopqrstuvwxyz]*)'
               r'(?P<word>.*?)'
               r'(?P<suff>[^abcdefghijklmnopqrstuvwxyz]*)$')
PUNCTUATION_PATTERN = re.compile(PUNCTUATION, re.IGNORECASE)


def match_caps(txt: str, to: str):
    if to.islower():
        return txt.lower()
    # istitle check must be before isupper to correctly handle single-char
    # strings
    elif to.istitle():
        # Regular str.title() handles punctuation poorly so we use our own
        return to_title(txt)
    elif to.isupper():
        return txt.upper()
    else:
        return txt


def to_title(txt: str):
    if not txt:
        return txt
    elif len(txt) == 1:
        return txt.upper()
    else:
        return txt[0].upper() + txt[1:].lower()


def convert_word(word):
    return ignoring_punctuation(word, piglatinize_word)


def piglatinize_word(word):
    m = CONSONANTS_PATTERN.match(word)
    if m is not None:
        orig_prefix = m.group('pref')
        prefix = orig_prefix.lower()
        stem = word[len(prefix):]
        # Match caps of stem to orig_prefix to avoid being fooled by
        # punctuation
        matched_stem = match_caps(stem, orig_prefix)
        return matched_stem + prefix + 'ay'
    else:
        return word + 'ay'


def ignoring_punctuation(word, op):
    m = PUNCTUATION_PATTERN.match(word)
    assert m is not None
    punct_start = m.group('pref')
    punct_end = m.group('suff')
    naked_word = m.group('word')
    return punct_start + op(naked_word) + punct_end


def convert(src):
    return ' '.join(convert_word(word) for word in src.split())


def main():
    args = sys.argv[1:]
    srcs = args or [line.strip() for line in sys.stdin.readlines()]
    for src in srcs:
        print(convert(src))


if __name__ == '__main__':
    main()
