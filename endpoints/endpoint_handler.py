class Endpoint:
    status = None

    def status_code_is_200(self):
        return self.status == 200

    def status_code_is_401(self):
        return self.status == 401

    def status_code_is_404(self):
        return self.status == 404
