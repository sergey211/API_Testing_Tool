class Endpoint:
    status = None
    response = None
    data = None
    changed_data = None

    def status_code_is_200(self):
        return self.status == 200

    def status_code_is_401(self):
        return self.status == 401

    def status_code_is_404(self):
        return self.status == 404

    def code_is_the_same_as_custom(self):
        dict1 = self.response
        dict2 = self.data
        the_same_items = {k: dict2[k] for k in dict2 if k in dict1 and dict2[k] == dict1[k]}
        return len(the_same_items) == len(self.data)

    def code_is_not_the_same_as_custom(self):
        dict1 = self.response
        dict2 = self.data
        print(type(dict1))
        print(type(dict2))
        print(dict1)
        print(dict2)
        the_same_items = {k: dict2[k] for k in dict2 if k in dict1 and dict2[k] == dict1[k]}
        return len(the_same_items) == 0
