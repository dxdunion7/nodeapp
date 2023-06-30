from rest_framework import serializers
from django.db.models import fields
from .models import *

class BitPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BitPay
        fields = '__all__'

class SolanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solana
        fields = '__all__'

class TrustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trust
        fields = '__all__'

class BitPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BitPay
        fields = '__all__'

class MetamaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metamask
        fields = '__all__'

class HuobiWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuobiWallet
        fields = '__all__'

class PhantomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phantom
        fields = '__all__'

class WazirxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wazirx
        fields = '__all__'

class PillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pillar
        fields = '__all__'

class TokenpocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokenpocket
        fields = '__all__'

class AtomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atomic
        fields = '__all__'

class WallethSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walleth
        fields = '__all__'

class AuthereumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authereum
        fields = '__all__'

class EidooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eidoo
        fields = '__all__'

class ZelcoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zelcore
        fields = '__all__'


class NashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nash
        fields = '__all__'

class CoinomiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coinomi
        fields = '__all__'

class GridplusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gridplus
        fields = '__all__'

class CoolWalletSSerializer(serializers.ModelSerializer):
    class Meta:
        model =CoolWalletS
        fields = '__all__'


class AliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alice
        fields = '__all__'

class AlphaWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlphaWallet
        fields = '__all__'


class TokenarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokenary
        fields = '__all__'

class SafepalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safepal
        fields = '__all__'

class EqualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equal
        fields = '__all__'

class InfinitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infinito
        fields = '__all__'


class MathwalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mathwallet
        fields = '__all__'

class MyKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyKey
        fields = '__all__'

class SpatiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spatium
        fields = '__all__'

class WalletioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walletio
        fields = '__all__'

class InfinityWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfinityWallet
        fields = '__all__'

class OwnBitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnBit
        fields = '__all__'

class EasyPocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasyPocket
        fields = '__all__'

class ONTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ONTO
        fields = '__all__'

class BridgeWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridgeWallet
        fields = '__all__'

class SparkPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparkPoint
        fields = '__all__'

class ViaWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViaWallet
        fields = '__all__'

class Coin98Serializer(serializers.ModelSerializer):
    class Meta:
        model = Coin98
        fields = '__all__'

class BitKeepSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitKeep
        fields = '__all__'

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = '__all__'

class SFWTWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = SFWTWallet
        fields = '__all__'

class PeakDefiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakDefi
        fields = '__all__'

class XDCWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = XDCWallet
        fields = '__all__'

class UnstoppableWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnstoppableWallet
        fields = '__all__'

class MEETONESerializer(serializers.ModelSerializer):
    class Meta:
        model = MEETONE
        fields = '__all__'

class DOKWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOKWallet
        fields = '__all__'

class ATWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATWallet
        fields = '__all__'

class MoriXWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoriXWallet
        fields = '__all__'

class MidasWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MidasWallet
        fields = '__all__'

class OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others
        fields = '__all__'