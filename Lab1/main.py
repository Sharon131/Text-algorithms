# za dwa tygodnie ocenianie (natępne laby)
# open file -> encoding dev8
import re
import time
import codecs


def naive(original, pattern):
    s = set()
    for i in range(len(original)-len(pattern)+1):
        if original[i:i+len(pattern)] == pattern:
            s.add(i)
    return s


def create_delta(pattern):
    delta = []

    for q in range(0, len(pattern)+1):
        delta.append({})
        for a in list(set(pattern)):
            k = min(len(pattern)+1, q+2)
            while True:
                k = k-1
                if re.search(f"{pattern[:k]}$", pattern[:q] + a):
                    break
            delta[q][a] = k
    return delta


def machine(original, delta):
    q = 0
    found = set()

    for s in range(0, len(original)):
        q = delta[q].get(original[s], 0)
        if q == (len(delta)-1):
            found.add(s+1-q)

    return found


def prefix_function(pattern):
    pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        pi.append(k)
    return pi


def kmp(text, pi):
    # pi = prefix_function(pattern)
    q = 0
    s = set()
    for i in range(0, len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == len(pattern):
            s.add(i+1-q)
            q = pi[q - 1]
    return s


def test_speed_of_naive(text, pattern):
    start = time.time()
    naive(text, pattern)
    end = time.time()
    return end-start


def test_speed_of_machine(text, pattern):
    start = time.time()
    create_delta(pattern)
    machine(text, delta)
    end = time.time()
    return end - start


def test_speed_of_kmp(text, pattern):
    start = time.time()
    pi = prefix_function(pattern)
    kmp(text, pi)
    end = time.time()
    return end - start


f = codecs.open("1997_714.txt", "r", "utf-8")
directive_content = f.read()
original = "abaabaaaaba"
pattern_eas = "aba"
pattern = "art"
pi = prefix_function(pattern)
pi_eas = prefix_function(pattern_eas)
delta_eas = create_delta(pattern_eas)
delta = create_delta(pattern)

print("Wynik z naiwnego algo: " + str(naive(original, pattern_eas)))
print("Wynik z automatu: " + str(machine(original, delta_eas)))
print("Tabela pi: " + str(pi_eas))
print("Wynik z kmp: " + str(kmp(original, pi_eas)))

print(f"Naive time: {test_speed_of_naive(directive_content, pattern)}")
print(f"Automat time: {test_speed_of_machine(directive_content, pattern)}")
print(f"KMP time: {test_speed_of_kmp(directive_content, pattern)}")

f.close()
