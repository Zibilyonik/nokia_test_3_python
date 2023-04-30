def solution(S):
    adjusted_s = ""
    first_half = ""
    second_half = ""
    for char in S:
        if char == "?":
            adjusted_s += "\?"
        else:
            adjusted_s += char
    if S == "" or type(S) != str:
        return "NO"
    if len(S) == 1:
        return S
    print(len(S))
    if len(S) % 2 == 0:
        count = 0
        for char in S:
            if count < len(S) / 2:
                first_half += char
            else:
                second_half += char
            count += 1
    else:
        count = 0
        for char in S:
            if count < (len(S) - 1) / 2:
                first_half += char
            elif count == round(len(S) / 2) - 1:
                pass
            else:
                second_half += char
            count += 1
    print(f'first half: {first_half}')
    print(f'second half : {second_half}')
    for index in range(len(first_half)):
        char = first_half[index]
        reversed_char = second_half[-index - 1]
        if char == "?":
            if reversed_char == char:
                pass
            else:
                first_half = first_half[:index] + reversed_char + first_half[index + 1:]
        else:
            if second_half[len(second_half) - index - 1] == "?":
                second_half = second_half[:len(second_half) - index - 1] + char + second_half[len(second_half) - index:]
            elif reversed_char == char:
                pass
            else:
                return "NO"
    return first_half + second_half