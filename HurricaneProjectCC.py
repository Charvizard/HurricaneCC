# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# mortality scale 
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

# damage scale 
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

# write your update damages function here:

def update_damages(damages) : 
    for count in range(len(damages)) : 
        damage = damages[count]
        if damage.lower() == "damages not recorded" : 
            pass
        else : 
            if damage[-1] == "M" :
                damage = damage[:-1] 
                damage = float(damage) 
                damage = damage * 1000000
            else :  
                damage = damage[:-1]
                damage = float(damage)
                damage = damage * 1000000000
        damages[count] = damage
update_damages(damages)
print(damages)

# write your construct hurricane dictionary function here:

def create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths) : 
    hurricane_dict = {}
    for index in range(len(names)) :
        print(index)
        Name = {"Name" : names[index]}
        Month = {"Months" : months[index]}
        Year = {"Year" : years[index]}
        Max_Winds = {"Max Sustained Wind" : max_sustained_winds[index]}
        Area_Affected = {"Areas Affected": areas_affected[index]}
        Damage = {"Damage": damages[index]}
        Death = {"Deaths": deaths[index]}
        hurricane_dict[names[index]] = [Name, Month, Year, Max_Winds, Area_Affected, Damage, Death]
    
    return hurricane_dict

hurricanes = create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print((("----" * 10) + "\n") * 10)

# write your construct hurricane by year dictionary function here:

def dict_by_year(hurricanes, years) :
    hurricane_by_year = {}
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_year = current_cane[2]
        current_year = current_year["Year"]
        if current_year in hurricane_by_year : 
            hurricane_by_year[current_year].append(current_cane)
        else : 
            hurricane_by_year[current_year] = current_cane
    return hurricane_by_year

#print(hurricanes)

# write your count affected areas function here:

def count_affected_areas(hurricanes) : 
    area_affected_count = {}
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_areas = current_cane[4]
        current_areas = current_areas["Areas Affected"] 
        for area in current_areas : 
            if area in area_affected_count : 
                area_affected_count[area] = area_affected_count[area] + 1
            else : 
                area_affected_count[area] = 1
    return area_affected_count

areas_counted = count_affected_areas(hurricanes)
#print(areas_counted)

# write your find most affected area function here:

def most_hit(areas_counted) : 
    highest_hit_area = " "
    highest_hit_amount = 0
    for area in areas_counted : 
        current_hit = areas_counted[area] 
        if current_hit > highest_hit_amount : 
            highest_hit_amount = current_hit
            highest_hit_area = area
        elif current_hit == highest_hit_amount : 
            highest_hit_amount = current_hit 
            highest_hit_area = highest_hit_area + " & " + area
        elif current_hit < highest_hit_amount : 
            pass 
    return "{Area} was the hardest hit, with {amount} hurricanes!".format(Area = highest_hit_area, amount = highest_hit_amount) 
        
print(most_hit(areas_counted))

# write your greatest number of deaths function here:

def find_most_deaths(hurricanes) : 
    most_deaths = 0
    most_deaths_name = " "
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_name = current_cane[0]
        current_name = current_name["Name"]
        current_deaths = current_cane[6]
        current_deaths = current_deaths["Deaths"] 
        if current_deaths > most_deaths : 
            most_deaths = current_deaths
            most_deaths_name = current_name
        elif current_deaths == most_deaths : 
            most_deaths = current_deaths
            most_deaths_names = most_deaths_name + " & " + current_name
        elif current_deaths < most_deaths : 
            pass
    return "Hurricane {Name} had the most deaths at {amount} lives lost".format(Name = most_deaths_name, amount = most_deaths)
 
print(find_most_deaths(hurricanes))

