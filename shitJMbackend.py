class Province:
    def __init__(self, name, type, isSupply, connections)
        self.name = name
        self.connections = connections
        self.type = 
        self.isSupply = isSupply

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
        Province("BUD", "land", True, ["GAL", "RUM", "SER", "TRI", "VIE"]),
        Province("BRE", "coast", True, ["ENG", "GAS", "MAO", "PAR", "PIC"]),
        Province("BUL/EC", "coast", True, ["BLA", "CON", "RUM"]),
        Province("BUL/SC", "coast", True, ["AEG", "CON", "GRE"]),
        Province("bul", "coast", True, ["AEG", "BLA", "CON", "GRE", "RUM", "SER"]),
        Province("BUR", "land", False, ["BEL", "GAS", "RUH", "MAR", "MUN", "PAR", "PIC", "SWI"]),
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
        Province("MAR", "coast", False, ["BUR", "GAS", "LYO", "PIE", "SPA/SC", "SWI"]),
        Province("MOS", "land", True, ["LVN", "SEV", "STP", "UKR", "WAR"]),
        Province("MUN", "land", False, ["BER", "BOH", "BUR", "KIE", "RUH", "SIL", "TYR", "SWI"]),
        Province("NAF", "coast", False, ["MAO", "TUN", "WES"]),
        Province("NAO", "water", False, ["CLY", "IRI", "LVP", "MAO", "NWG"]),
        Province("NAP", "coast", False, ["APU", "ION", "ROM", "TYS"]),
        Province("NWY", "coast", True, ["BAR", "FIN", "NTH", "NWG", "SKA", "STP/NC", "SWE"]),
        Province("NTH", "water", False, ["BEL", "DEN", "EDI", "ENG", "LON", "HEL", "HOL", "NWY", "NWG", "SKA", "YOR"]),
        Province("NWG", "water", False, ["BAR", "CLY", "EDI", "NAO", "NWY", "NTH"]),
        Province("PAR", "land", True, ["BUR", "BRE", "GAS", "PIC"]),
        Province("PIC", "coast", False, ["BEL", "BRE", "BUR", "ENG", "PAR"]),
        Province("PIE", "coast", False, ["LYO", "MAR", "TUS", "TYR", "VEN", "SWI"]),
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
        Province("stp", "coast", False, ["BAR", "BOT", "FIN", "LVN", "MOS", "NWY"]),
        Province("STP/NC", "coast", True, ["BAR", "NWY"]),
        Province("STP/SC", "coast", True, ["BOT", "FIN", "LVN"]),
        Province("SWE", "coast", True, ["BAL", "BOT", "DEN", "FIN", "NWY", "SKA"]),
        Province("SYR", "coast", False, ["ARM", "EAS", "SMY"]),
        Province("TRI", "coast", True, ["ADR", "ALB", "BUD", "SER", "TYR", "VEN", "VIE"]),
        Province("TUN", "coast", True, ["ION", "NAF", "TYS", "WES"]),
        Province("TUS", "coast", False, ["LYO", "PIE", "ROM", "TYS", "VEN"]),
        Province("TYR", "land", False, ["BOH", "MUN", "PIE", "TRI", "VEN", "VIE", "SWI"]),
        Province("TYS", "water", False, ["ION", "LYO", "ROM", "NAP", "TUN", "TUS", "WES"]),
        Province("UKR", "land", False, ["GAL", "MOS", "RUM", "SEV", "WAR"]),
        Province("VEN", "coast", True, ["ADR", "APU", "PIE", "ROM", "TRI", "TUS", "TYR"]),
        Province("VIE", "land", True, ["BOH", "BUD", "GAL", "TRI", "TYR"]),
        Province("WAL", "coast", False, ["ENG", "IRI", "LON", "LVP", "YOR"]),
        Province("WAR", "land", True, ["GAL", "LVN", "MOS", "PRU", "SIL", "UKR"]),
        Province("WES", "water", False, ["MAO", "LYO", "NAF", "SPA/SC", "TUN", "TYS"]),
        Province("YOR", "coast", False, ["EDI", "LON", "LVP", "NTH", "WAL"]),
    ]

class nation:
    def __init__(self, name, supplycenters, units):
        self.name = name
        self.units 

class unit:
    def __init__(self, loc, isFleet):
        self.loc = loc
        self.isFleet = isFleet

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


