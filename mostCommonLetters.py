import math

MAX_LETTERS = 20


def collect_data(text: str) -> dict:

    if not text:
        raise ValueError('The text is empty.')

    letters = {}

    for ch in text.upper():
        if ch.isalpha():
            if ch not in letters:
                letters[ch] = 0
            letters[ch] += 1

    return letters


def compute_data(data: dict) -> list:

    if not data:
        raise ValueError('There is no letters.')

    pairs = sorted(data.items(), key=lambda i: (-i[1], i[0]))
    return pairs[:MAX_LETTERS]


def get_graphic_data(tuples: list) -> str:

    graphic = ['Most common letters:', '']

    max_value = tuples[0][1]
    factor = MAX_LETTERS / max_value
    padding = 0

    while max_value > 0:
        padding += 1
        max_value //= 10

    for key, value in tuples:
        graphic.append('{}: {} {}'.format(key,
                                          str(value).rjust(padding),
                                          '#' * (math.ceil(factor * value) or 1)))

    return str.join('\n', graphic)


def solve(text: str):
    print(get_graphic_data(compute_data(collect_data(text))))


if __name__ == '__main__':

    while True:
        try:
            text = input('Please enter some text: ')
            solve(text)
            break
        except ValueError as e:
            print(e)
