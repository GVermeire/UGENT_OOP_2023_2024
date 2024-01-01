def display_average_hours(weekly_hours_table):
    averages=[(sum(hours) / len(hours), i + 1) for i, hours in enumerate(weekly_hours_table)]
    averages.sort(reverse=True)
    print("Employee, Average Daily Hours")
    print("---------------------------------")
    for avg, emp_id in averages:
        print(f"Employee{emp_id:2}\t{avg:.2f} hours")