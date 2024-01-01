import calendar

def print_month(jaar, maand):
    print_month_title(jaar, maand)
    print_month_body(jaar, maand)

def print_month_title(jaar, maand):
    print(f"{' '*10}{calendar.month_name[maand]}   {jaar}")
    print("-----------------------------")
    print(" Mon Tue Wed Thu Fri Sat Sun")

def print_month_body(jaar, maand):
    cal = calendar.monthcalendar(jaar, maand)
    for week in cal:
        for day in week:
            if day == 0:
                print("    ", end='')  # Print spaces for days that are part of the previous or next month
            else:
                formatted=f"{day:>4}"
                print(formatted, end='')  # Display the day
        print()  # Move to the next line after printing a week