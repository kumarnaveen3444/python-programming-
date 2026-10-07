total_runs = 0

for ball in range(1, 7):  # 6 balls in an over

    runs = int(input(f"Runs on ball {ball}: "))
    
    total_runs = total_runs + runs

print("Total Runs in Over:", total_runs)
