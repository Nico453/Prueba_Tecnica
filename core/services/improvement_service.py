class ImprovementService:
    def __init__(self, api_client, repo):
        self.api = api_client
        self.repo = repo

    def sweep_until_no_bad(self):
        sweeps = 0
        total_calls = 0
        while True:
            bad_items = list(self.repo.list_bad())
            if not bad_items:
                break
            sweeps += 1
            for r in bad_items:
                d = self.api.fetch()
                total_calls += 1
                if d['category'] in ('medium','good'):
                    r.value = d['value']
                    r.category = d['category']
                    r.timestamp = d['timestamp']
                    r.ip = d['ip']
                    r.attempts += 1
                    self.repo.save(r)
        return {"sweeps": sweeps, "improvement_calls": total_calls}
