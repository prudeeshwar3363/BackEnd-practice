# Custom exception for handling specific banking errors
class InsufficientBalanceError(Exception):
    """Custom exception for when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    """A secure bank account with robust error handling."""
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        # Using a private attribute to demonstrate encapsulation
        self.__balance = initial_balance

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        """Withdraws a positive amount, checking for sufficient funds."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        else:
            if amount > self.__balance:
                raise InsufficientBalanceError("Insufficient funds to complete the withdrawal.")
            else:
                self.__balance -= amount

    def get_balance(self):
        """Returns the current account balance."""
        return self.__balance


def main():
    """Main function to run the interactive ATM system."""
    account = None
    try:
        # --- Initial Account Setup ---
        while True:
            try:
                initial_balance = float(input("Enter your initial balance: "))
                account = BankAccount(initial_balance)
                print(f"Account created successfully with a balance of ${account.get_balance()}.")
                break  # Exit setup loop on success
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid positive number.")

        # --- Main ATM Interactive Loop ---
        while True:
            print("\n" + "="*20)
            print("      ATM MENU")
            print("="*20)
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Exit")
            print("="*20)

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                try:
                    amount_str = input("Enter amount to deposit: ")
                    amount = float(amount_str)
                    account.deposit(amount)
                except ValueError as e:
                    print(f"Error: Invalid amount. {e}")

            elif choice == '2':
                try:
                    amount_str = input("Enter amount to withdraw: ")
                    amount = float(amount_str)
                    account.withdraw(amount)
                except ValueError as e: # Catches invalid number or negative amount
                    print(f"Error: {e}")
                except InsufficientBalanceError as e: # Catches the custom exception
                    print(f"Transaction Failed: {e}")

            elif choice == '3':
                balance = account.get_balance()
                print(f"Your current account balance is: ${balance:,.2f}")

            elif choice == '4':
                break

            else:
                print("Invalid choice. Please select an option from 1 to 4.")

    except Exception as e:
        # This is the catch-all for any unexpected errors during the program's lifecycle
        print(f"\nAn unexpected system error occurred: {e}")
        print("The ATM is shutting down for safety.")
    finally:
        # The 'finally' block ensures this message is always displayed upon exit
        print("\n--- Session Ended ---\nThank you for using the ATM. Have a great day!")


if __name__ == "__main__":
    main()