from dataclasses import dataclass, field
from typing import List


@dataclass
class Component:

    name: str
    children: List['Component'] = field(default_factory=list)
    level: int = 0

    def add_children(self, c: 'Component') -> 'Component':
        self.children.append(c)
        return self

    def has_children(self) -> bool:
        # return len(self.children) > 0
        return bool(self.children)