from django.shortcuts import render
from django.http import JsonResponse
from name_random_generator import generate_name_pairs, generate_name_trios, generate_name_quads
import random

def home(request):
    return render(request, 'randomizer/home.html')

def generate_groups(request):
    if request.method == 'POST':
        names = request.POST.getlist('names[]')
        group_type = request.POST.get('group_type')
        
        if not names:
            return JsonResponse({'error': 'Please add some players first!'})
            
        if group_type == 'pairs':
            if len(names) < 2:
                return JsonResponse({'error': 'Need at least 2 players for pairs!'})
            groups = generate_name_pairs(names.copy())
            
        elif group_type == 'trios':
            if len(names) < 3:
                return JsonResponse({'error': 'Need at least 3 players for trios!'})
            groups = generate_name_trios(names.copy())
            
        elif group_type == 'quads':
            if len(names) < 4:
                return JsonResponse({'error': 'Need at least 4 players for quads!'})
            groups = generate_name_quads(names.copy())
            
        elif group_type == 'seven':
            if len(names) != 7:
                return JsonResponse({'error': 'Need exactly 7 players for this option!'})
            names_copy = names.copy()
            random.shuffle(names_copy)
            groups = [
                names_copy[:3],
                names_copy[3:5],
                names_copy[5:]
            ]
            
        # Handle leftover players
        used_names = set()
        for group in groups:
            for name in group:
                used_names.add(name)
                
        leftover = [name for name in names if name not in used_names]
        
        return JsonResponse({
            'groups': [list(group) for group in groups],
            'leftover': leftover
        })
        
    return JsonResponse({'error': 'Invalid request method'})
