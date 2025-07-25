def add_time(start, duration, day=''):
    # Parse start time
    time, meridian = start.split()
    start_hour, start_minute = map(int, time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start to 24-hour time
    if meridian == 'PM' and start_hour != 12:
        start_hour += 12
    elif meridian == 'AM' and start_hour == 12:
        start_hour = 0

    # Add time
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    days_passed = total_hours // 24
    new_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if new_hour_24 == 0:
        new_hour = 12
        period = 'AM'
    elif new_hour_24 < 12:
        new_hour = new_hour_24
        period = 'AM'
    elif new_hour_24 == 12:
        new_hour = 12
        period = 'PM'
    else:
        new_hour = new_hour_24 - 12
        period = 'PM'

    # Format minutes
    new_minute_str = f'{new_minute:02}'

    # Build new time
    new_time = f"{new_hour}:{new_minute_str} {period}"

    # Handle day of the week
    if day:
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = week_days.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = week_days[new_day_index]
        new_time += f", {new_day}"

    # Append day info
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
