# coding: utf-8
import random

UNDEFINED_PLACE = 'undefined_place'

from .environment import RollBackException

class KnowlegeBase(object):

    def __init__(self):
        self.places = {}
        self.persons = {}

    def initialize(self):
        for person_uuid, person in self.persons.items():
            self.places[person['place']]['persons'].append(person_uuid)

    def add_place(self, uuid, external_data={}):
        self.places[uuid] = {'uuid': uuid,
                             'external_data': external_data,
                             'persons': []}

    def add_person(self, uuid, place=UNDEFINED_PLACE, external_data={}):
        self.persons[uuid] = {'uuid': uuid,
                              'external_data': external_data,
                              'place': place}

    def get_random_place(self, exclude=[]):
        choices = [place_uuid for place_uuid in self.places.keys() if place_uuid not in exclude]
        if len(choices) == 0:
            raise RollBackException('can not found suitable place with excludes: %r' % exclude)
        return random.choice(choices)

    def get_random_person(self, place=UNDEFINED_PLACE, exclude=[]):

        exclude = set(exclude)

        choices = [ person_uuid for person_uuid in self.places[place]['persons'] if person_uuid not in exclude]

        if len(choices) == 0:
            raise RollBackException('can not found suitable person for place: %s with excludes: %r' % (place, exclude))

        return random.choice(choices)
