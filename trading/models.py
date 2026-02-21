from django.db import models
from users.models import User

class Trade(models.Model):
    TRADE_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ]
    CRYPTO_CHOICES = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('USDT', 'Tether'),
        ('BNB', 'Binance Coin')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trades')
    crypto_type = models.CharField(max_length=10, choices=CRYPTO_CHOICES)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=20, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.trade_type} {self.crypto_type}"

