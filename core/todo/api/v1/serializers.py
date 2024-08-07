from rest_framework import serializers
from todo.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
        read_only_fields = ["user"]
    def to_representation(self, obj):
        # remove user id when showing data
        ret = super(TaskSerializer, self).to_representation(obj)
        ret.pop("user",None)

        return ret 
