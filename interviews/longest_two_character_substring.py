def longest_two_char_substring(s):
    if len(s) == 0:
        return 0
    max_counter = float('-inf')
    counter = 1
    char_idx_dict = {f'{s[0]}': 0}

    char_set = set([s[0]])
    left, right = 0, 1

    while right < len(s): # might be off by one
        next_char = s[right]
        if next_char in char_idx_dict:
            counter += 1
            right += 1
            char_idx_dict[next_char] = right
        elif len(char_set) < 2:  # accaaad
            char_set.add(next_char)
            counter += 1
            right += 1
            char_idx_dict[next_char] = right
        else:

            char_to_drop = get_other_char(char_set, s[right])
            new_left_idx = char_idx_dict[char_to_drop] + 1
            char_set.remove(char_to_drop)
            max_counter = max(max_counter, right + 1- left)
            counter -= new_left_idx - left
            left = new_left_idx
            char_set.add(next_char)
            counter += 1
            right += 1

    return max_counter