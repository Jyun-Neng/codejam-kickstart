def solve(N, words, S):
    cnt = 0
    for word in words:
        freq_word = [0 for i in range(26)]
        freq_s = [0 for i in range(26)]
        word_len = len(word)
        for i in range(1, word_len - 1):
            freq_word[ord(word[i]) - 97] += 1
            freq_s[ord(S[i]) - 97] += 1
        for i in range(N - word_len + 1):
            if i > 0:
                freq_s[ord(S[i]) - 97] -= 1
                freq_s[ord(S[i + word_len - 2]) - 97] += 1
            if word[0] == S[i] and word[-1] == S[i + word_len - 1]:
                if freq_word == freq_s:
                    cnt += 1
                    break
    return cnt

f = open('C-large-practice.in.txt', 'r')
sol = open('output.txt', 'w')
t = int(f.readline())
for test in range(1, t + 1):
    L = int(f.readline())
    words = f.readline().strip('\n').split(' ')
    S1, S2, N, A, B, C, D = f.readline().split(' ')
    N, A, B, C, D = int(N), int(A), int(B), int(C), int(D)
    x1, x2 = ord(S1), ord(S2)
    S = [S1, S2]
    for i in range(3, N + 1):
        x1, x2 = x2, (A * x2 + B * x1 + C) % D
        S.append(chr(97 + x2 % 26))
    cnt = solve(N, words, S)    
    sol.write("Case #" + str(test) + ": " + str(cnt) + "\n")
