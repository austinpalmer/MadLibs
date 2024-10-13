def main():
    print("Welcome to Madlibs.py. A program that allows you to play with madlibs")
    handle_input()


def get_story(story_type: int, noun1: str, verb1: str, noun2: str, verb2: str):
    if story_type == 1:
        story = (f"John walked into a bar and saw {noun1}. "
                 f"When John saw {noun1} he {verb1} to {noun1}. "
                 f"John then asked \"Hey {noun1}, have you seen a {noun2} recently?\" "
                 f"{noun1} {verb2} away")
    elif story_type == 2:
        story = (f"Last summer, I went to the beach with my {noun1} and my {noun2}. "
                 f"We {verb1} in the water and {verb2} sandcastles all day. It was a perfect day!")
    elif story_type == 3:
        story = (f"Once upon a time, a brave {noun1} and a clever {noun2} {verb1} through the enchanted forest. "
                 f"They {verb2} many magical creatures along the way. Their adventure was unforgettable!")
    elif story_type == 4:
        story = (f"At my birthday party, my {noun1} and I had so much fun! We {verb1} games "
                 f"{verb2} cake. Everyone enjoyed the celebration, especially my {noun2}!")
    return story


def handle_input():
    print("Story Options:")
    print("1. Bar Story")
    print("2. Beach Trip")
    print("3. Great Adventure")
    print("4. Birthday Party")
    try:
        story_selection = int(input("Enter the number of the story you would like to use: "))
        noun1 = input("Enter a noun: ")
        verb1 = input("Enter a verb (past-tense): ")
        noun2 = input("Enter another noun: ")
        verb2 = input("Enter another verb (past-tense): ")
    except ValueError:
        print("Invalid input. Please try again.")

    print(get_story(story_selection, noun1, verb1, noun2, verb2))


if __name__ == "__main__":
    main()
