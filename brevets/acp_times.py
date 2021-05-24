"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    # check if we have a valid brevet distance
    acceptable_brevet_dists = {200, 300, 400, 600, 1000}
    if brevet_dist_km not in acceptable_brevet_dists:
        raise ValueError("Not a valid brevet distance!")

    # a dictionary with key = runs_through, value = max speed & max km
    max_speeds = {
        0: (34, 200),
        1: (32, 300),
        2: (30, 400),
        3: (28, 600),
        4: (26, 1000)
    }

    time_elapsed = 0

    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km

    # calculate the divisions from the segments
    temp = control_dist_km
    calc = temp
    last_num = temp
    parts = [200, 200, 200, 400, 300]
    parts_calc = 0
    # go through, checking how many times control_dist_km splits into parts
    for x in parts:
        calc -= x
        if calc < 0:
            break
        parts_calc += 1
    # if we can't split control_dist_km below
    if parts_calc == 0:
        time_elapsed += (temp / max_speeds[0][0])
    else:
        number_list = []
        for i in range(parts_calc):
            number_list.append(parts[i])
            last_num -= parts[i]
        if last_num <= 0:
            number_list[-1] += last_num
        else:
            number_list.append(last_num)

        for i, x in enumerate(number_list):
            time_elapsed += (x / max_speeds[i][0])
            temp -= max_speeds[i][1]

    h, m = divmod(time_elapsed, 1)
    m = round(m * 60)

    return brevet_start_time.shift(hours = h, minutes = m)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # check if we have a valid brevet distance
    acceptable_brevet_dists = {200, 300, 400, 600, 1000}
    if brevet_dist_km not in acceptable_brevet_dists:
        raise ValueError("Not a valid brevet distance!")

    # a dictionary with key = runs_through, value = max speed & max km
    min_speeds = {
        0: (15, 200),
        1: (15, 400),
        2: (15, 600),
        3: (11.428, 800),
        4: (13.333, 1000),
    }

    time_elapsed = 0

    control_dist_km = round(control_dist_km)
    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km
    # cover France's algorithm
    if control_dist_km <= 60:
        special = 2 / 6
        elapsed = (control_dist_km / special) + 60
        h = int(elapsed / 60)
        m = int(round(elapsed % 60))
        return brevet_start_time.shift(hours = h, minutes = m)

    # calculate the divisions from the segments
    temp = control_dist_km
    calc = temp
    last_num = temp
    parts = [200, 200, 200, 400, 300]
    parts_calc = 0
    # go through, checking how many times control_dist_km splits into parts
    for x in parts:
        calc -= x
        if calc < 0:
            break
        parts_calc += 1
    # if we can't split control_dist_km below
    if parts_calc == 0:
        time_elapsed += (temp / min_speeds[0][0])
    else:
        number_list = []
        for i in range(parts_calc):
            print(i)
            number_list.append(parts[i])
            last_num -= parts[i]
        if last_num <= 0:
            number_list[-1] += last_num
        else:
            number_list.append(last_num)
        print(number_list)

        for i, x in enumerate(number_list):
            print(str(x) + " / " + str(min_speeds[i][0]))
            time_elapsed += (x / min_speeds[i][0])
            temp -= min_speeds[i][1]

    h, m = divmod(time_elapsed, 1)
    m = round(m * 60)

    if control_dist_km == 200 and brevet_dist_km == 200:
        print("in 200 conditional")
        m += 10
    if control_dist_km == 400 and brevet_dist_km == 400:
        print("in 400 conditional")
        m += 20

    print("h = " + str(h) + ", m = " + str(m))

    print(brevet_start_time.shift(hours = h, minutes = m))

    return brevet_start_time.shift(hours = h, minutes = m)
