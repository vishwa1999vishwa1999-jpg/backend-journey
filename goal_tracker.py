# Day 1: Personal goal tracker
# Track my daily backend learning hours

def save_hours(hours):
    """Save today's hours to file"""
    with open('learning_log.txt', 'a') as file:
        file.write(f"{hours}\n")
    print(f"✅ Logged {hours} hours today!")

    if (f"{hours}\n") >= "4":
        print("🔥 Crushing it!")
    elif (f"{hours}\n") >= "2":
        print("💪 Solid work!")
    else:
        print("😔 Not doing great!!")        
    
def get_stats():
    """Calculate total hours and days practiced"""
    try:
        with open('learning_log.txt','r') as file:
            hours_list = [float(line.strip()) for line in file if line.strip()]

        total_hours = sum(hours_list)
        days_practiced = len(hours_list)
        avg_hours = total_hours / days_practiced if days_practiced > 0 else 0

        print("\n📊 YOUR PROGRESS:")
        print(f"Total hours: {total_hours}")
        print(f"Days practiced: {days_practiced}") 
        print(f"Average hours/day: {avg_hours:.2f}")
        print(f"Goal: 1,460 hours in 365 days")
        print(f"Progress: {(total_hours/1460)*100:.1f}% complete")

    except FileNotFoundError:
        print("No data yet. Start logging hours!")

def main():
    print("🎯 BACKEND LEARNING TRACKER") 
    print("1. Log today's hours")
    print("2. View stats") 
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        hours = float(input("Hours studied today: "))
        save_hours(hours)
    elif choice == "2":
        get_stats()
    else:
        print("Invalid choice!")   

if __name__ == "__main__":
    main()                