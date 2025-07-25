import math

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total_spent = sum(cat.total_spent for cat in categories)
    percentages = []

    for cat in categories:
        percent = (cat.total_spent / total_spent) * 100
        percentages.append(math.floor(percent / 10) * 10)

    # Build the chart lines from 100 to 0
    chart_lines = ""
    for i in range(100, -1, -10):
        chart_lines += f"{i:>3}|"
        for p in percentages:
            chart_lines += " o " if p >= i else "   "
        chart_lines += " \n"

    # Separator line
    separator = "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build names vertically
    max_name_len = max(len(cat.name) for cat in categories)
    name_lines = ""
    for i in range(max_name_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i != max_name_len - 1:
            line += "\n"
        name_lines += line

    return title + chart_lines + separator + name_lines
