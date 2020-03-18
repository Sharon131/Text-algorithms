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


def machine(original, pattern):
    q = 0
    delta = create_delta(pattern)
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


def kmp(text, pattern):
    pi = prefix_function(pattern)
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
    machine(text, pattern)
    end = time.time()
    return end - start


def test_speed_of_kmp(text, pattern):
    start = time.time()
    kmp(text, pattern)
    end = time.time()
    return end - start


def test_speed_of_creating_delta(pattern):
    start = time.time()
    create_delta(pattern)
    end = time.time()
    return end-start


def test_speed_of_creating_pi(pattern):
    start = time.time()
    prefix_function(pattern)
    end = time.time()
    return end-start


original = "abaabaaaaba"
pattern_eas = "aba"
pi_eas = prefix_function(pattern_eas)

print("Wynik z naiwnego algo: " + str(naive(original, pattern_eas)))
print("Wynik z automatu: " + str(machine(original, pattern_eas)))
print("Wynik z kmp: " + str(kmp(original, pattern_eas)))

# Zadanie 3
f = codecs.open("1997_714.txt", "r", "utf-8")
directive_content = f.read()
pattern = "art"

print("Szukanie wzoru art w ustawie:")
naive_res = naive(directive_content, pattern)
machine_res = machine(directive_content, pattern)
kmp_res = kmp(directive_content, pattern)

print("Algorytm naiwny: " + str(naive_res))
print("Algorytm z automatem: " + str(machine_res))
print("Algorytm kmp: " + str(kmp_res))

f.close()
# Zadanie 4
print("Czasy działania wyszukiwania art w ustawie:")
print("Algorytm naiwny: " + str(test_speed_of_naive(directive_content, pattern)))
print("Algorytm z automatem: " + str(test_speed_of_machine(directive_content, pattern)))
print("Algorytm kmp: " + str(test_speed_of_kmp(directive_content, pattern)))

# Zadanie 5
f = codecs.open("wikipedia-tail-kruszwil.txt", "r", "utf-8")
wiki_content = f.read()

pattern = "kruszwil"
print("Czasy działania wyszukiwania kruszwil w wiki:")
print("Algorytm naiwny: " + str(test_speed_of_naive(wiki_content, pattern)))
print("Algorytm z automatem: " + str(test_speed_of_machine(wiki_content, pattern)))
print("Algorytm kmp: " + str(test_speed_of_kmp(wiki_content, pattern)))

f.close()

# Zadanie 6
text = directive_content
pattern = "ryczałt"
print("Czasy działania wyszukiwania " + str(pattern) + " w dyrektywie:")
print("Algorytm naiwny: " + str(test_speed_of_naive(text, pattern)))
print("Algorytm z automatem: " + str(test_speed_of_machine(text, pattern)))
print("Algorytm kmp: " + str(test_speed_of_kmp(text, pattern)))
print("Liczba znalezionych wzorców: " + str(len(kmp(text, pattern))))

# Zadanie 7

pattern = "ABCD EFGH IJKL MNOP RSTV UWXY Z ABCD EFGH IJKL MNOP RSTV UWXY Z"
print("Czasy przygotowania dla wzorca " + str(pattern) + ":")
print("Algorytm z automatem: " + str(test_speed_of_creating_delta(pattern)))
print("Algorytm kmp: " + str(test_speed_of_creating_pi(pattern)))
