#!/usr/bin/env python
##############################################################################
# File: models.py
# Purpose: Module containing Diplomacy objects
#
# Author: Jack Martin (jmartin2017@gmail.com)
# Copyright (C) 2025 MIT License - All Rights Reserved
# The contents of this header may not be removed under any circumstance
##############################################################################

class Province:
    def __init__(self, name, ptype, isSupply, connections):
        self.name = name
        self.ptype = ptype
        self.isSupply = isSupply
        self.connections = connections

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