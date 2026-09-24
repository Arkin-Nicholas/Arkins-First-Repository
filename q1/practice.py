class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        print(f"❌ {self.owner} has insufficient funds!")
        return False


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float):
        # 1. Using super() to initialize the parent class attributes
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"📈 Applied {self.interest_rate:.1%} interest. New balance: ${self.balance:.2f}")

    def transfer_from(self, source_account, amount: float):
        # 2. Using isinstance() to check if the source is an actual BankAccount
        if not isinstance(source_account, BankAccount):
            print("❌ Transfer failed: Invalid account type!")
            return False

        # Attempt to withdraw from the source and deposit here
        if source_account.withdraw(amount):
            self.deposit(amount)
            print(f"✅ Successfully transferred ${amount:.2f} from {source_account.owner} to {self.owner}.")
            return True
        return False


# --- Running the Code ---

# Creating account instances
checking = BankAccount("Alice", 1000.0)
savings = SavingsAccount("Bob", 5000.0, 0.05)
fake_account = "Not a real account string"

print("--- Step 1: Valid Transfer ---")
# This works because 'checking' is an instance of BankAccount
savings.transfer_from(checking, 200.0)

print("\n--- Step 2: Failed Transfer (Type Security) ---")
# This is blocked by isinstance() before it can cause an error
savings.transfer_from(fake_account, 100.0)

print("\n--- Final Balances ---")
print(f"{checking.owner}'s Balance: ${checking.balance:.2f}")
print(f"{savings.owner}'s Balance: ${savings.balance:.2f}")
