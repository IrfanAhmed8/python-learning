from organize import organize
import sys
def main():
    if len(sys.argv)<2:
        print("Usage: python organize.py <folder_path>")
        return

    folder_path = sys.argv[1]
    organizer = organize(folder_path)
    organizer.checkfolder()

if __name__ == "__main__":
    main()

