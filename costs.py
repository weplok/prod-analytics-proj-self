import numpy as np  # type: ignore
import math


def add_cost_2013(x):
    if x[0] == "casual":
        final_cost = 7
        if x[1] > 30: final_cost += 2
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8
        return final_cost
    else:
        final_cost = 0.0
        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 4.5
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6
        return final_cost


def add_cost_2014(x):
    if x[0] == "casual":
        final_cost = 7
        if x[1] > 30: final_cost += 2
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8
        return final_cost
    else:
        final_cost = 0.0
        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 4.5
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6
        return final_cost


def add_cost_2015(x):
    if x[0] == "casual":
        final_cost = 9.95
        if x[1] > 30: final_cost += 2
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8
        return final_cost
    else:
        final_cost = 0.0
        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 4.5
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6
        return final_cost


def add_cost_2016(x):
    if x[0] == "casual":
        final_cost = 9.95
        if x[1] > 30: final_cost += 2
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8
        return final_cost
    else:
        final_cost = 0.0
        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 4.5
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6
        return final_cost


def add_cost_2017(x):
    if x[0] == "casual":
        final_cost = 15
        if x[1] > 30: final_cost += 1
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8
        return final_cost
    else:
        final_cost = 0.0
        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 3
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6
        return final_cost


def add_cost_2018(x):
    if x[0] == "casual":
        if x[1] > 45:
            final_cost = 15
            if x[1] > 180:
                final_cost += (round(x[1]) - 180) * 0.15
            return final_cost
        else:
            final_cost = 3
            if x[1] > 30:
                final_cost += (round(x[1]) - 30) * 0.15
            return final_cost
    else:
        final_cost = 0
        if x[1] >= 45:
            final_cost += (round(x[1]) - 45) * 0.15
        return final_cost


def add_cost_2019(x):
    if x[0] == "casual":
        if x[1] > 45:
            final_cost = 15
            if x[1] > 180:
                final_cost += (round(x[1]) - 180) * 0.15
            return final_cost
        else:
            final_cost = 3
            if x[1] > 30:
                final_cost += (round(x[1]) - 30) * 0.15
            return final_cost
    else:
        final_cost = 0
        if x[1] >= 45:
            final_cost += (round(x[1]) - 45) * 0.15
        return final_cost


def add_cost_2020(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.15
                return final_cost
            else:
                final_cost = 3
                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.15
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.15
            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.20
                return final_cost
            else:
                final_cost = 3
                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.20
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.15
            return final_cost


def add_cost_2021(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.15
                return final_cost
            else:
                final_cost = 3.30
                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.15
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.15
            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.20
                return final_cost
            else:
                final_cost = 3
                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.20
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.15
            return final_cost


def add_cost_2022(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.16
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.16
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.16
            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15
                final_cost += round(x[1]) * 0.39
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.39
                return final_cost
        else:
            final_cost = 0
            final_cost += round(x[1]) * 0.16
            return final_cost


def add_cost_2023(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 16.5
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.17
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.17
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.17
            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 16.5
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.17
                final_cost += round(x[1]) * 0.42
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.42
                return final_cost
        else:
            final_cost = 0
            final_cost += round(x[1]) * 0.17
            return final_cost


def add_cost_2024(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 18.1
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.18
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.18
                return final_cost
        else:
            final_cost = 0
            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.17
            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 18.1
                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.18
                final_cost += round(x[1]) * 0.44
                return final_cost
            else:
                final_cost = 1
                final_cost += round(x[1]) * 0.44
                return final_cost
        else:
            final_cost = 0
            final_cost += round(x[1]) * 0.18
            return final_cost
