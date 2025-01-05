import json

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
        self.startingSupCents = supcents

    def getHoldOrders(self):
        holds = []
        for unit in self.units:
            holds.append(Move(unit, unit.location))
        return holds

class Player:
    def __init__(self, player_name, nation_str):
        self.name = player_name
        self.nation_str = nation_str
        self.pendingOrders = []
    
    def holdAll(self, nation):
        for unit in nation.units:
            self.pendingOrders = []
            self.pendingOrders.append(nation.getHoldOrders())

    def clearOrders(self):
        self.pendingOrders = []
    
class Unit:
    def __init__(self, location, isFleet):
        self.location = location
        self.isFleet = isFleet
        self.isCuck = False

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
        self.season = 1             # 1 for Fall/Spring; 2 for Retreat; 3 for Build

    def to_dict(self):
        return {
            'nations': [nation.to_dict() for nation in self.nations],
            'provinces': [province.to_dict() for province in self.provinces],
            'season': self.season
        }

def create_gameState():
    nations = create_nations()
    provinces = create_provinces()
    return GameState(nations, provinces)

def create_Game():
    players = []
    jm = Player("jm", "Austria")
    players.append(jm)
    Game(create_gameState(), players)

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

def findProvince(prov_str, gameState):
    for game_province in gameState.provinces:
            if prov_str == game_province.name:
                return game_province
    print(f"{prov_str} was not found")
    return None

# Move Engine
def checkPossibleMoves(gameState, unit):
    # find unit's location as a province object in gamestate
    loc = unit.location
    unit_province = findProvince(loc, gameState)

    #looks at valid adjacent provinces to unit's locations
    possible_moves = []
 
    neighboring_provinces = []
    for province in unit_province.connections:
        found_province = findProvince(province, gameState)
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
    unit_province = findProvince(loc, gameState)
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
    unit_loc = findProvince(unit.location, gameState)

    return

def getOptionsOneUnit(gameState, unit):
    return checkPossibleMoves(gameState, unit) + checkSupportOptions(gameState, unit)

def getAllMoves(gameState):
    moves = []
    for nation in nations:
        for unit in nation.units:
            moves = moves + checkOptionsOneUnit(gameState, unit)

# Resolution 
def processMainPhase(gameState, turn):
    print("------PROCESSING TURN-------")

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
                                        unit.isCuck = True
                                        print(f"{nation.adjective} {unit.getType()} in {unit.location} was defeated and pushed by {order.unit.getType()} from {order.unit.location}")

    #actually move units
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

    #recalculate supply centers after movement, ignoring cucks
    for nation in gameState.nations:
        for unit in nation.units:
            unit_loc = findProvince(unit.location, gameState)
            if unit_loc.isSupply and not unit.isCuck:
                if unit.location not in nation.supcents:
                    for schnation in gameState.nations:
                        if unit.location in schnation.supcents and schnation != nation:
                            schnation.supcents.remove(unit.location)
                    nation.supcents.append(unit.location)

    gameState.season = 2

    return gameState

def getRetreatOptions(gameState, unit):
    pot_retreats = checkPossibleMoves(gameState, unit)
    retreatOptions = []
    for retreat in pot_retreats:
        valid_retreat = True
        for schnation in gameState.nations:
            for schmunit in schnation.units:
                if retreat.targetProvince == schmunit.location:
                    valid_retreat = False
        if valid_retreat and retreat.targetProvince != unit.location:
            retreatOptions.append(retreat)
    return retreatOptions

def getPossibleWinterOrders(gameState, nation):

    possibleWinterMoves = []
    #retreat orders
    for unit in nation.units:
        if unit.isCuck:
            retreatOptions = getRetreatOptions(gameState, unit)

    for option in retreatOptions:
        possibleWinterMoves.append(option)    



    return possibleWinterMoves

def findBuildOptions(nation, gameState):
    allowance = len(nation.supcents) - len(nation.units)

    possibleBuilds = []

    if allowance > 0:
        for buildSpot in nation.startingSupCents:
            if buildSpot in nation.supcents:
                occupied = False
                for unit in nation.units:
                    if unit.location == buildSpot:
                        occupied = True
                if not occupied:
                    loc = findProvince(buildSpot, gameState)
                    if loc.ptype == "coast":
                        possibleBuilds.append(Unit(buildSpot, True))
                        possibleBuilds.append(Unit(buildSpot, False))
                    elif loc.ptype == "land":
                        possibleBuilds.append(Unit(buildSpot, False))

    return possibleBuilds

def processRetreatPhase(gameState, orders):
    failed_retreat_units = []
    for order in orders:
        order_failed = False
        for schmorder in orders:
            if order.targetProvince == schmorder.targetProvince:
                order_failed = True
                failed_retreat_units.append(order.unit)
                failed_retreat_units.append(schmorder.unit)
        if not order_failed:
            for nation in gameState.nations:
                for unit in nation.units:
                    if order.unit == unit:
                        unit.move(order.targetProvince)
    for dead_unit in failed_retreat_units:
        for nation in gameState.nations:
            if dead_unit in nation.units:
                nation.units.remove(dead_unit)

    gameState.season = 3

    return gameState

