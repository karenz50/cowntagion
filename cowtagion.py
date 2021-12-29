def get_input():
    total_farm = int(input(""))
    path_list = []
    for i in range(total_farm - 1):
        cur_path = input("").split()
        path_list.append(sorted([int(i) for i in cur_path]))
    
    return total_farm, sorted(path_list)

def calc_double_cow_time( total_farm ):
    required_cows = 1
    days_passed = 0
    while required_cows < total_farm:
        required_cows *= 2
        days_passed += 1

    return days_passed

def check_if_infect_farm_in_list( cur_path, infected_farm_list ):
    if cur_path not in infected_farm_list.keys():
        return False
    return True

def calc_path_time( total_farm, path_list ):
    infected_farm_list = {}
    total_path_count = 0
    for cur_path in path_list:
        if len(infected_farm_list) == total_farm:
            break
        elif check_if_infect_farm_in_list(cur_path[1], infected_farm_list) != True:
            infected_farm_list[cur_path[1]] = 1
            total_path_count += 1

    return total_path_count


def calc_total_time( total_farm, path_list ):
    days_passed = calc_double_cow_time(total_farm) + calc_path_time(total_farm, path_list)
    
    return days_passed

if __name__ == "__main__":
    total_farm, path_list = get_input()
    #total_farm, path_list = 4, [[1, 2], [1, 3], [1, 4]]
    print(calc_total_time(total_farm, path_list))
