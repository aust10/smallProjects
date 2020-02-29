jackalope_population = [0,0]
year_counter = 0


while len(jackalope_population) <1000:

    mate_counter = 0

    for jack in jackalope_population:
        
        if jack >=4 and jack <=8:
            
            mate_counter += 1

    old_jack_count = jackalope_population.count(10)
    print(f'removing {old_jack_count} jacks')

    for i in range(0, old_jack_count):
        jackalope_population.remove(10)

    print(f'adding {(mate_counter // 2) * 2} new babies')

    for i in range(0,mate_counter//2):
        jackalope_population.append(0)
        jackalope_population.append(0)

    jackalope_population = [jack + 1 for jack in jackalope_population]

    year_counter += 1

    print(f'end of year. there are now {len(jackalope_population)} jackalopes and it is year counter is {year_counter}')