def processBuildPhase(gameState, builds):
    for build in builds:
        for nation in gameState.nations:
            for startingSupCent in nation.startingSupCents:
                if startingSupCent == build.location:
                    nation.units.append(build)

    gameState.season = 1

    return gameState

class Turn:
    def __init__(self, gameState):
        self.gameState = gameState
        self.orders = []

class Package:
    def __init__(self, game_id, player_username, gameState, current_orders, possible_orders):
        self.target = player_username
        self.gameState = gameState
        self.current_orders = current_orders
        self.possible_orders = possible_orders

    def to_json(self):
            def serialize(obj):
                if isinstance(obj, (int, float, str, bool, type(None))):
                    return obj
                elif isinstance(obj, (set, frozenset)):  # Handle sets explicitly
                    return list(obj)
                elif isinstance(obj, list):
                    return [serialize(item) for item in obj]
                elif isinstance(obj, dict):
                    return {key: serialize(value) for key, value in obj.items()}
                elif hasattr(obj, '__dict__'):
                    serialized = {}
                    for key, value in vars(obj).items():
                        # Skip private attributes
                        if not key.startswith('_'):
                            try:
                                serialized[key] = serialize(value)
                            except (TypeError, ValueError) as e:
                                # If we can't serialize it, convert to string
                                serialized[key] = str(value)
                    return serialized
                else:
                    return str(obj)

            try:
                # Serialize the entire object
                serialized_data = serialize(self.__dict__)
                return json.dumps(serialized_data, indent=4)
            except Exception as e:
                print(f"Error during serialization: {str(e)}")
                # Fallback to basic serialization
                return json.dumps({
                    "target": self.target,
                    "error": "Failed to serialize complete game state"
                })

class Game:
    def __init__(self, initial_gameState, players, turnLengthMinutes = 5):
        self.players = players 
        self.turns = []
        self.turns.append(Turn(initial_gameState))
        self.turnLengthMinutes = turnLengthMinutes

    def callOrders(self):
        for player in self.players:
            self.turns[-1].orders.append(player.pendingOrders)

    def setDefaultMainPhaseOrders(self):
        for player in self.players:
            for nation in self.turns[-1].gameState.nations:
                if player.nation_str == nation.name:
                    player.holdAll(nation)

    def clearAllPlayerOrders(self):
        for player in self.players:
            player.pendingOrders = []

    def processCurrentTurn(self):
        currentGameState = self.turns[-1].gameState
        
        season = currentGameState.season

        if season == 1:
            next_gameState = processMainPhase(currentGameState, self.turns[-1].orders)
            self.clearAllPlayerOrders()
        elif season == 2:
            next_gameState = processRetreatPhase(currentGameState, self.turns[-1].orders)
            self.clearAllPlayerOrders()
        elif season == 3:
            next_gameState = processBuildPhase(currentGameState, self.turns[-1].orders)
            self.setDefaultMainPhaseOrders()

        self.turns.append(Turn(next_gameState))

    def getPendingMoves(self, player_name):
        player_current_moves = []

        for player in self.players:
            if player.name == player_name:
                player_current_moves = player.pendingOrders

        return player_current_moves
    
    def getPossibleMoves(self, player_name):
        player_moves = []

        currentGameState = self.turns[-1].gameState

        gameSeason = currentGameState.season

        if gameSeason == 1:                  # MAIN PHASE OPTIONS
            for player in self.players:
                if player.name == player_name:
                    for nation in currentGameState.nations:
                        if player.nation_str == nation.name:
                            for unit in nation.units:
                                player_moves.append(getOptionsOneUnit(currentGameState, unit))

        if gameSeason == 2:                 # RETREAT PHASE OPTIONS
            for player in self.players:
                if player.name == player_name:
                    for nation in self.turns[-1].nations:
                        if player.nation_str == nation.name:
                            for unit in nation.units:
                                if unit.isCuck:
                                    player_moves.append(getRetreatOptions(currentGameState, unit))

        if gameSeason == 3:                 # BUILD PHASE OPTIONS
            for player in self.players:
                if player.name == player_name:
                    for nation in self.turns[-1].nations:
                        if player.nation_str == nation.name:
                            player_moves.append(findBuildOptions(nation, currentGameState))

        return player_moves

    def getPackage(self, player_name):

        gameState = self.turns[-1].gameState
        pending_orders = self.getPendingMoves(player_name)
        possible_orders = self.getPossibleMoves(player_name)
        
        return Package(player_name, gameState, pending_orders, possible_orders)

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


    # send initial gameState
    while True:
        # send gameState and list of possible Fall / Spring orders
        

        # receive Fall / Spring orders from Users
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

        # process turn
        gameState = processTurn(gameState, orders)


        # send gameState list of possible Winter / Summer orders
        winter_options = getPossibleWinterOrders(gameState, selected_nation)

        for option in winter_options:
            if type(option) is Move:
                print(f"Defeated {option.unit.getType()} in {option.unit.location} can retreat to {option.targetProvince}")

        # receive Summer / Winter orders from Users



        # process Summer / Winter orders



