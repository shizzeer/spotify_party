import random
import string
from itertools import combinations


def find_common_tracks(tracks_ids):
    # Generate all possible combinations of 'priority' number of sets
    for combination in combinations(tracks_ids, 2):
        # Find common elements in the current combination of sets
        common_elements = set.intersection(*combination)

        # If common elements exist, proceed with further processing
        if common_elements:
            # Create a list of remaining sets, excluding the current combination
            remaining_sets = [s for s in tracks_ids if s not in combination]

            # Subtract elements from the remaining sets
            common_elements_copy = common_elements.copy()  # Create a copy of common_elements
            for remaining_set in remaining_sets:
                common_elements_copy -= remaining_set
            return common_elements_copy

    return {}