from time import time
import re
from cmath import inf
start = time()

particles = dict()

with open('day20input.txt', 'r') as fin:
    tmp = fin.read().rstrip().split('\n')
    i = 0
    min_dist = [-1, inf]
    for particle in tmp:
        tmp_particle = re.findall(r'-?\d+', particle)
        particles[i] = dict()
        particles[i]['p'] = [int(i) for i in tmp_particle[0:3]]
        particles[i]['v'] = [int(i) for i in tmp_particle[3:6]]
        particles[i]['a'] = [int(i) for i in tmp_particle[6:9]]
        particles[i]['dist'] = sum([abs(x) for x in particles[i]['p']])
        if particles[i]['dist'] < min_dist[1]:
            min_dist = [i, particles[i]['dist']]
        i += 1
    print(min_dist)


def tick():
    min_dist = [-1, inf]
    positions = list()
    collisions = list()
    colliding_particles = list()
    for i in particles.keys():
        for j in range(3):
            particles[i]['v'][j] += particles[i]['a'][j]
            particles[i]['p'][j] += particles[i]['v'][j]
        particles[i]['dist'] = sum([abs(x) for x in particles[i]['p']])
        if particles[i]['dist'] < min_dist[1]:
            min_dist = [i, particles[i]['dist']]
        if particles[i]['p'] not in positions:
            positions.append(particles[i]['p'])
        else:
            collisions.append(particles[i]['p'])
    for i in particles.keys():
        if particles[i]['p'] in collisions:
            colliding_particles.append(i)
    for particle in colliding_particles:
        particles.pop(particle)
    print(min_dist, len(particles))


def part_one():
    counter = 0
    while counter < 50:
        tick()
        counter += 1


part_one()

print('finished in ' + str(time() - start) + ' seconds')