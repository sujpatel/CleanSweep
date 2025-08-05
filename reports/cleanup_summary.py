def generate_summary(file_stats, before, after):
    print("\n🧾 Cleanup Summary:")
    print("-" * 30)

    if file_stats:
        for label, stats in file_stats.items():
            print(f"{label.capitalize()} Files Deleted: {stats['count']}")
            print(f"Space Freed from {label}: {stats['freed'] / (1024 * 1024):.2f} MB\n")

    print(f"CPU Usage: {before['cpu_percent']}% → {after['cpu_percent']}%")
    print(f"RAM Used: {before['memory'] / 1e9:.2f} GB → {after['memory'] / 1e9:.2f} GB")
    print(f"Disk Used: {before['disk'] / 1e9:.2f} GB → {after['disk'] / 1e9:.2f} GB")
