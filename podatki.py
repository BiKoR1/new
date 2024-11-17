print("wpisz '1' dla brutto na netto '2' netto na brutto")
ile = input("> ")

if ile == "1":
    brutto = int(input("brutto:"))
    ppk = input("ppk? (tak/nie)") == "tak"

    emerytalna = round(brutto * 0.0976)
    rentowa = round(brutto * 0.015)
    chorobowa = round(brutto * 0.0245)
    suma = emerytalna + rentowa + chorobowa

    zdrowotna = (brutto - suma)*0.09

    if ppk:
        praco = round(brutto * 0.02)
        pracod = round(brutto * 0.015)
    else:
        praco, pracod = 0, 0
    
    koszt = int(input("podaj kwote uzyskania przychodow:"))
    podstawa = round(brutto - suma + pracod - koszt)
    podatek = round(podstawa * 0.12)
    zaliczka = podatek - 300

    nettow = brutto - suma - zdrowotna - praco - zaliczka

    print(f"netto: {nettow}zl")
    print(f"skladka emerytalna: {emerytalna}zl")
    print(f"skladka rentowa: {rentowa}zl")
    print(f"chorobowa: {chorobowa}zl")
    print(f"zuma skladek spolecznych: {suma}zl")
    print(f"skladka zdrowotna: {zdrowotna}zl")
    print(f"zaliczka na podatek: {zaliczka}zl")
    if ppk:
        print(f"pracownika: {praco}zl")
        print(f"pracodawcy: {pracod}zl")
elif ile == "2":
    netto = int(input("netto:"))
    brutto = netto * 0.80