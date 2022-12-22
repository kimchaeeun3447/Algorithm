def solution(cache_size, cities):
    cache = []
    time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5

            if cache_size == 0:
                continue

            if len(cache) >= cache_size:
                cache.pop(0)

            cache.append(city)

    return time