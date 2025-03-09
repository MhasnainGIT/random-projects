import os
import random
from datetime import datetime, timedelta

# Function to run shell commands
def run_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Error executing: {command}")
        exit(1)

# Define the date range
start_date = datetime(2024, 12, 4)
end_date = datetime(2024, 12, 31)

# File to modify
file_name = "Info.txt"

# Ensure the file exists
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("Initial content\n")

# Loop through each day
current_date = start_date
while current_date <= end_date:
    # Random number of commits per day (e.g., 1 to 5)
    num_commits = random.randint(1, 5)
    print(f"\n{num_commits} commits for date: {current_date.strftime('%d-%b-%Y')}")
    
    for i in range(num_commits):
        # Modify the file with a unique message
        commit_msg = f"Commit #{i+1} on {current_date.strftime('%d-%b-%Y')}"
        with open(file_name, "a") as f:
            f.write(f"{commit_msg} - {random.randint(1, 1000)}\n")
        
        # Stage the changes
        run_command(f"git add {file_name}")
        
        # Commit with the specific date
        date_str = current_date.strftime('%Y-%m-%d 12:00:00')
        run_command(f'git commit --date="{date_str}" -m "{commit_msg}"')
        
        print(f"Date: {current_date.strftime('%d-%b-%Y')}, Commit #: {i+1}")
    
    # Move to the next day
    current_date += timedelta(days=1)

# Push to GitHub
print("\nPushing to GitHub...")
run_command("git push origin master")
print("Done!")