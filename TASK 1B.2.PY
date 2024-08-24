def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
    return [list1 + ["*"] + list2, True]

def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common letters
    result, _ = remove_match_char(list(name1), list(name2))

    # Count the remaining letters
    count = len(result)

    # Relationship outcomes based on FLAMES
    outcomes = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

    # Determine relationship
    while len(outcomes) > 1:
        index = (count % len(outcomes)) - 1
        if index >= 0:
            left = outcomes[:index]
            right = outcomes[index + 1:]
            outcomes = right + left
        else:
            outcomes = outcomes[:len(outcomes) - 1]

    return outcomes[0]

# Example usage
if _name_ == "_main_":
    player1 = input("Enter the first name: ")
    player2 = input("Enter the second name: ")
    relationship_status = flames_game(player1, player2)
    print(f"The relationship between {player1} and {player2} is: {relationship_status}")