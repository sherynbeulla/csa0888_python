def denomination_program(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
    notes_count = {}

    for denomination in denominations:
        if amount >= denomination:
            notes = amount // denomination
            notes_count[denomination] = notes
            amount -= notes * denomination
    return notes_count

if __name__ == "__main__":
    try:
        rupees = int(input("Enter the amount in rupees: "))
        notes = denomination_program(rupees)
        print("Denominations needed:")
        for denomination, count in notes.items():
            print(f"{count} notes of {denomination} rupees")
    except ValueError:
        print("Invalid input. Please enter a valid amount in rupees.")
