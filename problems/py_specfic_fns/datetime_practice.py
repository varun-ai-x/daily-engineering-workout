"""
Docstring for problems.py_specfic_fns.datetime_practice

datetime.now()
datetime.strptime() -> String to Object
datetime.strftime() -> Object to String
timedelta(days=1) -> Add or Subtract datetimes
time_to_minutes(t: time) -> t.hour * 60 + t.minute
time.time()
"""



"""
Given a date string in format "2025-02-17 14:30:00", 
convert it to:
1. A datetime object
2. Format: "February 17, 2025 at 2:30 PM"
3. Format: "02/17/2025"
4. Format: "Monday, Feb 17"
"""
from datetime import datetime, timedelta

def format_datetime(date_string: str) -> dict:
    """
    Args:
        date_string: "2025-02-17 14:30:00"
    
    Returns:
        {
            "datetime_obj": datetime object,
            "readable": "February 17, 2025 at 2:30 PM",
            "short": "02/17/2025",
            "day_name": "Monday, Feb 17"
        }
    """
    dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    return {
        "datetime_obj": dt,
        "readable": dt.strftime("%B %d, %Y at %-I:%M %p"),
        "short": dt.strftime("%m/%d/%Y"),
        "day_name": dt.strftime("%A, %b %d")  
    }


"""
Given a meeting start time and duration, calculate:
1. End time
2. What time is 30 minutes before the meeting?
3. What time is 2 hours after the meeting?
4. How many minutes is the meeting?
"""

def calculate_meeting_times(start_str: str, duration_minutes: int) -> dict:
    """
    Args:
        start_str: "2025-02-17 14:30:00"
        duration_minutes: 90
    
    Returns:
        {
            "start": datetime object,
            "end": datetime object,
            "reminder_time": datetime (30 min before),
            "followup_time": datetime (2 hours after end),
            "duration_minutes": int
        }
    """
    dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    return {
        "start": dt,
        "end": dt + timedelta(minutes=duration_minutes),
        "reminder_time": dt - timedelta(minutes=30),
        "followup_time": dt + timedelta(minutes=duration_minutes) + timedelta(hours=2),
        "duration_minutes": duration_minutes
    }

# print(calculate_meeting_times("2025-02-17 14:30:00", 90))

"""
Given two datetime strings, determine:
1. Which one is earlier?
2. How many hours apart are they?
3. Are they on the same day?
4. Are they within 1 hour of each other?
"""

def compare_times(time1_str: str, time2_str: str) -> dict:
    """
    Args:
        time1_str: "2025-02-17 14:30:00"
        time2_str: "2025-02-17 16:45:00"
    
    Returns:
        {
            "earlier": datetime object (the earlier one),
            "hours_apart": float,
            "same_day": bool,
            "within_1_hour": bool
        }
    """
    time_1_dt = datetime.strptime(time1_str, "%Y-%m-%d %H:%M:%S")
    time_2_dt = datetime.strptime(time2_str, "%Y-%m-%d %H:%M:%S")

    delta = abs(time_1_dt - time_2_dt)
    hours_diff = delta.total_seconds() / 3600
    # print(type(delta))

    # print(hours_diff)
    # print(type(hours_diff))



compare_times("2025-02-17 14:30:00", "2025-02-17 16:45:00")



"""
Given a list of busy time intervals, find all gaps.

Example:
Work hours: 9 AM - 6 PM
Busy: [9-10], [11-12], [14-16]
Gaps: [10-11], [12-14], [16-18]

1. Sort all the busy intervals by the start time
2. Use current_time to increase the time
3. Check for time between last busy block and end of day

"""

def find_gaps(busy_intervals, 
              work_start: datetime, 
              work_end: datetime):
    """
    Find all gaps between busy intervals
    
    Args:
        busy_intervals: List of (start, end) tuples
        work_start: Start of work day
        work_end: End of work day
    
    Returns:
        List of (gap_start, gap_end) tuples
    """
    current_time = work_start
    gaps = []

    for busy_start, busy_end in sorted(busy_intervals):        
        if busy_start > current_time:
            gaps.append((current_time, busy_start))

        current_time = max(current_time, busy_end)
    
    if current_time < work_end:
        gaps.append((current_time, work_end))

    return gaps


