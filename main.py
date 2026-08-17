def coffee_routine(reply=None):
    if reply in ["+", "+1", "要", "對", "👍"]:
        return "☕ Coffee +1"
    elif reply == "pass":
        return "No coffee today. See you tomorrow."
    else:
        return "Humans are not state machines. XD"


if __name__ == "__main__":
    print(coffee_routine("+"))
