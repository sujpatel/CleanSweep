from scanner import system_scan, junk_finder, duplicate_finder
from cleaner.cleanup import confirm_and_cleanup
from reports.report_generator import generate_report
from database.logger import log_session

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


def main():
    print("Welcome to CleanSweep!\n")

    while True:
        print("\nChoose which actions to perform:")
        print("[1] Scan and clean junk files")
        print("[2] Scan and clean duplicate files")
        print("[3] Generate performance report")
        print("[4] Exit CleanSweep")

        choices = input("Enter options (e.g. 1 2 3): ").split()
        choices = set(choices)

        if '4' in choices:
            print("Exiting CleanSweep.")
            break

        before = system_scan.get_snapshot()
        file_stats = {}

        if '1' in choices:
            print("\nScanning for junk files...")
            junk_files = junk_finder.find_junk()
            print(f"Found {len(junk_files)} potential junk files.")
            if junk_files:
                result = confirm_and_cleanup(junk_files, label="junk")
                if result == 'menu':
                    continue
                if isinstance(result, dict):
                    file_stats['junk'] = result

        if '2' in choices:
            print("\nScanning for duplicate files...")
            duplicates = duplicate_finder.find_duplicates()
            print(f"Found {len(duplicates)} duplicate files.")
            if duplicates:
                result = confirm_and_cleanup(duplicates, label="duplicate")
                if result == 'menu':
                    continue
                if isinstance(result, dict):
                    file_stats['duplicate'] = result

        after = system_scan.get_snapshot()

        if '3' in choices:
            print("\nGenerating performance report...")
            generate_report(before, after)

        print("\nLogging cleanup session to database...")
        log_session(before, after)

        generate_summary(file_stats, before, after)

        again = input("\nReturn to menu? (Y/N): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
