from rest_framework import serializers

from plate.models import Plate


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'

    def validate_plate(self, plate):
        nums = plate[0] + plate[-2:]
        print('NUMS', nums)
        if not nums.isalpha() or not plate[1:-2].isdigit() or len(plate) != 6:
            raise serializers.ValidationError('неправильно введен номер авто')
        if Plate.objects.filter(plate=plate).exists():
            raise serializers.ValidationError('такой номер уже существует')
        return plate
