
import os


def confirm_and_cleanup(file_list, label):
    total_freed = 0
    deleted_count = 0

    for f in file_list:
        try:
            size = os.path.getsize(f)
            prompt = f"\nDo you want to delete this {label} file?\n{f}\nSize: {size / (1024 * 1024):.2f} MB\n(Y/N or M to return to menu): "
        except Exception:
            size = 0
            prompt = f"\nDo you want to delete this {label} file?\n{f}\nSize: unknown\n(Y/N or M to return to menu): "

        response = input(prompt).strip().lower()
        if response in ['m', 'menu']:
            print("Returning to main menu...")
            return 'menu'

        elif response in ['y', 'yes']:
            try:
                os.remove(f)
                deleted_count += 1
                total_freed += size
                print(f"Deleted: {f}")
            except Exception as e:
                print(f"Failed to delete {f}: {e}")
        else:
            print("Skipped.")

    return {
        "count": deleted_count,
        "freed": total_freed 
    }
