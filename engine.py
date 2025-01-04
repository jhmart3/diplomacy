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
    def __init__(self, name, adjective, supcents, units):
        self.name = name
        self.adjective = adjective
        self.supcents = supcents
        self.units = units

class Unit:
    def __init__(self, location, isFleet):
        self.location = location
        self.isFleet = isFleet
        self.cuck = False

    def getType(self):
        if self.isFleet:
            return "Fleet"
        else:
            return "Army"

    def move(self, province):
        self.location = province

def create_nations():
    return [
        Nation(
            "Austria",
            "Austrian",
            ["BUD", "TRI", "VIE"],
            [Unit("BUD", False), Unit("VIE", False), Unit("TRI", True)]
        ),
        Nation(
            "England",
            "English",
            ["EDI", "LON", "LVP"],
            [Unit("EDI", True), Unit("LON", True), Unit("LVP", False)]
        ),
        Nation(
            "France",
            "French",
            ["BRE", "MAR", "PAR"],
            [Unit("BRE", True), Unit("MAR", False), Unit("PAR", False)]
        ),
        Nation(
            "Germany",
            "German",
            ["BER", "KIE", "MUN"],
            [Unit("KIE", True), Unit("BER", False), Unit("MUN", False)]
        ),
        Nation(
            "Italy",
            "Italian",
            ["NAP", "ROM", "VEN"],
            [Unit("NAP", True), Unit("ROM", False), Unit("VEN", False)]
        ),
        Nation(
            "Russia",
            "Russian",
            ["MOS", "SEV", "STP", "WAR"],
            [Unit("WAR", False), Unit("MOS", False), Unit("SEV", True), Unit("STP/SC", True)]
        ),
        Nation(
            "Turkey",
            "Turkish",
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
        self.isHold = False
        if self.unit.location == self.targetProvince:
            self.isHold = True

class Support:
    def __init__(self, unit, supported_move):
        self.unit = unit
        self.supported_move = supported_move
        self.cutOff = False

def findProvince(prov_str, provinces):
    for game_province in provinces:
            if name == game_province.name:
                return game_province
    print(f"{name} was not found")
    return None

# Move Engine
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

    holdMove = Move(unit, unit.location)
    possible_moves.append(holdMove)

    if possible_moves:
        return possible_moves
    else:
        print(f"No possible moves for the {unit.getType()} in {unit.getLocation}")

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
                        if (possible_move.targetProvince == potential_test_unit_move.targetProvince) and (possible_move.targetProvince != unit.location):
                            #print(f"{unit.getType()} in {unit.location} can support a {test_unit.getType()} of {nation.name} move from {test_unit.location} to {possible_move.targetProvince}")
                            possible_supports.append(Support(unit, potential_test_unit_move))
                        # else: print(f"{unit.getType()} in {unit.location} cannot support the {test_unit.getType()} in {test_unit.location}'s move to {possible_move.targetProvince} :(")

    if possible_supports:
        return possible_supports
    else:
        print(f"No possible supports for the {unit.getType()} in {unit.getLocation}")

def checkConvoyOptions(gameState, unit):
    #to do
    return

def checkOptionsOneUnit(gameState, unit):
    return checkPossibleMoves(gameState, unit) + checkSupportOptions(gameState, unit)

def getAllMoves(gameState):
    moves = []
    for nation in nations:
        for unit in nation.units:
            moves = moves + checkOptionsOneUnit(gameState, unit)

# Resolution 
def processTurns(gameState, turn):
    print("------PROCESSING TURN-------")
    outcomes = []

    #resolve supports and cutoff supports
    for order in turn:
        if type(order) is Support: #check for supports in order list
            for schmorder in turn:
                if type(schmorder) is Move: #check for moves in order list that may cancel support or be supported
                    
                    #check if support has been cut
                    if schmorder.targetProvince == order.unit.location:     #need to add scenario where supported move attacks schmorder's location so cutoff doesn't matter
                        order.cutOff = True
                        print(f"{schmorder.unit.getType()} in {schmorder.unit.location} cut off support from the {order.unit.getType()} in {order.unit.location}.")
                    
                    #check if its supporting an actually ordered move
                    if (order.supported_move.unit == schmorder.unit) and (order.supported_move.targetProvince == schmorder.targetProvince):
                        if not order.cutOff:
                            schmorder.support += 1
                            print(f"{order.unit.getType()} in {order.unit.location} successfully added support to {schmorder.unit.getType()} of {schmorder.unit.location}'s attack on {schmorder.targetProvince}.")

    #resolve moves
    for order in turn:
        if type(order) is Move:
            for schmorder in turn:
                if schmorder != order:
                    if type(schmorder) is Move:
                        if (order.targetProvince == schmorder.targetProvince) and (order.support == schmorder.support): # bounce conditions
                            print(f"{order.unit.getType()} from {order.unit.location} bounced with {schmorder.unit.getType()} from {schmorder.unit.location} on the battleground of {order.targetProvince}")
                            order.targetProvince = order.unit.location # send bouncing armies back to where the came from
                            schmorder.targetProvince = schmorder.unit.location # send bouncing armies back to where they came from 
                        if (order.targetProvince == schmorder.targetProvince) and (order.support > schmorder.support): # push conditions
                            for nation in gameState.nations:
                                for unit in nation.units:
                                    if unit == schmorder.unit:
                                        unit.cuck = True
                                        print(f"{nation.adjective} {unit.getType()} in {unit.location} was defeated and pushed by {order.unit.getType()} from {order.unit.location}")

    for nation in gameState.nations:
        for unit in nation.units:
            for order in turn:
                if order.unit == unit:
                    if type(order) is Move:
                        if (unit.location == order.targetProvince) and not order.isHold:
                            print(f"{unit.getType()} in {unit.location} stays put after bouncing.")
                        elif order.isHold:
                            print(f"{unit.getType()} in {unit.location} holds.")
                        else:
                            print(f"Moving {unit.getType()} of {nation.name} from {unit.location} to {order.targetProvince}.")
                        unit.move(order.targetProvince)

    return gameState, outcomes

def getRetreatOptions(gameState, unit):
    for nation in gameState.nations:
        for test_unit in nation.units:
            if test_unit.cuck:
                pot_retreats = checkPossibleMoves(gameState, test_unit)
                retreatOptions = []
                for retreat in pot_retreats:
                    potential_retreat = True
                    for schnation in gameState.nations:
                        for schmunit in schnation.units:
                            if retreat.targetProvince == schmunit.location & (nation != schnation & unit != schmunit):
                                potential_retreat = False
                    if potential_retreat:
                        retreatOptions.append(retreat)
    return retreatOptions




# Command Line Orders
def select_nation(gameState):
    print("Select a nation:")
    for i, nation in enumerate(gameState.nations):
        print(f"{i + 1}. {nation.name}")
    while True:
        try:
            choice = int(input("Enter the number of your chosen nation: "))
            if 1 <= choice <= len(gameState.nations):
                return gameState.nations[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def issue_orders(gameState, nation):
    print(f"\nYou have selected {nation.name}. Here are your units:")
    for i, unit in enumerate(nation.units):
        print(f"{i + 1}. {unit.getType()} in {unit.location}")
    orders = []
    for i, unit in enumerate(nation.units):
        moves = checkPossibleMoves(gameState, unit)
        supports = checkSupportOptions(gameState, unit)

        print(f"\nOptions for {unit.getType()} in {unit.location}:")

        # Display possible moves
        if moves:
            print("Possible moves:")
            for j, move in enumerate(moves):
                msg = f"{j + 1}. "
                if move.isHold:
                    print(msg + "Hold.")
                else:
                    print(msg + f"Move to {move.targetProvince}")
        else:
            print("No possible moves.")

        # Display possible supports
        if supports:
            print("Possible supports:")
            for j, support in enumerate(supports):
                move_target = support.supported_move.targetProvince
                supported_unit = support.supported_move.unit
                print(f"{len(moves) + j + 1}. Support {supported_unit.getType()} from {supported_unit.location} to {move_target}")
        else:
            print("No possible supports.")

        while True:
            try:
                choice = int(input(f"Choose an action for {unit.getType()} in {unit.location}:"))
                if 1 <= choice <= len(moves):
                    selected_move = moves[choice - 1]
                    orders.append(selected_move)
                    print(f"Order added: {unit.getType()} in {unit.location} -> {selected_move.targetProvince}")
                    break
                elif len(moves) < choice <= len(moves) + len(supports):
                    selected_support = supports[choice - len(moves) - 1]
                    orders.append(selected_support)
                    supported_unit = selected_support.supported_move.unit
                    move_target = selected_support.supported_move.targetProvince
                    print(f"Order added: Support {supported_unit.getType()} from {supported_unit.location} to {move_target}")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return orders

if __name__ == "__main__":
    gameState = create_gameState()

    selected_nation = select_nation(gameState)

    while True:
        orders = issue_orders(gameState, selected_nation)

        print("\nYour orders:")
        for order in orders:
            if isinstance(order, Move):
                if not order.isHold:
                    print(f"Move {order.unit.getType()} from {order.unit.location} to {order.targetProvince}.")
                if order.isHold:
                    print(f"{order.unit.getType()} in {order.unit.location} holds.")
            elif isinstance(order, Support):
                supported_unit = order.supported_move.unit
                move_target = order.supported_move.targetProvince
                print(f"Support {supported_unit.getType()} from {supported_unit.location} to {move_target}.")

        gameState = processTurns(gameState, orders)
