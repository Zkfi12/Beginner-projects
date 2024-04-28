from datetime import datetime

current_date = datetime.now()

release_date = datetime(2025, 1, 7)

time_until_release = release_date - current_date

answer_seconds = int(time_until_release.total_seconds())

print("You have", answer_seconds ," seconds left until your out.")


