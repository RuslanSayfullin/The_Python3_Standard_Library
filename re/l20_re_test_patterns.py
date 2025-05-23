import re

def test_patterns(text, patterns):
    """Получив исходный текст и список шаблонов в качестве
        аргументов, выполняет поиск всех вхождений каждого шаблона
        в тексте и направляет результаты в стандартный поток вывода
        stdout.
    """
    # Поиск всех вхождений шаблона в тексте и вывод результатов
    for pattern, desc in patterns:
        print("'{}' ({})Xn".format(pattern, desc))
        print(" '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(" {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == '__main__ ':
    test_patterns('abbaaabbbbaaaaa', [('ab', "'a' followedby 'b'"), ])