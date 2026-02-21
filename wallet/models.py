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

