def main():
    database = []
    while True:
        try:
            # asking user what they want to do
            print("Please Choose between these three options!")
            print("1. Add to List")
            print("2. See List")
            print("3. Stop")

            choice = int(input("Enter your choice here: "))
            if choice == 1:
                adding = input("Add: ")
                database.append(adding)
            elif choice == 2:
                for index in range(len(database)):
                    print(f"{index + 1}. {database[index]}")
                try:
                    whatnext = int(
                        input(
                            "Press 0 to continue; 1 to delete from list; 3 to update the list: "
                        )
                    )
                except ValueError:
                    print("Please Enter Correct type")

                if whatnext == 1:
                    print("Give Index Number of the todo list you want to delete.")
                    try:
                        to_delete = int(input("index number: "))
                    except ValueError:
                        input("Please Provide number next time...")

                    about_to_delete = to_delete - 1
                    try:
                        database.pop(about_to_delete)
                        input("Deleted Succesfully! Press Enter to Continue!")
                    except IndexError:
                        print("Cannot Delete the item. out of range!")

            elif choice == 3:
                break
        except ValueError:
            print("Please Provide Valid Input!")
        except:  # noqa: E722
            print("Something went wrong!")


if __name__ == "__main__":
    main()
