from .models import Result

class ResultRepository:
    def create(self, *, user_id, value, category, timestamp, ip, attempts=1):
        return Result.objects.create(
            user_id=user_id, value=value, category=category,
            timestamp=timestamp, ip=ip, attempts=attempts
        )

    def list_all(self):
        return Result.objects.all()

    def list_bad(self):
        return Result.objects.filter(category='bad')

    def save(self, instance: Result):
        instance.save()
        return instance

    def delete(self, instance: Result):
        instance.delete()
    
    def count(self) -> int:
        return Result.objects.count()

    def delete_all(self) -> int:
        deleted, _ = Result.objects.all().delete()
        return deleted