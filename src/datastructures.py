"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id': self._generate_id(),
                          'first_name': 'John',
                          'last_name': self.last_name,
                          'age': 33,
                          'lucky_numbers': [7, 13, 22]},
                         {'id': self._generate_id(),
                          'first_name': 'Jane',
                          'last_name': self.last_name,
                          'age': 35,
                          'lucky_numbers': [10, 14, 3]},
                         {'id': self._generate_id(),
                          'first_name': 'Jimmy',
                          'last_name': self.last_name,
                          'age': 5,
                          'lucky_numbers': [1]}]

    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        print(member)
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        return id

    def get_member(self, id):
        
        for row in self._members:
            if row['id'] == id:
                return row
        
        result = [row for row in self._members if row['id'] == id]
        return result[0] if result else None

    def get_all_members(self):
        return self._members