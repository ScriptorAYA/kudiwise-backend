from django.db import models
from users.models import User

class Wallet(models.Model):
    CRYPTO_CHOICES = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('USDT', 'Tether'),
        ('BNB', 'Binance Coin')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallets')
    crypto_type = models.CharField(max_length=10, choices=CRYPTO_CHOICES)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0.0)

    def __str__(self):
        return f"{self.user.username} - {self.crypto_type}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer')
    ]
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=20, default='pending')
    tx_reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username} - {self.transaction_type} - {self.amount}"

