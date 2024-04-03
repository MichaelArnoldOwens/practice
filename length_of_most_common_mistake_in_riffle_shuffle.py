'''
❓ PROMPT
You're practicing the riffle shuffle in cardistry (https://youtube.com/shorts/NFnJoWcaL_0). You start with the red cards in one hand and black cards in the other and try to interweave them perfectly, meaning the colors alternate every card once you merge them into a single deck.

You build a machine that accepts a deck of cards to automatically determine the length of your most common mistake after the merge. The most common mistake can be identified by one that is not alternating from the opposite color. For example, "B, R, B, R" would be a perfectly alternating sequence, but there is one mistake in "B, B, R, B". If there are no mistakes, then return 0.

Example(s)
Given the shuffled deck: ["R", "R", "R", "B", "B", "R", "R", "R", "R", "B", "R", "B", "B", "B"]

The following sequences of consecutive cards of the same color:

"R", "R", "R" - Length 3
"R", "R", "R", "R" - Length 4
"B", "B", "B" - Length 3

Returns 3 because it's the most "common" mistake, occurring twice.
'''

# sequence = ["R", "R", "R", "B", "B", "R", "R", "R", "R", "B", "R", "B", "B", "B"]
sequence = ['B', 'B', 'R', 'R', 'B', 'R', 'R', 'R', 'B']
def check_rifle_shuffle_longest(seq):
    longest = 0
    curr_longest = 0
    prev_color = seq[0]

    for idx in range(1, len(seq)):
        if seq[idx] == prev_color:
            curr_longest += 1
            longest = max(longest, curr_longest)
        else:
            curr_longest = 1
            prev_color = seq[idx]
    return longest


# print(check_rifle_shuffle_longest(sequence))

def check_rifle_shuffle_frequent(seq):
    count_dict = {}
    curr_longest = 1
    prev_color = seq[0]

    for idx in range(1, len(seq)):
        if seq[idx] == prev_color:
            curr_longest += 1
        elif curr_longest >= 2:
            dict_key = str(curr_longest)
            if dict_key in count_dict:
                count_dict[dict_key] += 1
            else:
                count_dict[dict_key] = 1

            curr_longest = 1
        prev_color = seq[idx]
    print(curr_longest)
    print(count_dict)
    if curr_longest >= 2:
        dict_key = str(curr_longest)
        if dict_key in count_dict:
            count_dict[dict_key] += 1
        else:
            count_dict[dict_key] = 1
    max_freq = float('-inf')
    result = None
    for k in count_dict:
        if count_dict[k] > max_freq:
            max_freq = count_dict[k]
            result = k


    return result


print('expect output to be 3 => ', check_rifle_shuffle_frequent(sequence))
