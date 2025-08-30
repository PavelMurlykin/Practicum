from __future__ import annotations
from typing import Optional


class Spaceman:

    def __init__(
            self,
            name: str,
            space_experience: int,
            father: Optional[Spaceman] = None,
            mother: Optional[Spaceman] = None,
    ):
        self.name = name
        self.space_experience = space_experience
        self.father = father
        self.mother = mother


def count_dynasty_experience(spaceman: Spaceman) -> int:
    total_experience = spaceman.space_experience

    if spaceman.father is not None:
        total_experience += count_dynasty_experience(spaceman.father)

    if spaceman.mother is not None:
        total_experience += count_dynasty_experience(spaceman.mother)

    return total_experience


yu_a_tatarin = Spaceman(
    name='Юрий Алексеевич Татарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Татарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)
result = count_dynasty_experience(yu_a_tatarin)
print(result)