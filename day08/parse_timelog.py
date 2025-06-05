from datetime import datetime

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def minutes_diff(t1, t2):
    return int((t2 - t1).total_seconds() // 60)

def process_log(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Each entry: (time, activity)
    entries = []
    for line in lines:
        time_str, activity = line.split(' ', 1)
        entries.append((parse_time(time_str), activity))

    # Process intervals and accumulate times
    report_lines = []
    activity_totals = {}

    for i in range(len(entries)):
        start_time, activity = entries[i]

        if i < len(entries) - 1:
            end_time = entries[i + 1][0]
        else:
            # Last entry, no end time - skip or handle specially
            break

        # Format interval line
        interval_str = f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} {activity}"
        report_lines.append(interval_str)

        # Calculate minutes spent
        duration = minutes_diff(start_time, end_time)
        if activity != 'End':  # Skip "End" activity in totals
            activity_totals[activity] = activity_totals.get(activity, 0) + duration

    # Write report to output file
    with open(output_path, 'w') as f:
        # Write intervals
        for line in report_lines:
            f.write(line + '\n')

        f.write('\n')

        # Calculate total minutes for all activities
        total_minutes = sum(activity_totals.values())

        # Sort activities alphabetically for summary
        for activity in sorted(activity_totals.keys()):
            mins = activity_totals[activity]
            percent = round((mins / total_minutes) * 100)
            f.write(f"{activity:<25} {mins:4} minutes   {percent:2}%\n")

    print(f"Report created: {output_path}")

if __name__ == "__main__":
    input_file = "timelog.log"
    output_file = "timelog.txt"
    process_log(input_file, output_file)
