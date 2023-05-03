# The story!
story = {
    "start": """
        Luci was once an innocent child, but witnessing the death of his parents at the hands of a gang feud, something inside him snapped.
        He vowed to rid the world of evil no matter what the cost. From this day on, his name would become Lucifer.
    """,
    "middle": """
        Lucifer's methods were unorthodox and often involved breaking the law himself. But he always got results.
        He infiltrated gangs, took down corrupt officials and even went undercover as a hitman to bring down the cartel.
        At this point people would wander if he was more than human.
    """,
    "end": """
        Lucifer's journey took a toll. He had no friends or family and no one to turn to.
        He became the darkness he once hated, what he once fought now consumes him.
        Lucifer went too far, his ethics went haywire and he was ended by those he tried to protect.
        He died alone, a martyr to his own cause. Lucifer's legacy is in the hearts of many, who have been wronged and shunned, those who want to cross the line between good and evil.
    """
}

# Printing the dictionary
print(story)

# Printing the type of dictionary
print(type(story))

# Printing the keys
print(story.keys())

# Printing the values
print(story.values())

# printing the values using the keys
print(story["start"])
print(story["middle"])
print(story["end"])

# Pairing a key to a name
story["hero"] = "Lucifer"