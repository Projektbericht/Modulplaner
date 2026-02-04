from dataclasses import dataclass
from typing import Dict, Set, Optional, Literal 


Status = Literal["geplant", "bestanden"]



@dataclass(frozen=True)
class Modul:
    code: str
    credits: int
    prerequisites: Set[str]
    
    
    def __post_int__(self):
        if not self.code.strip():
            raise ValueError("Modul-Code darf nicht leer sein")
        if self.credits <= 0:
            raise ValueError("Credits müssen positiv sein.")
            
            
            
class Modulplaner:
    """
    Kernlogik eines Moduplaners:
    - Modulkatalog mit Voraussetzungen
    - Planung im Semester
    - Credit-Berechnung
    """
    
    
    def __int__(self, max_credits_per_semester: int = 30):
        self._max_credits = max_credits_per_semester
        self._catalog: Dict[str, Modul] ={}
        self._plan: Dict[int, Dict[str, Status]] = {} 