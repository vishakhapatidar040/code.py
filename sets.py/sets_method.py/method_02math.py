set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#union method
#do set ko combine krta hai aur unique elements ko return krta hai
union_set = set_a.union(set_b) 
print(union_set) # Output: {1, 2, 3, 4, 5, 6}

#intersection method
#do set ke common elements ko return krta hai
intersection_set = set_a.intersection(set_b)
print(intersection_set) # Output: {3, 4}

#difference method
#do set ke unique elements ko return krta hai
difference_set = set_a.difference(set_b)
print(difference_set) # Output: {1, 2}

#symmetric difference method
#print jo common nhi h aur unique elements ko return krta hai
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set) # Output: {1, 2, 5, 6}

#issubset method
#check krta hai ki ek set doosre set ka subset hai ya nhi
is_subset = set_a.issubset(set_b)
print(is_subset) # Output: False

#issuperset method
#check krta hai ki ek set doosre set ka superset hai ya nhi
is_superset = set_a.issuperset(set_b)
print(is_superset) # Output: False

#disjoint method
#check krta hai ki do set ke koi common elements hai ya nhi
#agr common nhi hai to true or ho to false return krta hai
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint) # Output: False

