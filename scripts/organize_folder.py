from pathlib import Path
import shutil

DRY_RUN = False


FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Data": {".csv", ".xlsx", ".xls", ".json"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Archives": {".zip", ".rar", ".7z"},
}


def get_category(file_extension: str) -> str:
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category

    return "Others"


def organize_folder(folder_path: str) -> None:
    folder = Path(folder_path)

    if not folder.exists():
        print(f"Folder does not exist: {folder}")
        return

    if not folder.is_dir():
        print(f"This is not a folder: {folder}")
        return

    for item in folder.iterdir():
        if not item.is_file():
            continue

        extension = item.suffix.lower()
        category = get_category(extension)

        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / item.name

        counter = 1

        while destination_file.exists():
            destination_file = (
                destination_folder /
                f"{item.stem}_{counter}{item.suffix}"
            )
            counter += 1

        if DRY_RUN:
            print(f"[DRY RUN] {item.name} → {category}/")
        else:
            shutil.move(str(item), str(destination_file))
            print(f"Moved: {item.name} → {category}/")


folder_path = input("Enter folder path: ").strip()

organize_folder(folder_path)