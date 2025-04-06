def chocolate_parsel(finalparcel, n_small, w_small, n_medium, w_medium, n_large, w_large):
    if w_small > w_medium or w_medium > w_large or w_small > w_large:
        print("-1 -1 -1")
        return

    # Büyük çikolatadan başla, sonra orta, sonra küçük
    for used_large in range(n_large, -1, -1):
        for used_medium in range(n_medium, -1, -1):
            for used_small in range(n_small, -1, -1):
                total_weight = (
                    used_large * w_large +
                    used_medium * w_medium +
                    used_small * w_small
                )
                if total_weight == finalparcel:
                    print(f"{used_small} {used_medium} {used_large}")
                    return
    print("-1 -1 -1")

secrequest = []
myinp = input()
request = myinp.split(" ")
if len(request) == 7:
    for i in request:
        secrequest.append(int(i))
    chocolate_parsel(secrequest[0], secrequest[1], secrequest[2],
                     secrequest[3], secrequest[4], secrequest[5], secrequest[6])
