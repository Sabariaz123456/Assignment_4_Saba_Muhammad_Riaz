import time
import os

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to perform binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0  # To count number of steps

    while left <= right:
        steps += 1
        mid = (left + right) // 2  # Find the middle index

        # Displaying current search range
        print(f"\n🔍 Searching between index {left} and {right}...")
        print(f"🧐 Middle index: {mid}, Middle value: {arr[mid]}")

        if arr[mid] == target:
            print("\n🎯 Target found!")
            print(f"✅ {target} is at index {mid} in {steps} steps.\n")
            return mid

        elif arr[mid] < target:
            print(f"➡️ {target} is greater than {arr[mid]} - Searching Right")
            left = mid + 1  # Move to the right half
        else:
            print(f"⬅️ {target} is smaller than {arr[mid]} - Searching Left")
            right = mid - 1  # Move to the left half

        time.sleep(1)  # Pause for better visibility

    print("\n❌ Target not found!")
    return -1

# Main function to run the project
def main():
    clear_console()
    print("🔢 Welcome to Binary Search Project! 🔍\n")
    
    # Taking sorted list input from user
    try:
        numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
        numbers.sort()  # Ensure the list is sorted
    except ValueError:
        print("❗ Invalid input! Please enter only numbers.")
        return

    target = int(input("\n🎯 Enter the number you want to search: "))

    # Calling binary search function
    binary_search(numbers, target)

    # Asking if user wants to run again
    replay = input("\n🔄 Do you want to search again? (y/n): ").lower()
    if replay == 'y':
        main()
    else:
        print("\n👋 Thanks for using Binary Search Program! Have a great day!")

# Run the program
if __name__ == "__main__":
    main()

