from collections import deque

S = input()

q = deque()
st = set()
for i in range(len(S)):
    if S[i] == '(':
        q.append(S[i])
    elif S[i] == ')':
        while True:
            if q[-1] != '(':
                st.remove(q.pop())
            else:
                q.pop()
                break
    else:
        q.append(S[i])
        tmp = len(st)
        st.add(S[i])
        if len(st) == tmp:
            print("No")
            exit()

print("Yes")
