import random
from random import randint
from data.data import landscape_subtypes, seascapes_subtypes, coastal_subtypes
from .data import data

def main():
    while True:
        world = {}
        inpt = input('Do you want to generate a random world? ')
        if 'y' not in inpt.lower():
            break

        name = input("What shall we name your world? ")
        world['name'] = name
        hot = False
        cold = False
        wet = False
        dry = False


        for feature in data.all_list:

            if feature == 'landscapes':
                list_ = data.landscapes
            elif feature == 'seascapes':
                list_ = data.seascapes
            elif feature == 'coastal':
                list_ = data.coastal

            elif feature == 'features':
                ...
                continue
                list_ = data.features

            ...
            len_list = len(list_)
            counter = 0
            while True:
                counter+=1
                if counter > 10:
                    print(world)
                    print(hot, cold, wet, dry)
                    raise("Infinite loop")
                rand = random.randint(0,len_list-1)
                feat = list_[rand]
                traits = has_traits(feat)
                if 'hot' in traits and cold == True:
                    continue
                elif 'hot' in traits:
                    hot = True

                if 'cold' in traits and hot == True:
                    continue
                elif 'cold' in traits:
                    cold = True

                if 'wet' in traits and dry == True:
                    continue
                elif 'wet' in traits:
                    wet = True
                if 'dry' in traits and wet == True:
                    continue
                elif 'dry' in traits:
                    dry = True

                world[feature] = feat
                break
        subtype_dict = {}
        for k,v in world.items():
            if k == 'landscapes':
                category = landscape_subtypes[v]
            elif k == 'seascapes':
                category = seascapes_subtypes[v]
            elif k == 'coastal':
                category = coastal_subtypes[v]
            else:
                continue

            while True:
                rand = randint(0,len(category)-1)
                selection = category[rand]
                traits = has_traits(selection)
                if 'hot' in traits and cold == True:
                    continue
                elif 'cold' in traits and hot == True:
                    continue
                elif 'wet' in traits and dry == True:
                    continue
                elif 'dry' in traits and wet == True:
                    continue

                if 'cold' in traits:
                    cold = True
                if 'wet' in traits:
                    wet = True
                if 'hot' in traits:
                    hot = True
                if 'dry' in traits:
                    dry = True

                subtype_dict[f"{k} subtype: "] = selection
                break
        world.update(subtype_dict)

        for k,v in world.items():
            print(f'{k}: {v}')

        print("Additional traits: ", end="")

        traits = []
        if hot:
            traits.append('hot')
        if cold:
            traits.append('cold')
        if wet:
            traits.append('wet')
        if dry:
            traits.append('dry')
        for trait in traits:
            print(trait, " ", end="")
        print()

def has_traits(feature):
    trait_list = []
    for k,v in data.traits.items():
        if feature in v:
            trait_list.append(k)
    return trait_list
main()

