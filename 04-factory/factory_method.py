from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

class PersonalSection(Section):
    def __repr__(self):
        return 'Personal Section'

class AlbumSection(Section):
    def __repr__(self):
        return 'Album Section'

class ProjectSection(Section):
    def __repr__(self):
        return 'Project Section'

class PublishSection(Section):
    def __repr__(self):
        return 'Publish Section'

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)

class Linkedin(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())
        self.add_sections(ProjectSection())

class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())

if __name__ == '__main__':
    profile_type = input('Which Profile you\'d like to create? [LinkedIn or Facebook]')
    profile = eval(profile_type)()
    print('Creating Profile..', type(profile).__name__)
    print('Profile has sections --', profile.get_sections())