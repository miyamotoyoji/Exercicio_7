from dataclasses import dataclass


@dataclass(frozen=True)
class Cliente:
    nome: str