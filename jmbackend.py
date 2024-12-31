class Province:
    def __init__(self, name, ptype, isSupply, connections):
        self.name = name
        self.ptype = ptype
        self.isSupply = isSupply
        self.connections = connections

def create_provinces():
    return [
        Province("ADR", "water", False, ["ALB", "APU", "ION", "TRI", "VEN"]),
        Province("AEG", "water", False, ["BUL/SC", "CON", "EAS", "GRE", "ION", "SMY"]),
        Province("ALB", "coast", False, ["ADR", "GRE", "ION", "SER", "TRI"]),
        Province("ANK", "coast", True, ["ARM", "BLA", "CON", "SMY"]),
        Province("APU", "coast", False, ["ADR", "ION", "NAP", "ROM", "VEN"]),
        Province("ARM", "coast", False, ["ANK", "BLA", "SEV", "SMY", "SYR"]),
        Province("BAL", "water", False, ["BER", "BOT", "DEN", "LVN", "KIE", "PRU", "SWE"]),
        Province("BAR", "water", False, ["NWY", "NWG", "STP/NC"]),
        Province("BEL", "coast", True, ["BUR", "ENG", "HOL", "NTH", "PIC", "RUH"]),
        Province("BER", "coast", True, ["BAL", "KIE", "MUN", "PRU", "SIL"]),
        Province("BLA", "water", False, ["ANK", "ARM", "BUL/EC", "CON", "RUM", "SEV"]),
        Province("BOH", "land", False, ["GAL", "MUN", "SIL", "TYR", "VIE"]),
        Province("BOT", "water", False, ["BAL", "FIN", "SWE", "STP/SC", "LVN"]),
        Province("BUD", "land", True, ["GAL", "RUM", "SER", "TRI", "VIE"]),
        Province("BRE", "coast", True, ["ENG", "GAS", "MAO", "PAR", "PIC"]),
        Province("BUL/EC", "coast", True, ["BLA", "CON", "RUM"]),
        Province("BUL/SC", "coast", True, ["AEG", "CON", "GRE"]),
        Province("BUL", "coast", True, ["AEG", "BLA", "CON", "GRE", "RUM", "SER"]),
        Province("BUR", "land", False, ["BEL", "GAS", "RUH", "MAR", "MUN", "PAR", "PIC"]),
        Province("CLY", "coast", False, ["EDI", "LVP", "NAO", "NWG"]),
        Province("CON", "coast", True, ["AEG", "BUL/EC", "BUL/SC", "BLA", "ANK", "SMY"]),
        Province("DEN", "coast", True, ["BAL", "HEL", "KIE", "NTH", "SKA", "SWE"]),
        Province("EDI", "coast", True, ["CLY", "LVP", "NTH", "NWG", "YOR"]),
        Province("EAS", "water", False, ["AEG", "ION", "SMY", "SYR"]),
        Province("ENG", "water", False, ["BEL", "BRE", "IRI", "LON", "MAO", "NTH", "PIC", "WAL"]),
        Province("FIN", "coast", False, ["BOT", "NWY", "STP/SC", "SWE"]),
        Province("GAL", "land", False, ["BOH", "BUD", "RUM", "SIL", "UKR", "VIE", "WAR"]),
        Province("GAS", "coast", False, ["BUR", "BRE", "MAO", "MAR", "PAR", "SPA/NC"]),
        Province("GRE", "coast", True, ["AEG", "ALB", "BUL/SC", "ION", "SER"]),
        Province("HEL", "water", False, ["DEN", "HOL", "KIE", "NTH"]),
        Province("HOL", "coast", True, ["BEL", "HEL", "KIE", "NTH", "RUH"]),
        Province("ION", "water", False, ["ADR", "AEG", "ALB", "APU", "EAS", "GRE", "NAP", "TUN", "TYS"]),
        Province("IRI", "water", False, ["ENG", "LVP", "MAO", "NAO", "WAL"]),
        Province("KIE", "coast", True, ["BAL", "BER", "DEN", "HEL", "HOL", "MUN", "RUH"]),
        Province("LON", "coast", True, ["ENG", "NTH", "YOR", "WAL"]),
        Province("LVN", "coast", False, ["BAL", "BOT", "MOS", "PRU", "STP/SC", "WAR"]),
        Province("LVP", "coast", True, ["CLY", "EDI", "IRI", "NAO", "WAL", "YOR"]),
        Province("LYO", "water", False, ["MAR", "PIE", "SPA/SC", "TUS", "TYS", "WES"]),
        Province("MAO", "water", False, ["BRE", "ENG", "GAS", "IRI", "NAF", "NAO", "POR", "SPA/NC", "SPA/SC", "WES"]),
        Province("MAR", "coast", False, ["BUR", "GAS", "LYO", "PIE", "SPA/SC"]),
        Province("MOS", "land", True, ["LVN", "SEV", "STP", "UKR", "WAR"]),
        Province("MUN", "land", False, ["BER", "BOH", "BUR", "KIE", "RUH", "SIL", "TYR"]),
        Province("NAF", "coast", False, ["MAO", "TUN", "WES"]),
        Province("NAO", "water", False, ["CLY", "IRI", "LVP", "MAO", "NWG"]),
        Province("NAP", "coast", False, ["APU", "ION", "ROM", "TYS"]),
        Province("NWY", "coast", True, ["BAR", "FIN", "NTH", "NWG", "SKA", "STP/NC", "SWE"]),
        Province("NTH", "water", False, ["BEL", "DEN", "EDI", "ENG", "LON", "HEL", "HOL", "NWY", "NWG", "SKA", "YOR"]),
        Province("NWG", "water", False, ["BAR", "CLY", "EDI", "NAO", "NWY", "NTH"]),
        Province("PAR", "land", True, ["BUR", "BRE", "GAS", "PIC"]),
        Province("PIC", "coast", False, ["BEL", "BRE", "BUR", "ENG", "PAR"]),
        Province("PIE", "coast", False, ["LYO", "MAR", "TUS", "TYR", "VEN"]),
        Province("POR", "coast", True, ["MAO", "SPA/NC", "SPA/SC"]),
        Province("PRU", "coast", False, ["BAL", "BER", "LVN", "SIL", "WAR"]),
        Province("ROM", "coast", True, ["APU", "NAP", "TUS", "TYS", "VEN"]),
        Province("RUH", "land", False, ["BEL", "BUR", "HOL", "KIE", "MUN"]),
        Province("RUM", "coast", True, ["BLA", "BUD", "BUL/EC", "GAL", "SER", "SEV", "UKR"]),
        Province("SER", "land", True, ["ALB", "BUD", "BUL", "GRE", "RUM", "TRI"]),
        Province("SEV", "coast", True, ["ARM", "BLA", "MOS", "RUM", "UKR"]),
        Province("SIL", "land", False, ["BER", "BOH", "GAL", "MUN", "PRU", "WAR"]),
        Province("SKA", "water", False, ["DEN", "NWY", "NTH", "SWE"]),
        Province("SMY", "coast", True, ["AEG", "ANK", "ARM", "CON", "EAS", "SYR"]),
        Province("SPA/NC", "coast", True, ["GAS", "MAO", "POR"]),
        Province("SPA/SC", "coast", True, ["LYO", "MAO", "MAR", "POR", "WES"]),
        Province("STP", "land", False, ["BAR", "BOT", "FIN", "LVN", "MOS", "NWY"]),
        Province("STP/NC", "coast", True, ["BAR", "NWY"]),
        Province("STP/SC", "coast", True, ["BOT", "FIN", "LVN"]),
        Province("SWE", "coast", True, ["BAL", "BOT", "DEN", "FIN", "NWY", "SKA"]),
        Province("SYR", "coast", False, ["ARM", "EAS", "SMY"]),
        Province("TRI", "coast", True, ["ADR", "ALB", "BUD", "SER", "TYR", "VEN", "VIE"]),
        Province("TUN", "coast", True, ["ION", "NAF", "TYS", "WES"]),
        Province("TUS", "coast", False, ["LYO", "PIE", "ROM", "TYS", "VEN"]),
        Province("TYR", "land", False, ["BOH", "MUN", "PIE", "TRI", "VEN", "VIE"]),
        Province("TYS", "water", False, ["ION", "LYO", "ROM", "NAP", "TUN", "TUS", "WES"]),
        Province("UKR", "land", False, ["GAL", "MOS", "RUM", "SEV", "WAR"]),
        Province("VEN", "coast", True, ["ADR", "APU", "PIE", "ROM", "TRI", "TUS", "TYR"]),
        Province("VIE", "land", True, ["BOH", "BUD", "GAL", "TRI", "TYR"]),
        Province("WAL", "coast", False, ["ENG", "IRI", "LON", "LVP", "YOR"]),
        Province("WAR", "land", True, ["GAL", "LVN", "MOS", "PRU", "SIL", "UKR"]),
        Province("WES", "water", False, ["MAO", "LYO", "NAF", "SPA/SC", "TUN", "TYS"]),
        Province("YOR", "coast", False, ["EDI", "LON", "LVP", "NTH", "WAL"]),
    ]

