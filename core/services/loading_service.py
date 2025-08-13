from django.db import transaction

class LoadingService:
    def __init__(self, api_client, repo):
        self.api = api_client
        self.repo = repo

    @transaction.atomic
    def initial_load(self, n: int = 100, auto_reset: bool = True):
        
        reset_performed = False
        if auto_reset and self.repo.count() > 0:
            self.repo.delete_all()
            reset_performed = True

        bad = med = good = 0
        for _ in range(n):
            d = self.api.fetch()
            self.repo.create(**d)
            c = d['category']
            if c == 'bad': bad += 1
            elif c == 'medium': med += 1
            else: good += 1

        return bad, med, good, reset_performed
