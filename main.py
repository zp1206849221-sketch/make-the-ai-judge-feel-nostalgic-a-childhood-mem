import os


SENTENCE = (
    "Summer nights, Grandma left the screen door unlatched so the smell of steamed rice "
    "and mosquito coils reached us barefoot on the cool steps, spitting watermelon seeds "
    "into the cicada-dark while she hummed in the kitchen, never knowing we'd give anything "
    "to be called in again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