class Nation:
    def __init__(self, name, supcents, units):
        self.name = name
        self.supcents = supcents
        self.units = units

class Unit:
    def __init__(self, location, isFleet):
        self.location = location
        self.isFleet = isFleet

    def getType(self):
        if self.isFleet:
            return "Fleet"
        else:
            return "Army"

def create_nations():
    return [
        Nation(
            "Austria",
            ["BUD", "TRI", "VIE"],
            [Unit("BUD", False), Unit("VIE", False), Unit("TRI", True)]
        ),
        Nation(
            "England",
            ["EDI", "LON", "LVP"],
            [Unit("EDI", True), Unit("LON", True), Unit("LVP", False)]
        ),
        Nation(
            "France",
            ["BRE", "MAR", "PAR"],
            [Unit("BRE", True), Unit("MAR", False), Unit("PAR", False)]
        ),
        Nation(
            "Germany",
            ["BER", "KIE", "MUN"],
            [Unit("KIE", True), Unit("BER", False), Unit("MUN", False)]
        ),
        Nation(
            "Italy",
            ["NAP", "ROM", "VEN"],
            [Unit("NAP", True), Unit("ROM", False), Unit("VEN", False)]
        ),
        Nation(
            "Russia",
            ["MOS", "SEV", "STP", "WAR"],
            [Unit("WAR", False), Unit("MOS", False), Unit("SEV", True), Unit("STP/SC", True)]
        ),
        Nation(
            "Turkey",
            ["ANK", "CON", "SMY"],
            [Unit("ANK", True), Unit("CON", False), Unit("SMY", False)]
        )
    ]