busy = [
    (datetime(2025, 2, 17, 9, 0), datetime(2025, 2, 17, 10, 0)),   # 9-10
    (datetime(2025, 2, 17, 11, 0), datetime(2025, 2, 17, 12, 0)),  # 11-12
    (datetime(2025, 2, 17, 14, 0), datetime(2025, 2, 17, 16, 0)),  # 14-16
]

work_start = datetime(2025, 2, 17, 9, 0)
work_end = datetime(2025, 2, 17, 18, 0)

# print(find_gaps(busy, work_start, work_end))




"""
Given overlapping intervals, merge them.

Example:
Input:  [9-11], [10-12], [14-16], [15-17]
Output: [9-12], [14-17]

This is used to combine busy times from multiple people.

- Merge any times which are overlapping
- Compare the start time of the current interval with the end time of the previous interval

"""

def merge_intervals(intervals):
    """
    Merge overlapping intervals
    
    Args:
        intervals: List of (start, end) tuples (may be unsorted)
    
    Returns:
        List of merged (start, end) tuples (sorted)
    """
    intervals.sort()
    merged = [intervals[0]]    
    for interval in intervals:        
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)        
    return merged
        
intervals = [[9,11], [10,12], [14,16], [15,17]]

print(merge_intervals(intervals))
        

"""
FINAL BOSS: Build a complete availability finder

Given a person's busy schedule, find the first available gap
that fits a required duration.

This combines ALL previous skills:
- Date ranges
- Time conversion
- Overlap detection
- Merging intervals
- Finding gaps


- Need to check if the duration is present inside the gaps
- 

To find the first available slot

- For each user, 
    - sort the BusySlots
    - merge any overlapping intervals
    - find available gaps

"""


"""
To find gaps in between the work_start and work_end -> 9 AM and 6 PM
- busy_intervals = [[9,11], [12,4]] -> [[11,12], [4,6]]

- Use current_time as a pointer to calculate the gaps
- Initialize gaps = [], Initialize current_time to work_start
- Now iterate through the intervals,
    - If busy_start is greater than the current_time - then, append [current_time, busy_start]
    - Else, Increment current_time = max(current_time, busy_end)
    - if current_time < work_end - then, append to gaps

"""

def find_gaps(busy_intervals, work_start, work_end):
    current_time = work_start
    gaps = []

    for busy_start, busy_end in busy_intervals:
        if busy_start > current_time:
            gaps.append([current_time, busy_start])

        current_time = max(current_time, busy_end)

    if current_time < work_end:
        gaps.append([current_time, work_end])

    return gaps        



"""
Merge Overlapping Intervals

ip: [[9,11], [12,14], [13,17]] -> [[9,11], [12,17]]

- Sort the intervals
- Use a stack to store the previous interval
- Now compare the previous interval (stack[-1][1]) with the curr_interval (interval[0])
    - If, stack[-1][1] > interval[0] - then, stack[1] = max(stack[-1][1], interval[1])
    - Else, do nothing and append the value to stack


"""

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for interval in intervals:
        if merged[-1][1] > interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


"""
To find the first available slot

- For each user, 
    - sort the BusySlots
    - merge any overlapping intervals
    - find available gaps


# 1. Merge the busy blocks (Clean the "rocks" in the bucket)
# 2. Step through each day in the search range
# 3. Use find_gaps to get all free windows today    

"""


def find_first_available_slot(
    busy_intervals: List[Tuple[datetime, datetime]],
    duration_minutes: int,
    search_start: datetime,
    search_end: datetime,
    work_start: time = time(9, 0),
    work_end: time = time(18, 0)
) -> Optional[Tuple[datetime, datetime]]:
    """
    Find first available time slot
    
    Args:
        busy_intervals: Person's busy times
        duration_minutes: How long we need
        search_start: Start searching from this datetime
        search_end: Stop searching at this datetime
        work_start: Work day starts (default 9 AM)
        work_end: Work day ends (default 6 PM)
    
    Returns:
        (slot_start, slot_end) or None if no availability
    """
    pass



    

