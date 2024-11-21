def month_conversions():
    while True:
        answer = input("Enter a month's abbreviation (e.g., Jan, Feb): ").strip().capitalize()

        month_dict = {
            'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
            'Apr': 'April', 'May': 'May', 'Jun': 'June',
            'Jul': 'July', 'Aug': 'August', 'Sep': 'September',
            'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
        }

        print(month_dict.get(answer, 'Invalid abbreviation. Please try again.'))

        retry = input('Try another month? [y/n]: ').lower()
        if retry == 'y':
            continue
        elif retry == 'n':
            break
        else:
            print("Please enter 'y' or 'n'")
