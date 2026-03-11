import unittest
from bank_acc import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.akun = BankAccount("DIAN FAJAR", 10000000)
        self.akun2 = BankAccount("FAJRI", 500000)

    def tearDown(self):
        self.akun = None
        self.akun2 = None

    # ======================
    # TEST INISIALISASI
    # ======================

    def test_account_initialization(self):
        self.assertEqual(self.akun.owner, "DIAN FAJAR")
        self.assertEqual(self.akun.get_balance(), 10000000)

    def test_default_balance(self):
        akun = BankAccount("FAJRI")
        self.assertEqual(akun.get_balance(), 0)

    def test_owner_name_type(self):
        self.assertIsInstance(self.akun.owner, str)

    def test_balance_type(self):
        self.assertIsInstance(self.akun.get_balance(), (int, float))

    # ======================
    # TEST DEPOSIT
    # ======================

    def test_deposit_valid_amount(self):
        self.akun.deposit(500000)
        self.assertEqual(self.akun.get_balance(), 10500000)

    def test_deposit_zero(self):
        self.akun.deposit(0)
        self.assertEqual(self.akun.get_balance(), 10000000)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.akun.deposit(-100)

    def test_deposit_invalid_type_string(self):
        with self.assertRaises(TypeError):
            self.akun.deposit("500000")

    def test_deposit_invalid_type_list(self):
        with self.assertRaises(TypeError):
            self.akun.deposit([500000])

    def test_deposit_large_amount(self):
        self.akun.deposit(1000000000)
        self.assertEqual(self.akun.get_balance(), 1010000000)

    # ======================
    # TEST WITHDRAW
    # ======================

    def test_withdraw_valid_amount(self):
        self.akun.withdraw(400000)
        self.assertEqual(self.akun.get_balance(), 9600000)

    def test_withdraw_exact_balance(self):
        self.akun.withdraw(10000000)
        self.assertEqual(self.akun.get_balance(), 0)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.akun.withdraw(20000000)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.akun.withdraw(-50000)

    def test_withdraw_invalid_type_string(self):
        with self.assertRaises(TypeError):
            self.akun.withdraw("200")

    def test_withdraw_invalid_type_none(self):
        with self.assertRaises(TypeError):
            self.akun.withdraw(None)

    # ======================
    # TEST MULTIPLE TRANSACTION
    # ======================

    def test_multiple_transactions(self):
        self.akun.deposit(500000)
        self.akun.withdraw(200000)
        self.akun.deposit(100000)

        self.assertEqual(self.akun.get_balance(), 10400000)

    def test_multiple_withdraw(self):
        self.akun.withdraw(100000)
        self.akun.withdraw(100000)
        self.akun.withdraw(100000)

        self.assertEqual(self.akun.get_balance(), 9700000)

    # ======================
    # TEST AKUN TERPISAH
    # ======================

    def test_accounts_are_independent(self):
        self.akun.deposit(100000)
        self.assertNotEqual(self.akun.get_balance(), self.akun2.get_balance())

    def test_second_account_transaction(self):
        self.akun2.deposit(500000)
        self.assertEqual(self.akun2.get_balance(), 1000000)

    # ======================
    # TEST STATE SETELAH ERROR
    # ======================

    def test_balance_not_changed_after_failed_withdraw(self):
        initial_balance = self.akun.get_balance()

        try:
            self.akun.withdraw(20000000)
        except ValueError:
            pass

        self.assertEqual(self.akun.get_balance(), initial_balance)

    def test_balance_not_changed_after_failed_deposit(self):
        initial_balance = self.akun.get_balance()

        try:
            self.akun.deposit("salah")
        except TypeError:
            pass

        self.assertEqual(self.akun.get_balance(), initial_balance)

    # ======================
    # STRESS TEST
    # ======================

    def test_many_small_deposits(self):
        for _ in range(100):
            self.akun.deposit(1000)

        self.assertEqual(self.akun.get_balance(), 10100000)


if __name__ == "__main__":
    unittest.main(verbosity=2)