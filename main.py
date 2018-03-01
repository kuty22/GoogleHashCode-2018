from utils import parssFile
import operator
import math

def calc_diff_btw_pos(posXA, posYA, posXB, posYB):
    f_res_pos = int(posXA) - int(posXB)
    f_res_pos = abs(f_res_pos)
    s_res_pos = int(posYA) - int(posYB)
    s_res_pos = abs(s_res_pos)
    ret_res = f_res_pos + s_res_pos
    return (ret_res)

def calc_best_voiture(list_cars, posStartX, posStartY):
    tab_dist = []
    for a, car in enumerate(list_cars):
        if (car.status == 0):
            pos_car = car.get_position()
            diff_btw_pos = calc_diff_btw_pos(pos_car['x'], pos_car['y'], posStartX, posStartY)
            tab_dist.append(dict({"id": a, "dist" : diff_btw_pos}))
    tab_dist.sort(key=operator.itemgetter("dist"))
    if (len(tab_dist)):
        return (tab_dist[0])
    else:
        return -1

def available_car(list_car):
    for car in list_car:
        if (car.status > 0):
            car.status = car.status - 1


if __name__ == "__main__":

    toto = parssFile('c_no_hurry.in')
    t = toto.get_summary()
    r = toto.get_ride_information()
    r.sort(key=operator.itemgetter('earliest'))

    c = toto.get_cars()
    for car in c:
        car.status = 0

    close_ride = []
    for t in range(t["steps"]):
        available_car(c)
        for i, ride in enumerate(r):
            if (int(ride["earliest"]) <= t and i not in close_ride):
                best_voit = calc_best_voiture(c, ride["startIntCol"], ride["startIntRow"])
                if (best_voit != -1):
                    c[best_voit["id"]].status = best_voit["dist"] + calc_diff_btw_pos(ride["startIntCol"], ride["startIntRow"], ride["endIntCol"], ride["endIntRow"])
                    c[best_voit["id"]].addRide(i)
                    close_ride.append(i)
                    c[best_voit["id"]].move(dict({"x": ride["endIntCol"],"y": ride["endIntRow"]}))
    for car in c:
        res = str(len(car.getRides()))
        list_rides = car.getRides()
        list_rides.reverse()
        for e in list_rides:
            res = res + " {}".format(e)
        print(res)