# write your catgeorize by mortality function here:
def mortality_rater(Hurricanes, mortality_scale) : 
    hurricanes_by_mortality = dict.fromkeys([0,1,2,3,4,5])
    print(hurricanes_by_mortality)
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_deaths = current_cane[6]
        current_deaths = current_deaths["Deaths"] 
        if current_deaths >= mortality_scale[4] : 
            if hurricanes_by_mortality[5] != None : 
                hurricanes_by_mortality[5].append(current_cane)
            else : 
                hurricanes_by_mortality[5] = current_cane
        if current_deaths >= mortality_scale[3] and current_deaths < mortality_scale[4] : 
            if hurricanes_by_mortality[4] != None : 
                hurricanes_by_mortality[4].append(current_cane)
            else : 
                hurricanes_by_mortality[4] = current_cane
        if current_deaths >= mortality_scale[2] and current_deaths < mortality_scale[3] : 
            if hurricanes_by_mortality[3] != None : 
                hurricanes_by_mortality[3].append(current_cane)
            else : 
                hurricanes_by_mortality[3] = current_cane
        if current_deaths >= mortality_scale[1] and current_deaths < mortality_scale[2] : 
            if hurricanes_by_mortality[2] != None :  
                hurricanes_by_mortality[2].append(current_cane)
            else : 
                hurricanes_by_mortality[2] = current_cane
        if current_deaths >= mortality_scale[0] and current_deaths < mortality_scale[1] : 
            if hurricanes_by_mortality[1] != None : 
                hurricanes_by_mortality[1].append(current_cane)
            else : 
                hurricanes_by_mortality[1] = current_cane
        if current_deaths == mortality_scale[0] : 
            if hurricanes_by_mortality[0] != None : 
                hurricanes_by_mortality[0].append(current_cane)
            else : 
                hurricanes_by_mortality[0] = current_cane
    return hurricanes_by_mortality
           
#print(mortality_rater(hurricanes, mortality_scale))
# write your greatest damage function here:

def find_most_damage(hurricanes) : 
    most_damage = 0
    most_damage_name = " "
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_name = current_cane[0]
        current_name = current_name["Name"]
        current_damage = current_cane[5]
        try :
            current_damage = int(current_damage["Damage"])
            if current_damage > most_damage : 
                most_damage = current_damage
                most_damage_name = current_name
            elif current_damage == most_damage : 
                most_damage = current_damage
                most_damage_names = most_damage_name + " & " + current_name
            elif current_damage < most_damage : 
                pass
        except ValueError : 
            pass
    return "Hurricane {Name} had the most damage at ${amount}".format(Name = most_damage_name, amount = most_damage)
 
print(find_most_damage(hurricanes))

# write your catgeorize by damage function here:

def damage_rater(Hurricanes, damage_scale) : 
    hurricanes_by_damage = dict.fromkeys([0,1,2,3,4,5])
    print(hurricanes_by_damage)
    for hurricane in (hurricanes) : 
        current_cane = hurricanes[hurricane]
        current_damage = current_cane[5]
        try :
            current_damage = int(current_damage["Damage"])
            if current_damage >= damage_scale[4] : 
                if hurricanes_by_damage[5] != None :
                    hurricanes_by_damage[5].append(current_cane)
                else : 
                    hurricanes_by_damage[5] = current_cane
            if current_damage >= damage_scale[3] and current_damage < damage_scale[4] : 
                if hurricanes_by_damage[4] != None :
                    hurricanes_by_damage[4].append(current_cane)
                else : 
                    hurricanes_by_damage[4] = current_cane
            if current_damage >= damage_scale[2] and current_damage < damage_scale[3] : 
                if hurricanes_by_damage[3] != None :
                    hurricanes_by_damage[3].append(current_cane)
                else : 
                    hurricanes_by_damage[3] = current_cane
            if current_damage >= damage_scale[1] and current_damage < damage_scale[2] : 
                if hurricanes_by_damage[2] != None : 
                    hurricanes_by_damage[2].append(current_cane)
                else : 
                    hurricanes_by_damage[2] = current_cane
            if current_damage >= damage_scale[0] and current_damage < damage_scale[1] : 
                if hurricanes_by_damage[1] != None : 
                    hurricanes_by_damage[1].append(current_cane)
                else : 
                    hurricanes_by_damage[1] = current_cane
        except ValueError : 
            if current_damage == "Damage not recorded" :
                if "Damage not recorded" in hurricanes_by_damage : 
                    hurricanes_by_damage[0].append(current_cane)
                else : 
                    hurricanes_by_damage[0] = current_cane
    return hurricanes_by_damage

print(damage_rater(hurricanes, damage_scale))