class GameState:
    def __init__(self, nations, provinces):
        self.nations = nations
        self.provinces = provinces

def create_gameState():
    nations = create_nations()
    provinces = create_provinces()
    return GameState(nations, provinces)

class Move:
    def __init__(self, unit, target):
        self.unit = unit
        self.targetProvince = target
        self.support = 0

class Support:
    def __init__(self, unit, supported_move):
        self.unit = unit
        self.supported_move = supported_move

def findProvince(name, provinces):
    for game_province in provinces:
            if name == game_province.name:
                return game_province
    print(f"{name} was not found")
    return None

def checkPossibleMoves(gameState, unit):
    # find unit's location as a province object in gamestate
    loc = unit.location
    unit_province = findProvince(loc, gameState.provinces)

    #looks at valid adjacent provinces to unit's locations
    possible_moves = []
 
    neighboring_provinces = []
    for province in unit_province.connections:
        found_province = findProvince(province, gameState.provinces)
        neighboring_provinces.append(found_province)
    
    for province in neighboring_provinces:
        if unit.isFleet and (province.ptype in ["water", "coast"]):
            possible_moves.append(Move(unit, province.name))
        elif (not unit.isFleet) and province.ptype in ["land", "coast"]:
            possible_moves.append(Move(unit, province.name))

    if possible_moves:
        return possible_moves
    else:
        print(f"No possible moves for the {unit.getType()} in {unit.getLocation}")

def displayMoves(moves):
    strings = []
    for move in moves:
        strings.append(move.targetProvince)
    return strings

def checkSupportOptions(gameState, unit):
    loc = unit.location
    unit_province = findProvince(loc, gameState.provinces)
    supporter_possible_moves = checkPossibleMoves(gameState, unit)
    possible_supports = []
    for nation in gameState.nations:
        for test_unit in nation.units:
            if unit.location != test_unit.location:
                #print(f"checking if the {unit.getType()} in {unit.location} can support the {test_unit.getType()} in {test_unit.location}")
                potential_test_unit_moves = checkPossibleMoves(gameState, test_unit)
                #print(displayMoves(potential_test_unit_moves))
                for potential_test_unit_move in potential_test_unit_moves:
                    for possible_move in supporter_possible_moves:
                        if possible_move.targetProvince == potential_test_unit_move.targetProvince:
                            print(f"{unit.getType()} in {unit.location} can support a {test_unit.getType()} of {nation.name} move from {test_unit.location} to {possible_move.targetProvince}")
                            possible_supports.append(Support(unit, potential_test_unit_move))
                        # else: print(f"{unit.getType()} in {unit.location} cannot support the {test_unit.getType()} in {test_unit.location}'s move to {possible_move.targetProvince} :(")

    if possible_supports:
        return possible_supports
    else:
        print(f"No possible supports for the {unit.getType()} in {unit.getLocation}")

def checkConvoyOptions(gameState, unit):
    #to do
    
if __name__ == "__main__":
    gameState = create_gameState()

    test_unit = Unit("CON", False)
    moves = checkPossibleMoves(gameState, test_unit)
    names = displayMoves(moves)
    print(f"The {test_unit.getType()} in {test_unit.location} can move to {names}")

    supports = checkSupportOptions(gameState, test_unit)
    #print(supports)



    
