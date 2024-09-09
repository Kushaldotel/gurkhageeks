from rest_framework import serializers


class ResumeFeedbackSerializer(serializers.Serializer):
    job_description = serializers.CharField()
    resume = serializers.FileField()
    task = serializers.ChoiceField(
        choices=[("review", "Review"), ("match", "percentage match")]
    )
