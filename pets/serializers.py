from rest_framework import serializers
from pets.models import Pet, Sex
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from groups.models import Group
from traits.models import Trait


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Sex.choices,
        default=Sex.DEFAULT,
    )
    traits_count = serializers.SerializerMethodField()

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data: dict) -> Pet:
        group_dict = validated_data.pop("group")
        traits_list = validated_data.pop("traits")

        group_obj, created = Group.objects.get_or_create(
            scientific_name=group_dict["scientific_name"]
        )

        pet_obj = Pet.objects.create(**validated_data, group=group_obj)

        for item in traits_list:
            traits_obj, created = Trait.objects.get_or_create(**item)
            traits_obj.pets.add(pet_obj)

        return pet_obj

    def get_traits_count(self, obj):
        return len(obj.traits.values())

    def update(self, instance: Pet, validated_data: dict):
        group_dict: dict = validated_data.pop("group", None)
        traits_list = validated_data.pop("traits", None)

        if group_dict:
            group_obj, created = Group.objects.get_or_create(
                scientific_name=group_dict["scientific_name"]
            )
            setattr(instance, "group", group_obj)

        if traits_list:
            list_traits = []

            for item in traits_list:
                traits_obj, created = Trait.objects.get_or_create(**item)
                list_traits.append(traits_obj)

            instance.traits.set(list_traits)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
