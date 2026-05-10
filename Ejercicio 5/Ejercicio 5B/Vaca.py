from abc import Mob

class Vaca(Mob):
    """Mob pasivo, suena 'Muuuu', camina lento."""
    # TODO: implementa hacer_sonido, comportamiento, moverse
    pass
   
    def hacer_sonido(self) -> str:
        return "Moo"
    
    def comportamiento(self) -> str:
        return "Pasivo"
    
    def moverse(self) -> str:
        return "Derecha"