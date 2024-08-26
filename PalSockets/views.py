from django.shortcuts import render
from django.http import JsonResponse
from PalSockets.controls.palworld.PalSocket import PalConnect


def players(requests):
    return JsonResponse(PalConnect.get_players(),safe=False)

def metric(requests):
    return JsonResponse(PalConnect.get_metrics(),safe=False)