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


#Modulkatalog
def add_modul(self, code: str, credits: int, prerequisites: Optional[Set[str]] = None):
    if code in self._catalog:
        raise ValueError("Modul existiert bereits.")
    self._catalog[code] = Modul(code, credits, prerequisites or set())


#Planung
def plan_modul(self, semester: int, code: str, status: Status = "geplant"): 
    if code not in self._catalog:
        raise KeyError("Modul nicht im Katalog.")
    if self._is_planned(code):
        raise ValueError("Modul bereits geplant.")


    if self._missing_prerequisites(code):
        raise ValueError("Voraussetzungen nicht erfüllt.")


    self._plan.setdefault(semester, {})
    self._plan[semester][code] = status


    if self.semester_credits(semester) > self._max_credits:
        del self._plan[semester][code]
        raise ValueError("Credit-Limit überschritten.")
